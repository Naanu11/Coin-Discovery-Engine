import pandas as pd
import plotly.express as px
import streamlit as st
from src.ui import setup, card

d = setup("Overview")
m = d["meta"]
c = st.columns(4)
c[0].metric("Documents analysed", f"{m['documents']:,}")
c[1].metric("Sources", m["sources"])
c[2].metric("Date range", f"{m['date_min']} to {m['date_max']}")
c[3].metric("Quote grounding rate", f"{m['grounding_rate']:.0%}")

left, right = st.columns(2)
with left:
    st.subheader("Data funnel")
    f = pd.DataFrame(d["funnel"], columns=["Stage", "Documents"])
    fig = px.bar(f, x="Documents", y="Stage", orientation="h", text="Documents", color_discrete_sequence=["#387ED1"])
    fig.update_layout(yaxis=dict(autorange="reversed"), height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Source mix")
    s = pd.DataFrame(list(d["source_mix"].items()), columns=["Source", "Documents"])
    fig = px.bar(s, x="Documents", y="Source", orientation="h", color_discrete_sequence=["#12A594"])
    fig.update_layout(yaxis=dict(autorange="reversed"), height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Headline findings")
for x in d["findings"]:
    card(f"{x['text']}<br><span class='muted'>n = {x['n']} &nbsp;|&nbsp; {x['ci']} &nbsp;|&nbsp; Confidence: {x['confidence']}</span>")

with st.expander("Read this before using the numbers", expanded=True):
    st.markdown("- Reviews skew negative.\n- Reddit skews to experienced investors.\n- YouTube skews to influencer audiences.\n- Silent drop-offs rarely post.\n\n"
                "Prevalence here describes the conversation sample, not all investors.")
