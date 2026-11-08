"""python run_pipeline.py <command>
  extract         structured extraction (backend set in config.yaml; rules needs no key)
  import-manual   import JSON replies saved in data/extracted/manual/
  analyze         themes, quantification, opportunity scoring, dashboard export
  golden-sheet    create the blind 20-item labelling sheet
  golden-score    compare your labels with the AI output, write the evidence log
  consistency     re-run the golden documents at higher temperature to measure run-to-run agreement
  all             extract, then analyze"""
import sys
from src.process import extract, themes, quantify, score, export_ui
from src.process.common import cfg
from src.eval import golden
import pandas as pd

c = sys.argv[1] if len(sys.argv) > 1 else ""
if c == "extract": extract.run()
elif c == "import-manual": extract.manual_import()
elif c in ("analyze", "all"):
    if c == "all": extract.run()
    q = quantify.run(); t = themes.run(); o = score.run(q); d = export_ui.run(q, t, o)
    print(f"{q['n_docs']} docs, {q['n_stop']} stop signals, {q['n_stop_with_reason']} with a reason")
    for x in o[:5]: print(f"  #{x['rank']} {x['title']}  score {x['score']}  robust={x['robust']} blocked={x['blocked']}")
elif c == "golden-sheet": print("rows:", golden.make_sheet())
elif c == "golden-score": golden.score()
elif c == "consistency":
    ids = pd.read_csv("data/golden/golden_sheet.csv")["doc_id"].tolist()
    extract.run(only_ids=ids, out_name="extractions_run2.jsonl", temperature=cfg()["extraction"]["consistency_temperature"])
else: print(__doc__)
