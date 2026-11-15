import random
import re
import streamlit as st

# ---------------------------------------------------------
# 1. 페이지 설정 및 흑백(검은 바탕 / 흰 글씨) 테마 CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="기시 유스케 생존기",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');
    :root {
        --bg: #171615; --text: #e7e1d8; --muted: #9b9389;
        --line: #49413b; --accent: #a34b4b; --accent-soft: #6f3434;
    }
    .stApp {
        background: radial-gradient(ellipse at 50% 0%, #292321 0%, transparent 55%), var(--bg);
        color: var(--text); font-family: 'Noto Sans KR', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 980px; padding-top: 3.2rem; padding-bottom: 4rem; }
    h1, h2, h3 {
        color: var(--text) !important; font-family: 'Gowun Batang', serif !important;
        letter-spacing: -0.04em;
    }
    h1 { font-size: 2.35rem !important; font-weight: 700 !important; margin-bottom: .35rem !important; }
    p, label, span, li { color: var(--text); }
    [data-testid="stSidebar"] { background: #191817; border-right: 1px solid #39322e; }
    [data-testid="stSidebar"] > div { padding-top: 2.5rem; }
    [data-testid="stSidebar"] h3 {
        font-family: 'Noto Sans KR', sans-serif !important; font-size: .92rem !important;
        font-weight: 500 !important; color: var(--muted) !important; letter-spacing: .08em;
    }
    [data-testid="stProgress"] { margin-top: .7rem; }
    [data-testid="stProgress"] > div > div > div > div { background: var(--accent) !important; }
    [data-testid="stProgress"] > div > div > div { background: #39322e !important; }
    .eyebrow {
        color: #b56c65; font-size: .72rem; font-weight: 600;
        letter-spacing: .22em; margin-bottom: .8rem;
    }
    .subnote { color: var(--muted); font-size: .84rem; letter-spacing: .04em; margin-bottom: 1.8rem; }
    .story-box {
        background: linear-gradient(135deg, rgba(42,37,34,.96), rgba(30,28,26,.98));
        border: 1px solid var(--line); border-left: 3px solid var(--accent-soft);
        padding: 26px 30px; border-radius: 3px; line-height: 2; font-size: 1rem;
        color: var(--text); margin: 1.2rem 0 1.5rem; box-shadow: 0 12px 32px rgba(0,0,0,.12);
    }
    .story-box strong { color: #d9aaa0; font-weight: 700; }
    .badge {
        display: inline-block; padding: 5px 11px; border-radius: 2px; font-size: .78rem;
        font-weight: 600; letter-spacing: .04em; background: #302522; color: #d9aaa0;
        border: 1px solid #70423e; margin-top: 8px;
    }
    div.stButton > button {
        width: 100%; min-height: 3.1rem; text-align: left; white-space: normal;
        background: #211f1d !important; color: #ded7ce !important;
        border: 1px solid #49413b !important; padding: 13px 17px; border-radius: 3px;
        font-size: .94rem; line-height: 1.6;
        transition: background .18s ease, border-color .18s ease, transform .18s ease;
    }
    div.stButton > button:hover {
        background: #302522 !important; border-color: #98605a !important;
        color: #fff4ec !important; transform: translateY(-1px);
    }
    div.stButton > button:focus:not(:active) {
        border-color: #a34b4b !important; box-shadow: 0 0 0 1px #a34b4b !important;
    }
    hr { border-color: #49413b !important; }
    @media (max-width: 700px) {
        .block-container { padding: 2rem 1.1rem 3rem; }
        h1 { font-size: 1.8rem !important; }
        .story-box { padding: 20px 19px; font-size: .94rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SLOTS = ["오전", "오후", "밤"]


def to_html(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text.replace("\n", "<br>")


# ---------------------------------------------------------
# 2. 게임 이벤트 데이터
# ---------------------------------------------------------
def get_fixed_events():
    return {
