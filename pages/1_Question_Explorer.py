import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from src.ui import setup, card

d = setup("Question Explorer")
names = ["Why start", "Behaviour change", "Stop reasons", "Checking habits", "In-app confusion",
         "Outside the app", "Continue vs drop-off", "Segments", "Unmet needs"]
tabs = st.tabs(names)
for i, t in enumerate(tabs):
    with t:
        if names[i] != "Stop reasons":
            st.info("This view is filled in after the extraction step has run.")
            continue
        st.markdown("**What leads investors to pause, reduce or stop a SIP?**")
        st.caption(f"n = {d['reasons_n']}  |  field coverage {d['reasons_coverage']:.0%}")
        r = pd.DataFrame(d["reasons"])
        fig = go.Figure(go.Bar(x=r["share"], y=r["label"], orientation="h", marker_color="#387ED1",
                               error_x=dict(type="data", symmetric=False,
                                            array=r["hi"] - r["share"], arrayminus=r["share"] - r["lo"])))
        fig.update_layout(yaxis=dict(autorange="reversed"), xaxis=dict(tickformat=".0%"), height=360,
                          margin=dict(l=0, r=0, t=10, b=0))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("**What people said**")
        for q in d["quotes"]:
            card(f"<span class='quote'>{q['text']}</span><br><span class='muted'>{q['source']} | {q['stage']}</span>")
