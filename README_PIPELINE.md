# Extraction, scoring and evidence log

Run on your own computer after `python run_ingest.py` has produced `data/clean/docs.csv`.

## 1. Pick an extraction backend (config.yaml, `extraction.backend`)
| Backend | Needs | Use it for |
|---|---|---|
| `gemini` | free key from Google AI Studio, then `export GEMINI_API_KEY=...` (Windows: `set GEMINI_API_KEY=...`). Check the model name in AI Studio and update `gemini_model`. | Main run, no cost on the free tier (mind rate limits) |
| `anthropic` | `ANTHROPIC_API_KEY` | If you get a key |
| `manual` | nothing | No key: `python run_pipeline.py extract` writes prompt files to `data/extracted/manual/`. Paste each into Claude or Gemini, save the JSON reply as `batch_001.json` (same number), then `python run_pipeline.py import-manual` |
| `rules` | nothing | Keyword baseline, not AI. Use it as a comparison in your evidence log |

## 2. Run
```
python run_pipeline.py extract      # or import-manual
python run_pipeline.py analyze      # themes, quantification, scoring, dashboard
```
Outputs in `data/extracted/`: `extractions.jsonl`, `quant.json`, `themes.json`, `opportunities.json`, `dashboard.json`. Commit `dashboard.json`, `quant.json`, `themes.json`, `opportunities.json`, `eval_metrics.json`, `ingest_report.json` and `funnel.json` to GitHub. The Streamlit app switches from sample to real data and drops the "Sample data" label automatically.

## 3. Golden set and evidence log
```
python run_pipeline.py golden-sheet   # creates data/golden/golden_sheet.csv (text only, AI output hidden)
```
Fill the `human_*` columns for all 20 rows BEFORE opening `golden_ai.csv`. Allowed values are the ones in `prompts/extraction.md`. Then:
```
python run_pipeline.py consistency    # re-runs those 20 at higher temperature (skip for rules backend)
python run_pipeline.py golden-score   # agreement, F1, grounding, kappa; writes data/golden/evidence_log.csv
```
Open `evidence_log.csv`, fill `error_type` and `action_taken` for every Disagree or Partly agree row, and copy 2 to 3 examples into your Evidence Log document.

## What was tested
Tested offline on synthetic documents with the `rules` and `manual` backends, including the quote-grounding check. The Gemini and Anthropic calls are written to each provider's documented REST format but have not been run against the live APIs. Run `python run_pipeline.py extract` on 5 documents first and read the output before the full run.

## Analyst-set parts to disclose
Leak mapping, `proximity` and `addressability` scores per reason code are priors set in `config.yaml`, not measured. Say so in the deck. The ranking is tested under 5 weightings, and an opportunity is "robust" only if it stays in the top 5 in at least 4 of them.
