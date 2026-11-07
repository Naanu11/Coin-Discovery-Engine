import json
from pathlib import Path
import streamlit as st

DATA = Path(__file__).resolve().parent.parent / "data"
BANNER = "Public-conversation analysis for product discovery. Not investment advice."
CSS = """
<style>
.block-container{padding-top:2rem;padding-bottom:4rem;max-width:1200px}
.pill{display:inline-block;padding:2px 10px;border-radius:999px;background:#E8F1FB;color:#387ED1;font-size:12px;margin-left:8px}
.card{background:#fff;border:1px solid #E3E8EF;border-radius:8px;padding:14px 16px;margin-bottom:10px}
.muted{color:#66788A;font-size:13px}
.quote{font-style:italic}
.foot{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #E3E8EF;
 text-align:center;font-size:12px;color:#66788A;padding:6px;z-index:99}
</style>
"""

@st.cache_data
def load(name: str):
    """Return (data, is_sample). Real files in data/extracted override the sample."""
    real = DATA / "extracted" / name
    if real.exists():
        return json.loads(real.read_text()), False
    return json.loads((DATA / "sample" / name).read_text()), True

def setup(title: str, file: str = "sample.json"):
    st.set_page_config(page_title=f"{title} | Coin SIP Discovery", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)
    data, sample = load(file)
    pill = '<span class="pill">Sample data</span>' if sample else ""
    st.markdown(f"## {title}{pill}", unsafe_allow_html=True)
    st.markdown(f'<div class="foot">{BANNER}</div>', unsafe_allow_html=True)
    return data

def card(html: str):
    st.markdown(f'<div class="card">{html}</div>', unsafe_allow_html=True)
