# Coin SIP Discovery Engine

Research app that mines public conversations to explain why first-time mutual fund investors pause, reduce or stop SIPs on Zerodha Coin, and ranks opportunity areas.

Metric: % of first-time investors with an active SIP 12 months after their first SIP (active = at least one successful instalment in the last 30 days).

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Status
Starter UI running on sample data (the app shows a "Sample data" label). Real results in `data/extracted/` override the sample automatically.

Public-conversation analysis for product discovery. Not investment advice.
