"""Usage:
  python run_ingest.py --check                       # confirm app titles only
  python run_ingest.py --sources playstore --limit 50  # small trial run
  python run_ingest.py                               # everything
"""
import argparse, importlib, json, os
from pathlib import Path
import yaml
from src.process.pipeline import run

SOURCES = ["playstore", "appstore", "tradingqna", "youtube", "reddit_api", "csv_upload"]
ap = argparse.ArgumentParser()
ap.add_argument("--sources", default=",".join(SOURCES))
ap.add_argument("--limit", type=int, default=None, help="small cap per source for trial runs")
ap.add_argument("--check", action="store_true")
a = ap.parse_args()
cfg = yaml.safe_load(open("config.yaml"))
if os.environ.get("INGEST_SALT") is None:
    print("note: set INGEST_SALT to any secret string so author hashes can't be reversed")

if a.check:
    from google_play_scraper import app
    for k, v in cfg["apps"].items():
        try: print(k, "->", app(v["play"], country="in")["title"])
        except Exception as e: print(k, "NOT FOUND", e)
    raise SystemExit

Path("data/raw").mkdir(parents=True, exist_ok=True)
docs, errors = [], {}
for s in a.sources.split(","):
    try:
        got = importlib.import_module(f"src.ingest.{s}").fetch(cfg, limit=a.limit)
        with open(f"data/raw/{s}.jsonl", "w", encoding="utf-8") as f:
            for d in got: f.write(json.dumps(d, ensure_ascii=False, default=str) + "\n")
        docs += got
    except Exception as e:
        errors[s] = str(e); print(f"!! {s} failed: {e}")
if not docs:
    raise SystemExit("no documents collected; see messages above")
df, funnel, rep = run(docs, errors)
print("\nFunnel:", funnel)
for s, v in rep["sources"].items(): print(f"  {s:12} fetched {v['fetched']:>5}  relevant {v['relevant']:>5}  (core {v['core']})")
print("\nOutputs: data/clean/docs.csv, data/clean/relevance_qa_sample.csv, data/extracted/ingest_report.json")
