import io
import pandas as pd
import streamlit as st
from src.ui import setup

setup("Evidence Log")
st.progress(0.0, text="Golden set: 0 of 20 items labelled")
c = st.columns(4)
for col, name in zip(c, ["Field accuracy", "Macro-F1", "Quote grounding rate", "Run-to-run kappa"]):
    col.metric(name, "n/a")
st.caption("Metrics appear once the golden set is labelled and extraction has run.")
cols = ["item_id", "source", "text_excerpt", "ai_output", "human_label", "verdict", "error_type",
        "action_taken", "prompt_version", "date"]
buf = io.StringIO()
pd.DataFrame(columns=cols).to_csv(buf, index=False)
st.download_button("Download evidence log template (CSV)", buf.getvalue(), "evidence_log_template.csv", "text/csv")
st.markdown("**Verdict options:** Agree, AI wrong, Human wrong, Ambiguous.")
