import pandas as pd
import streamlit as st
from src.ui import setup

setup("Data Sources")
src = pd.DataFrame({
    "Source": ["Play Store", "App Store", "Reddit", "YouTube", "TradingQ&A", "Social uploads", "Survey", "Interviews"],
    "Access": ["Public reviews", "Official feed", "Official API", "Data API", "Respects robots.txt", "Manual upload", "CSV upload", "File upload"],
    "Status": ["Not connected"] * 8})
st.dataframe(src, use_container_width=True, hide_index=True)
up = st.file_uploader("Add survey CSV, interview notes, or social exports", type=["csv"])
if up is not None:
    st.dataframe(pd.read_csv(up).head(20), use_container_width=True)
    st.caption("Preview only. Mapping to the common schema is added with the ingestion step.")
st.caption("Author handles are hashed and personal data is redacted before analysis.")
