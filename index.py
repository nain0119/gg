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
        --bg: #171615;
        --panel: #211f1d;
        --panel-soft: #1c1b19;
        --text: #e7e1d8;
        --muted: #9b9389;
        --line: #49413b;
        --accent: #a34b4b;
        --accent-soft: #6f3434;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, #292321 0%, transparent 55%),
            var(--bg);
        color: var(--text);
        font-family: 'Noto Sans KR', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 980px;
        padding-top: 3.2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: var(--text) !important;
        font-family: 'Gowun Batang', serif !important;
        letter-spacing: -0.04em;
    }

    h1 {
        font-size: 2.35rem !important;
        font-weight: 700 !important;
        margin-bottom: .35rem !important;
    }

    h2, h3 {
        font-weight: 700 !important;
    }

    p, label, span, li {
        color: var(--text);
    }

    [data-testid="stSidebar"] {
        background: #191817;
        border-right: 1px solid #39322e;
    }

    [data-testid="stSidebar"] > div {
        padding-top: 2.5rem;
    }

    [data-testid="stSidebar"] h3 {
        font-family: 'Noto Sans KR', sans-serif !important;
        font-size: .92rem !important;
        font-weight: 500 !important;
        color: var(--muted) !important;
        letter-spacing: .08em;
    }

    [data-testid="stProgress"] {
        margin-top: .7rem;
    }

    [data-testid="stProgress"] > div > div > div > div {
        background: var(--accent) !important;
    }

    [data-testid="stProgress"] > div > div > div {
        background: #39322e !important;
    }

    .eyebrow {
