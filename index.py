
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&display=swap');

:root {
    --bg: #171615;
    --panel: #211f1d;
    --text: #e7e1d8;
    --muted: #9b9389;
    --line: #49413b;
    --accent: #a34b4b;
}

/* 전체 배경 */
.stApp {
    background:
        radial-gradient(ellipse at top, #302522 0%, transparent 60%),
        var(--bg);
    color: var(--text);
    font-family: 'Noto Sans KR', sans-serif;
}

/* 화면 여백 */
.block-container {
    max-width: 950px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* 제목 */
h1, h2, h3 {
    font-family: 'Gowun Batang', serif !important;
    color: var(--text) !important;
}

/* 본문 */
p, span, label {
    color: var(--text);
}

/* 사이드바 */
[data-testid="stSidebar"] {
    background: #191817;
    border-right: 1px solid var(--line);
}

/* 이야기 상자 */
.story-box {
    background: var(--panel);
    border: 1px solid var(--line);
    border-left: 3px solid #6f3434;
    padding: 25px;
    border-radius: 3px;
    line-height: 2;
    margin: 20px 0;
}

/* 버튼 */
div.stButton > button {
    width: 100%;
    min-height: 3rem;
    background: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 3px;
    padding: 12px 18px;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #302522 !important;
    border-color: var(--accent) !important;
    color: white !important;
}

/* 체력 게이지 */
[data-testid="stProgress"] > div > div > div > div {
    background: var(--accent) !important;
}

[data-testid="stProgress"] > div > div > div {
    background: #39322e !important;
}

/* 구분선 */
hr {
    border-color: var(--line) !important;
}

/* 모바일 */
@media (max-width: 700px) {
    .block-container {
        padding: 2rem 1rem;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 메인 화면 기본 틀
# -------------------------------------------------

st.markdown(
    '<p style="color:#b56c65; letter-spacing:4px; font-size:12px;">'
    'PORT MAFIA  /  PERSONAL RECORD</p>',
    unsafe_allow_html=True
)

st.title("기시 유스케 생존 기록")

st.markdown(
    '<p style="color:#9b9389;">요코하마 · 생존 기록</p>',
    unsafe_allow_html=True
)

st.divider()

# 사이드바
with st.sidebar:
    st.subheader("STATUS")
    st.write("체력 : 100 / 100")
    st.progress(1.0)

    st.divider()

    st.caption("PORT MAFIA")
    st.caption("SURVIVAL RECORD")


# 콘텐츠 영역
st.markdown("### 기록")

st.markdown("""
<div class="story-box">
    이곳에 이야기 내용을 작성하세요.
</div>
""", unsafe_allow_html=True)

st.button("다음으로")
