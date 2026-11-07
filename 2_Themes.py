import pandas as pd
import streamlit as st
from src.ui import setup, card

d = setup("Themes")
t = pd.DataFrame(d["themes"]).rename(columns={"label": "Theme", "definition": "Definition", "n_docs": "Docs (n)",
                                              "stability": "Stability", "origin": "Origin"})
st.dataframe(t, use_container_width=True, hide_index=True)
pick = st.selectbox("Theme detail", t["Theme"])
row = t[t["Theme"] == pick].iloc[0]
card(f"<b>{row['Theme']}</b><br>{row['Definition']}<br><span class='muted'>n = {row['Docs (n)']} | {row['Stability']} | {row['Origin']}</span>")
st.caption("The cluster map appears here once embeddings and clustering have run.")
