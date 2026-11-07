import pandas as pd
import streamlit as st
from src.ui import setup, card

d = setup("Opportunities")
o = pd.DataFrame(d["opportunities"])
o.insert(0, "Rank", range(1, len(o) + 1))
cfg = {c: st.column_config.ProgressColumn(c.title(), min_value=0, max_value=100, format="%d")
       for c in ["score", "reach", "severity", "proximity", "addressability", "evidence"]}
st.dataframe(o, column_config=cfg, use_container_width=True, hide_index=True)
pick = st.selectbox("Opportunity card", o["title"])
r = o[o["title"] == pick].iloc[0]
tag = "Robust across weightings" if r["robust"] else "Not robust across weightings"
card(f"<b>{r['title']}</b><br>Score {r['score']} | {tag}<br>"
     "<span class='muted'>Full card (problem, who, journey link, evidence, unknowns, solution directions) "
     "is generated after scoring runs.</span>")
st.caption("Weights are set in config and tested under five weightings. Items that break the no-advice, no-FOMO rules are marked Blocked.")
