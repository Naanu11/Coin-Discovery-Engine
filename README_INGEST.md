# Data collection guide

Run on your own computer (not on Streamlit Cloud).

## One-time setup
```
pip install -r requirements-ingest.txt
export INGEST_SALT="any-secret-text"          # Windows: set INGEST_SALT=any-secret-text
```

## Run
```
python run_ingest.py --check                         # confirms the app package names
python run_ingest.py --sources playstore --limit 50  # small trial
python run_ingest.py                                 # everything
```
Optional keys: `YOUTUBE_API_KEY` (YouTube Data API v3), `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` (only if you already hold approved Reddit API credentials).

## Reddit, social media and survey data (manual CSV)
Reddit no longer allows new API access or anonymous scraping. Collect threads by hand instead:
1. Search each subreddit in your browser (for example `SIP stopped`, `pause SIP`, `SIP failed`).
2. Open each relevant thread and copy the post and useful comments into a copy of `data/uploads/TEMPLATE.csv`, one row per post or comment, with the thread URL.
3. Save it as `data/uploads/reddit_<topic>.csv`. Do the same for X, Instagram, Telegram and survey free-text answers, using `source` to say which one.
These files are loaded automatically and never committed to GitHub (see `.gitignore`).

## What you get
- `data/clean/docs.csv`: cleaned, de-duplicated, relevant documents with topic tags
- `data/clean/docs_all.csv`: everything, with `drop_reason` for rejected rows
- `data/clean/relevance_qa_sample.csv`: 40 random kept rows per source. Read these and check they are on topic.
- `data/extracted/funnel.json` and `ingest_report.json`: shown on the app's Data Sources page
