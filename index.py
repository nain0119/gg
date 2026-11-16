import base64
import html
import mimetypes
from pathlib import Path
import random
import re
import time
import streamlit as st

# 페이지 설정 (사이드바 숨김)
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 디자인 테마 + 아이폰/카톡 스타일 CSS
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

.stApp {
    background:
        radial-gradient(ellipse at top, #302522 0%, transparent 60%),
        var(--bg);
    color: var(--text);
    font-family: 'Noto Sans KR', sans-serif;
}

header[data-testid="stHeader"],
[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

.block-container {
    max-width: 600px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Gowun Batang', serif !important;
    color: var(--text) !important;
}

p, span, label {
    color: var(--text);
}

/* 기본 버튼 */
div.stButton > button {
    width: 100%;
    background: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.94rem;
    transition: 0.15s;
}

div.stButton > button:hover {
    background: #302522 !important;
    border-color: var(--accent) !important;
    color: #ffffff !important;
}

div.stButton > button p {
    color: var(--text) !important;
}

.opening-line {
    text-align: center;
    color: #c9c0b4 !important;
    font-family: 'Gowun Batang', serif;
    font-size: 1.12rem;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
}

/* 스마트폰 외형 */
.st-key-phone_shell {
    max-width: 460px !important;
    min-height: 760px !important;
    margin: 0 auto !important;
    background: #ffffff !important;
    border: 10px solid #1f1d1c !important;
    border-radius: 44px !important;
    padding: 14px 18px 14px 18px !important;
    box-shadow: 0 26px 65px rgba(0, 0, 0, 0.85), 0 0 0 1px #49413b !important;
}

/* 폰 내부 기본 글자색 검은색 유지 */
.st-key-phone_shell p,
.st-key-phone_shell span,
.st-key-phone_shell label,
.st-key-phone_shell div {
    color: #111111;
}

/* 아이폰 상단 상태바 & 다이나믹 아일랜드 */
.ios-statusbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px 12px 10px 12px;
    font-size: 0.86rem;
    font-weight: 700;
    color: #111111 !important;
}

.ios-island {
    width: 98px;
    height: 24px;
    background: #111111;
    border-radius: 99px;
}

.ios-battery {
    display: inline-block;
    background: #ffd60a;
    color: #111111 !important;
    font-size: 0.74rem;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 6px;
}

/* 목록 상단 헤더 */
.kakao-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 4px 12px 4px;
    border-bottom: 1px solid #ececef;
    margin-bottom: 6px;
}

.kakao-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #111111 !important;
}

.kakao-day {
    font-size: 0.86rem;
    color: #8e8e93 !important;
}

/* 채팅 목록 영역 */
.st-key-phone_list {
    min-height: 560px !important;
}

.st-key-phone_list [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 10px 2px !important;
    border-bottom: 1px solid #f2f2f5;
}

.st-key-phone_list [data-testid="stHorizontalBlock"] > div:nth-child(1) {
    flex: 0 0 56px !important;
    width: 56px !important;
    min-width: 56px !important;
}

.st-key-phone_list [data-testid="stHorizontalBlock"] > div:nth-child(2) {
    flex: 1 1 auto !important;
    min-width: 0 !important;
}

.st-key-phone_list [data-testid="stHorizontalBlock"] > div:nth-child(3) {
    flex: 0 0 68px !important;
    width: 68px !important;
    min-width: 68px !important;
}

.k-avatar {
    width: 52px;
    height: 52px;
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1.15rem;
    color: #ffffff !important;
}

.k-avatar img,
.ios-avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.k-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 6px;
}

.k-time {
    font-size: 0.76rem;
    color: #8e8e93 !important;
    white-space: nowrap;
}

.k-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 22px;
    height: 22px;
    padding: 0 7px;
    border-radius: 99px;
    background: #ff5722;
    color: #ffffff !important;
    font-size: 0.78rem;
    font-weight: 700;
}

.k-badge-empty {
    height: 22px;
}

.st-key-phone_list div.stButton > button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    text-align: left !important;
    padding: 4px 6px !important;
    min-height: 3.1rem !important;
    border-radius: 10px !important;
}

.st-key-phone_list div.stButton > button:hover {
    background: #f4f4f7 !important;
}

.st-key-phone_list div.stButton > button p {
    color: #6e6e73 !important;
    font-size: 0.87rem !important;
    line-height: 1.45 !important;
    margin: 0 !important;
}

.st-key-phone_list div.stButton > button strong {
    color: #111111 !important;
    font-size: 1.02rem !important;
}

/* 채팅방 상단 바 */
.st-key-phone_topbar_row [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 6px !important;
    padding-bottom: 10px;
    border-bottom: 1px solid #ececef;
    margin-bottom: 6px;
}

.st-key-phone_topbar_row [data-testid="stHorizontalBlock"] > div:nth-child(1) {
    flex: 0 0 82px !important;
    width: 82px !important;
    min-width: 82px !important;
}

.st-key-phone_topbar_row [data-testid="stHorizontalBlock"] > div:nth-child(2) {
    flex: 1 1 auto !important;
    min-width: 0 !important;
}

.st-key-phone_topbar_row [data-testid="stHorizontalBlock"] > div:nth-child(3) {
    flex: 0 0 82px !important;
    width: 82px !important;
    min-width: 82px !important;
}

.st-key-phone_back div.stButton > button {
    background: #f2f2f7 !important;
    border: 1px solid #e5e5ea !important;
    border-radius: 99px !important;
    padding: 5px 12px !important;
    min-height: 2.2rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08) !important;
}

.st-key-phone_back div.stButton > button p {
    color: #111111 !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
}

.ios-center-profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
}

.ios-avatar {
    width: 42px;
    height: 42px;
    border-radius: 99px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1rem;
    color: #ffffff !important;
}

.ios-name {
    font-size: 0.9rem;
    font-weight: 700;
    color: #111111 !important;
}

/* 아이폰 SMS 채팅창 */
.ios-chat-scroll {
    height: 555px;
    overflow-y: auto;
    display: flex;
    flex-direction: column-reverse;
    background: #ffffff;
    padding: 12px 6px;
    margin-bottom: 8px;
}

.ios-chat-scroll::-webkit-scrollbar {
    width: 5px;
}

.ios-chat-scroll::-webkit-scrollbar-thumb {
    background: #d1d1d6;
    border-radius: 99px;
}

.ios-chat-inner {
    display: flex;
    flex-direction: column;
}

.ios-sys {
    align-self: center;
    font-size: 0.78rem;
    color: #8e8e93 !important;
    margin: 12px 0 8px 0;
}

.ios-npc-row {
    display: flex;
    justify-content: flex-start;
    align-items: flex-end;
    gap: 6px;
    margin-bottom: 6px;
}

.ios-bubble-npc {
    background: #e9e9eb;
    color: #111111 !important;
    padding: 10px 15px;
    border-radius: 20px 20px 20px 6px;
    max-width: 78%;
    font-size: 0.96rem;
    line-height: 1.52;
    word-break: break-word;
}

.ios-img-bubble {
    max-width: 70%;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #e5e5ea;
}

.ios-img-bubble img {
    width: 100%;
    display: block;
}

.ios-me-row {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    gap: 6px;
    margin-bottom: 6px;
}

.ios-bubble-me {
    background: #34c759;
    color: #ffffff !important;
    padding: 10px 15px;
    border-radius: 20px 20px 6px 20px;
    max-width: 78%;
    font-size: 0.96rem;
    line-height: 1.52;
    word-break: break-word;
}

.ios-msg-time {
    font-size: 0.72rem;
    color: #8e8e93 !important;
    white-space: nowrap;
}

/* 상대 입력 중 말풍선 애니메이션 */
.ios-typing {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: #e9e9eb;
    padding: 12px 15px;
    border-radius: 20px 20px 20px 6px;
    margin-bottom: 6px;
}

.ios-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #8e8e93;
    animation: iosBlink 1.1s infinite ease-in-out;
}

.ios-dot:nth-child(2) { animation-delay: 0.18s; }
.ios-dot:nth-child(3) { animation-delay: 0.36s; }

@keyframes iosBlink {
    0%, 80%, 100% { opacity: 0.3; transform: scale(0.85); }
    40% { opacity: 1; transform: scale(1); }
}

/* 실제 직접 입력 폼 */
.st-key-phone_shell [data-testid="stForm"] {
    border: none !important;
    padding: 4px 0 0 0 !important;
    background: transparent !important;
}

.st-key-phone_shell [data-testid="stForm"] [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 8px !important;
}

.st-key-phone_shell [data-testid="stForm"] [data-testid="stHorizontalBlock"] > div:nth-child(1) {
    flex: 1 1 auto !important;
    min-width: 0 !important;
}

.st-key-phone_shell [data-testid="stForm"] [data-testid="stHorizontalBlock"] > div:nth-child(2) {
    flex: 0 0 70px !important;
    width: 70px !important;
    min-width: 70px !important;
}

.st-key-phone_shell div[data-baseweb="input"] {
    background-color: #ffffff !important;
    border: 1px solid #d1d1d6 !important;
    border-radius: 99px !important;
    padding: 2px 8px !important;
}

.st-key-phone_shell div[data-baseweb="base-input"] {
    background-color: transparent !important;
}

.st-key-phone_shell div[data-baseweb="input"] input {
    background-color: transparent !important;
    color: #111111 !important;
    caret-color: #111111 !important;
    font-size: 0.92rem !important;
    border: none !important;
}

.st-key-phone_shell div[data-baseweb="input"] input::placeholder {
    color: #8e8e93 !important;
    opacity: 1 !important;
}

.st-key-phone_shell [data-testid="InputInstructions"] {
    display: none !important;
}

.st-key-phone_shell [data-testid="stFormSubmitButton"] button {
    background: #34c759 !important;
    border: none !important;
    border-radius: 99px !important;
    min-height: 2.5rem !important;
    padding: 6px 10px !important;
}

.st-key-phone_shell [data-testid="stFormSubmitButton"] button:hover {
    background: #28b34b !important;
}

.st-key-phone_shell [data-testid="stFormSubmitButton"] button p {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
}

/* 하단 네비 버튼 (오늘 마감) */
.st-key-phone_nav {
    margin-top: 10px;
}

.st-key-phone_nav div.stButton > button {
    background: #f2f2f7 !important;
    border: 1px solid #e5e5ea !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
    min-height: 2.7rem !important;
}

.st-key-phone_nav div.stButton > button:hover {
    background: #e5e5ea !important;
}

.st-key-phone_nav div.stButton > button p {
    color: #111111 !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
}

/* 하단 아이폰 홈 바 */
.ios-homebar {
    width: 130px;
    height: 5px;
    background: #111111;
    border-radius: 99px;
    margin: 12px auto 2px auto;
}

/* 엔딩 박스 */
.story-box {
    background: var(--panel);
    border: 1px solid var(--line);
    border-left: 3px solid #6f3434;
    padding: 24px 26px;
    border-radius: 3px;
    line-height: 1.9;
    margin: 14px 0 20px 0;
}

hr {
    border-color: var(--line) !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 0. 이미지 로더 (로컬 images/ 폴더 또는 https:// URL 지원)
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent


def load_image_uri(path_or_url: str) -> str | None:
    if not path_or_url:
        return None
    if path_or_url.startswith(("http://", "https://", "data:")):
        return path_or_url

    file_path = BASE_DIR / path_or_url
    if not file_path.is_file() and file_path.parent.is_dir():
        stem = file_path.stem.lower()
        for cand in file_path.parent.iterdir():
            if (
                cand.is_file()
                and cand.stem.lower() == stem
                and cand.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
            ):
                file_path = cand
                break

    if not file_path.is_file():
        return None

    mime, _ = mimetypes.guess_type(file_path.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(file_path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def render_avatar(info: dict, cls_name: str) -> str:
    uri = load_image_uri(info.get("img", ""))
    if uri:
        return f'<div class="{cls_name}"><img src="{uri}" alt="{info["name"]}"></div>'
    return (
        f'<div class="{cls_name}" style="background:{info["color"]};">'
        f'{info["initial"]}</div>'
    )


# -------------------------------------------------
# 1. 인물 및 하루치 첫 메시지 데이터
# -------------------------------------------------
STATE_VERSION = 12

CONTACTS = {
    "mori":   {"name": "보스",       "initial": "보", "color": "#8c3b3b", "img": "images/mori.jpg"},
    "dazai":  {"name": "자살 희망자", "initial": "자", "color": "#55687a", "img": "images/dazai.jpg"},
    "chuuya": {"name": "망할 자식",   "initial": "망", "color": "#b0653b", "img": "images/chuuya.jpg"},
    "akane":  {"name": "아카네",     "initial": "아", "color": "#6e6a68", "img": "images/akane.png"},
    "jebi":   {"name": "제비",       "initial": "제", "color": "#4f6d63", "img": "images/jebi.png"},
}

TODAY_INCOMING = {
    "mori": {
        "time": "오전 9:02",
        "clock": "09:02",
        "lines": [
            "유스케 군~",
            "진료 시간 10분 지났는데 아직도 이불 속이니? ^^",
        ],
    },
    "dazai": {
        "time": "오전 9:11",
        "clock": "09:11",
        "lines": [
            "기시 군~!",
            "나 돈이 없는데 100엔만 빌려주지 않겠나?",
            "아니, 기왕이면 1000엔!",
        ],
    },
    "chuuya": {
        "time": "오전 9:18",
        "clock": "09:18",
        "lines": [
            "야 기시",
            "내 책상 위 결재 서류 파쇄기에 처넣은 거 너지",
        ],
    },
    "akane": {
        "time": "오전 9:24",
        "clock": "09:24",
        "lines": ["아까 복도에서 들이받고 튄 거 너지"],
    },
    "jebi": {
        "time": "오전 9:31",
        "clock": "09:31",
        "lines": [
            "야 유스케",
            "너 오늘 출근 안 하고 또 침대랑 물아일체냐?",
        ],
    },
}

SURVIVE_ENDING = {
    "title": "오늘 하루 무사 통과",
    "text": (
        "오늘 하루 침대 밖으로 한 발짝도 안 나가고 직접 친 답장만으로 포트 마피아를 버텨낸다. "
        "모리의 약은 퀵으로 배달 오고, 다자이는 여전히 묘한 연락을 남겨 두며, 츄야는 내일 보자고 이를 갈지만 "
        "일단 오늘 하루는 무사히 지나갔다. 살아가는 것만으로도 수고했다."
    ),
}


# -------------------------------------------------
# 2. 직접 입력 답장 대사 생성 엔진
# -------------------------------------------------
def is_polite_korean(text: str) -> bool:
    t = text.strip()
    if re.search(
        r"(요|습니다|ㅂ니다|세요|시죠|십니다|옵니다|드릴게요|할게요|갈게요|볼게요|이에요|예요)[!?.~ㅋㅎㅠㅜ\s]*$",
        t,
    ):
        return True
    if re.search(r"^(네|예)[!?.~\s]*$", t):
        return True
    if any(
        w in t
        for w in [
            "보스님", "간부님", "선배님", "츄야님", "다자이님", "모리님", "아카네님", "제비님",
            "다자이씨", "다자이 씨", "츄야씨", "츄야 씨", "아카네씨", "아카네 씨", "제비씨", "제비 씨",
            "죄송", "송구", "감사", "말씀", "부탁드",
        ]
    ):
        return True
    return False


def has_any(text: str, words: list[str]) -> bool:
    return any(w in text for w in words)


def generate_npc_reply(cid: str, text: str) -> tuple[list[str], bool]:
    """(답장 문구 리스트, 이후 무응답 차단 여부)"""
    t = text.strip()
    polite = is_polite_korean(t)

    # 1) 보스 (모리 오가이)
    if cid == "mori":
        if polite:
            return (
                random.choice([
                    ["...어라?", "방금 나한테 존댓말 썼니? 유스케 군 핸드폰 누가 훔쳐 갔니?"],
                    ["보스님이라니. 유스케 군 머리를 어디 세게 박은 건 아니지? ^^"],
                ]),
                False,
            )
        if has_any(t, ["사랑", "좋아", "존경", "보고 싶", "보고싶", "최고", "착하"]):
            return (["어머나. 약 기운이 잘못 돌았나 보구나. 확인하러 좀 갈까? ^^"], False)
        if has_any(t, ["면상", "얼굴", "수명", "꺼져", "닥쳐", "죽", "귀찮", "시끄", "미친", "징그", "소름", "변태", "싫", "해부", "안 가", "안 감", "못 가", "못 나"]):
            return (
                random.choice([
                    ["어머 기운 넘치네.", "그럼 오늘 치 약은 퀵으로 보내줄게."],
                    ["하하, 그 험한 입을 보니 진짜 유스케 군이 맞구나. 약 챙겨둘게."],
                ]),
                False,
            )
        if has_any(t, ["약", "진료", "아파", "아프", "병", "기침", "피", "살려", "사탕", "주사", "퀵"]):
            return (["그래그래, 제 발로 기어 나올 리가 없지. 오늘 치 약 바로 보낸다."], False)
        return (
            random.choice([
                ["후후, 심심할 때마다 톡이나 하려무나. 약은 보내둘게."],
                ["하하 여전히 뻔뻔해서 안심했네. 잘 먹고 살아남으렴."],
            ]),
            False,
        )

    # 2) 자살 희망자 (다자이 오사무) - 기시 군 호칭 + 혐관러브 톤 + 이상할 시 "자네 누구야?" 후 무응답
    if cid == "dazai":
        rejecting_suicide = has_any(
            t,
            [
                "개소리", "미친", "혼자", "싫", "안 해", "안 감", "안 가",
                "살", "생존", "이승", "꺼져", "닥쳐", "죽지 마", "뛰어내리지 마",
                "들어가지 마", "안 죽", "죽기 싫", "그만", "헛소리",
            ],
        )
        ooc_suicidal = (not rejecting_suicide) and has_any(
            t,
            ["죽고 싶", "같이 죽", "나도 죽", "같이 뛰어", "입수하", "자살하", "살기 싫", "힘들어", "우울해", "지쳤"],
        )
        ooc_sweet = has_any(
            t,
            ["미안", "죄송", "고마워", "고맙", "감사", "힘내", "화이팅", "응원", "사과", "잘못했", "사랑해"],
        )

        # 유스케가 아닌 것 같은 대답 -> "자네 누구야?" 한 마디 후 영구 무응답
        if polite or ooc_suicidal or ooc_sweet:
            return (["자네 누구야?"], True)

        # 상처받은 상태일 때 "어쩌라고" 식의 반응이면 "쳇...... 매정해라" 로 마무리
        if st.session_state.get("dazai_stage") == "hurt":
            if has_any(
                t,
                [
                    "어쩌라고", "어쩌라구", "어쩔", "알빠", "알 바", "알바",
                    "그래서", "상관", "몰라", "그러든가", "말든가", "상처받든가",
                    "네 사정", "흥", "귀찮", "응 아니야",
                ],
            ):
                st.session_state.dazai_stage = "ended"
                return (["쳇...... 매정해라"], True)
            st.session_state.dazai_stage = "normal"

        # "꺼져" / "좆까" 반응
        if has_any(t, ["꺼져", "꺼지", "좆까", "ㅈㄲ", "닥쳐"]):
            has_k = has_any(t, ["꺼져", "꺼지"])
            has_j = has_any(t, ["좆까", "ㅈㄲ"])
            if has_k and has_j:
                echo = "꺼져? 좆까?"
            elif has_j:
                echo = "좆까?"
            elif "닥쳐" in t:
                echo = "닥쳐?"
            else:
                echo = "꺼져?"
            st.session_state.dazai_stage = "hurt"
            return ([f"뭐어? {echo} 말이 너무하잖아! 섬세한 내 마음이 상처받았어!"], False)

        if has_any(t, ["츄야", "꼬맹", "모자", "낙서", "땅꼬마", "키", "중력"]):
            return (
                random.choice([
                    ["지금 나랑 톡하면서 그 땅꼬마 얘기를 꺼낸 거야, 기시 군?"],
                    ["흐음~ 기시 군한테는 나만 있으면 되는 거 아니었나? 섭섭하네."],
                ]),
                False,
            )
        if has_any(t, ["돈", "엔", "100", "1000", "백", "천", "거지", "지갑", "빌려", "안 줘", "못 줘", "일해", "월급", "양심", "싫", "개소리", "미친"]):
            return (
                random.choice([
                    ["으응~ 역시 기시 군은 나한테만 매몰차단 말이지?", "그 쌀쌀맞은 반응이 보고 싶어서 보낸 거긴 하지만."],
                    ["어라, 기시 군도 빈털터리인가? 그럼 1000엔 대신 오늘 저녁에 내 밥이나 얻어먹으러 오시지!"],
                    ["치사하게 굴긴~ 그럼 1000엔 대신 기시 군 얼굴 한 번만 보여주면 퉁쳐 줄게!"],
                    ["에이, 이래 봬도 기시 군은 내 지갑이나 다름없잖아? (아님 말구~)"],
                ]),
                False,
            )
        if has_any(t, ["계좌", "가져가", "던져", "줄게", "보내", "먹어"]):
            return (
                random.choice([
                    ["오오?! 기시 군이 나한테 선뜻 돈을 다 주겠다고? 이거 혹시 사랑의 표현인가~"],
                    ["이야, 이러면 내가 감동해서 기시 군 방 앞으로 당장 달려갈 수밖에 없잖아?"],
                ]),
                False,
            )
        if has_any(t, ["아파", "아프", "약", "침대", "집", "누워", "피곤", "귀찮", "못 나", "안 나", "모리"]):
            return (
                random.choice([
                    ["응? 기시 군 어디 아픈 건가?", "이불 속에만 있지 말고 내 얼굴 좀 보지? 약보다 내가 더 잘 들을 텐데."],
                    ["기시 군이 그렇게 기운이 없다니 신경 쓰이네. 이따 1000엔 어치 병문안이라도 가줄까? (물론 빈손으로!)"],
                ]),
                False,
            )
        if rejecting_suicide:
            return (
                random.choice([
                    ["하하, 역시 기시 군은 내가 죽는 꼴을 못 본단 말이지? 이거 혹시 나 엄청 아끼는 거 아냐?"],
                    ["그럼 기시 군이 직접 와서 안아 주기라도 할 건가? 아니면 그냥 솔직하게 보고 싶다고 말해 보든가~"],
                ]),
                False,
            )
        return (
            random.choice([
                ["그렇게 튕기면서도 결국 내 연락은 못 씹지, 기시 군?"],
                ["역시 기시 군을 괴롭힐 때가 세상에서 제일 재밌다니까~"],
                ["좋아, 이따 밤에 1000엔 받으러 기시 군 숙소 앞으로 갈게. 문 잠그면 창문으로 들어간다?"],
            ]),
            False,
        )

    # 3) 망할 자식 (나카하라 츄야)
    if cid == "chuuya":
        if polite or has_any(t, ["잘생", "멋", "존경", "팬", "사랑", "좋아"]):
            return (
                random.choice([
                    ["...너 오늘 뭘 잘못 처먹었냐? 사과하고 아부 떠는 거 더 기분 나쁘네."],
                    ["미쳤냐?! 소름 돋으니까 헛소리할 거면 차단한다."],
                ]),
                False,
            )
        if has_any(t, ["키", "꼬맹", "땅꼬마", "작", "모자", "난쟁", "호빗"]):
            return (["야!! 너 내일 아침에 보자마자 천장으로 처박아버린다!!"], False)
        if has_any(t, ["능력", "얼굴", "복붙", "사방", "천", "눈", "똑같", "멀미", "토", "헛구역"]):
            return (["아 젠장 또 네 놈 능력 얘기냐.", "천 뒤집어쓰고 방에 쳐박혀 있어 그럼."], False)
        if has_any(t, ["파쇄", "서류", "난", "내", "아니", "뒤집", "마늘", "카레", "냄새", "오지", "꺼져", "닥쳐"]):
            return (
                random.choice([
                    ["하아?! 네 놈 전적이 몇 번인데 끝까지 오리발이야. 여튼 불쾌한 놈."],
                    ["누가 그런 거 들고 간댔냐. 여튼 내일 얼굴 본다."],
                ]),
                False,
            )
        return (
            random.choice([
                ["뭐라는 거야, 기분 나쁜 놈. 내일 기어 나오기나 해."],
                ["하아?! 말투 한 번 띠껍네. 내일 보자."],
            ]),
            False,
        )

    # 4) 아카네
    if cid == "akane":
        if polite or has_any(t, ["다쳤", "괜찮", "걱정", "연고", "사랑", "고마", "먹을래", "사줄", "엄마"]):
            return (
                random.choice([
                    ["...너 누구야. 기시는 그런 말 안 해."],
                    ["...기분 나쁘게 왜 갑자기 상냥한 척해?"],
                ]),
                False,
            )
        if has_any(t, ["안 보", "눈", "앞", "내 탓", "조심", "부딪", "너도"]):
            return (["응. 너도 조심해."], False)
        if has_any(t, ["식당", "밥", "카레", "마늘", "냄새", "먹", "죽", "안 가"]):
            return (["알겠어. 내 거 뺏어 먹지 마."], False)
        if has_any(t, ["살", "죽", "어", "응", "그래", "생존"]):
            return (["그래. 내일 또 복도에서 부딪히지 마."], False)
        return (random.choice([["응."], ["알겠어."]]), False)

    # 5) 제비
    if polite or has_any(t, ["사랑", "좋아", "고마", "미안", "존경", "착하"]):
        return (
            random.choice([
                ["...잠깐. 너 방금 나한테 존댓말 썼냐? 소름 돋게 왜 이래."],
                ["너 진짜 기시 유스케 맞냐? 오늘 뭘 잘못 먹었네."],
            ]),
            False,
        )
    if has_any(t, ["침대", "자", "누워", "아파", "피곤", "귀찮", "안 나", "안 가", "집", "약"]):
        return (["하긴, 네가 제 발로 돌아다닐 놈이 아니지. 약이나 챙겨 먹어."], False)
    if has_any(t, ["천", "얼굴", "츄야", "능력", "복붙", "바꿔", "벗", "똑같"]):
        return (["진짜 볼 때마다 적응 안 되네. 아무튼 눈에 띄지 말고 찌그러져 있어."], False)
    if has_any(t, ["살", "죽", "생존", "다자이", "버텨"]):
        return (["그래, 기어코 살아남는 건 너 하나만큼은 1등이니까."], False)
    return (
        random.choice([
            ["뭐라는 거야. 여튼 안 뒤졌으면 다행이고."],
            ["하아, 여전히 말투 하나는 안 죽었네."],
        ]),
        False,
    )


# -------------------------------------------------
# 3. 상태 관리 및 콜백
# -------------------------------------------------
def next_minute_str(clock_str: str, add_min: int) -> str:
    h, m = map(int, clock_str.split(":"))
    total = h * 60 + m + add_min
    return f"{(total // 60) % 24:02d}:{total % 60:02d}"


def push_today_messages():
    for cid, data in TODAY_INCOMING.items():
        st.session_state.histories[cid].append(
            {"sender": "sys", "text": "오늘"}
        )
        for line in data["lines"]:
            st.session_state.histories[cid].append(
                {
                    "sender": "npc",
                    "text": line,
                    "time": data["clock"],
                    "label_time": data["time"],
                }
            )


def init_game():
    st.session_state.state_version = STATE_VERSION
    st.session_state.phase = "phone"
    st.session_state.phone_view = "list"
    st.session_state.active_chat = None
    st.session_state.read_today = []
    st.session_state.replied_today = []
    st.session_state.ghosted = []
    st.session_state.dazai_stage = "normal"
    st.session_state.msg_counts = {cid: 0 for cid in CONTACTS}
    st.session_state.pending_reply = None
    st.session_state.histories = {cid: [] for cid in CONTACTS}
    push_today_messages()


def resolve_pending_reply():
    pending = st.session_state.get("pending_reply")
    if not pending:
        return

    st.session_state.pending_reply = None
    cid = pending["cid"]
    user_text = pending["text"]
    t_npc = pending["t_npc"]

    npc_lines, should_ghost = generate_npc_reply(cid, user_text)
    for line in npc_lines:
        st.session_state.histories[cid].append(
            {"sender": "npc", "text": line, "time": t_npc, "label_time": t_npc}
        )

    if should_ghost and cid not in st.session_state.ghosted:
        st.session_state.ghosted.append(cid)

    if cid not in st.session_state.read_today:
        st.session_state.read_today.append(cid)
    if cid not in st.session_state.replied_today:
        st.session_state.replied_today.append(cid)


def open_chat(cid: str):
    resolve_pending_reply()
    if cid not in st.session_state.read_today:
        st.session_state.read_today.append(cid)
    st.session_state.active_chat = cid
    st.session_state.phone_view = "chat"


def go_list():
    resolve_pending_reply()
    st.session_state.phone_view = "list"


def queue_free_reply(cid: str, user_text: str):
    base_clock = TODAY_INCOMING[cid]["clock"]
    count = st.session_state.msg_counts.get(cid, 0)
    offset = count * 2 + 2
    t_me = next_minute_str(base_clock, offset)
    t_npc = next_minute_str(base_clock, offset + 1)
    st.session_state.msg_counts[cid] = count + 1

    st.session_state.histories[cid].append(
        {"sender": "me", "text": user_text, "time": t_me}
    )
    if cid not in st.session_state.read_today:
        st.session_state.read_today.append(cid)

    if cid in st.session_state.ghosted:
        return

    st.session_state.pending_reply = {
        "cid": cid,
        "text": user_text,
        "t_npc": t_npc,
    }


def finish_today():
    resolve_pending_reply()
    st.session_state.phase = "ending"


REQUIRED_KEYS = (
    "state_version",
    "phase",
    "phone_view",
    "active_chat",
    "read_today",
    "replied_today",
    "ghosted",
    "dazai_stage",
    "msg_counts",
    "pending_reply",
    "histories",
)

if (
    st.session_state.get("state_version") != STATE_VERSION
    or any(k not in st.session_state for k in REQUIRED_KEYS)
):
    init_game()


# -------------------------------------------------
# 4. 메인 화면 (핸드폰 단독)
# -------------------------------------------------
unread_count = len(CONTACTS) - len(st.session_state.read_today)
unreplied_count = len(CONTACTS) - len(st.session_state.replied_today)

st.markdown(
    '<p class="opening-line">눈앞에 핸드폰이 있다......</p>',
    unsafe_allow_html=True,
)

# [A] 핸드폰 화면
if st.session_state.phase == "phone":
    with st.container(border=True, key="phone_shell"):
        st.markdown(
            '<div class="ios-statusbar">'
            '<span>9:30</span>'
            '<div class="ios-island"></div>'
            '<span class="ios-battery">60</span>'
            '</div>',
            unsafe_allow_html=True,
        )

        # 1) 카톡 스타일 채팅 목록 화면
        if st.session_state.phone_view == "list":
            st.markdown(
                '<div class="kakao-header">'
                '<span class="kakao-title">채팅</span>'
                '<span class="kakao-day">TODAY</span>'
                '</div>',
                unsafe_allow_html=True,
            )

            with st.container(key="phone_list"):
                for cid, info in CONTACTS.items():
                    is_unread = cid not in st.session_state.read_today
                    last_msg = st.session_state.histories[cid][-1]
                    preview = "(사진)" if last_msg["text"].startswith("img:") else last_msg["text"]
                    if len(preview) > 22:
                        preview = preview[:22] + "..."
                    t_label = last_msg.get("label_time", last_msg.get("time", ""))

                    with st.container(key=f"row_{cid}"):
                        c_av, c_mid, c_meta = st.columns([0.9, 2.7, 1.0])
                        with c_av:
                            st.markdown(
                                render_avatar(info, "k-avatar"),
                                unsafe_allow_html=True,
                            )
                        with c_mid:
                            st.button(
                                f"**{info['name']}**\n\n{preview}",
                                on_click=open_chat,
                                args=(cid,),
                                key=f"chat_list_{cid}",
                            )
                        with c_meta:
                            badge_html = (
                                '<div class="k-badge">1</div>'
                                if is_unread
                                else '<div class="k-badge-empty"></div>'
                            )
                            st.markdown(
                                f'<div class="k-meta">'
                                f'<span class="k-time">{t_label}</span>'
                                f'{badge_html}'
                                f'</div>',
                                unsafe_allow_html=True,
                            )

            with st.container(key="phone_nav"):
                if unreplied_count == 0:
                    st.button("오늘 마감", on_click=finish_today, key="finish_day_btn")
                else:
                    replied_n = len(st.session_state.replied_today)
                    st.button(
                        f"답장 대기 중 ({replied_n} / {len(CONTACTS)})",
                        disabled=True,
                        key="wait_day_btn",
                    )

        # 2) 아이폰 문자 스타일 1:1 대화방 (직접 입력)
        elif st.session_state.phone_view == "chat" and st.session_state.active_chat in CONTACTS:
            cid = st.session_state.active_chat
            info = CONTACTS[cid]
            pending = st.session_state.get("pending_reply")
            is_typing_now = bool(pending and pending["cid"] == cid)

            with st.container(key="phone_topbar_row"):
                c_back, c_prof, c_sp = st.columns([1, 2.5, 1])
                with c_back:
                    with st.container(key="phone_back"):
                        back_lbl = f"< {unread_count}" if unread_count > 0 else "< 목록"
                        st.button(back_lbl, on_click=go_list, key="back_btn")
                with c_prof:
                    st.markdown(
                        f'<div class="ios-center-profile">'
                        f'{render_avatar(info, "ios-avatar")}'
                        f'<div class="ios-name">{info["name"]}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with c_sp:
                    st.markdown("<div></div>", unsafe_allow_html=True)

            # 아이폰 말풍선 채팅창
            items = []
            for msg in st.session_state.histories[cid]:
                raw_txt = msg["text"]
                t_str = msg.get("time", "")
                if msg["sender"] == "sys":
                    items.append(f'<div class="ios-sys">{html.escape(raw_txt)}</div>')
                elif msg["sender"] == "npc":
                    if raw_txt.startswith("img:"):
                        uri = load_image_uri(raw_txt[4:].strip())
                        bubble = (
                            f'<div class="ios-img-bubble"><img src="{uri}"></div>'
                            if uri
                            else '<div class="ios-bubble-npc">(사진)</div>'
                        )
                    else:
                        bubble = f'<div class="ios-bubble-npc">{html.escape(raw_txt)}</div>'
                    items.append(
                        f'<div class="ios-npc-row">'
                        f'{bubble}'
                        f'<span class="ios-msg-time">{t_str}</span>'
                        f'</div>'
                    )
                else:
                    items.append(
                        f'<div class="ios-me-row">'
                        f'<span class="ios-msg-time">{t_str}</span>'
                        f'<div class="ios-bubble-me">{html.escape(raw_txt)}</div>'
                        f'</div>'
                    )

            if is_typing_now:
                items.append(
                    '<div class="ios-npc-row">'
                    '<div class="ios-typing">'
                    '<span class="ios-dot"></span>'
                    '<span class="ios-dot"></span>'
                    '<span class="ios-dot"></span>'
                    '</div>'
                    '</div>'
                )

            chat_html = (
                '<div class="ios-chat-scroll"><div class="ios-chat-inner">'
                + "".join(items)
                + '</div></div>'
            )
            st.markdown(chat_html, unsafe_allow_html=True)

            # 하단 직접 입력 폼
            with st.form(key=f"chat_form_{cid}", clear_on_submit=True):
                c_inp, c_send = st.columns([4.2, 1.1])
                with c_inp:
                    user_msg = st.text_input(
                        "메시지",
                        placeholder="입력 중..." if is_typing_now else "문자 메시지 · SMS",
                        label_visibility="collapsed",
                        disabled=is_typing_now,
                        key=f"input_{cid}",
                    )
                with c_send:
                    submitted = st.form_submit_button("전송", disabled=is_typing_now)

            if submitted and user_msg.strip() and not is_typing_now:
                queue_free_reply(cid, user_msg.strip())
                st.rerun()

        # 하단 홈 바
        st.markdown('<div class="ios-homebar"></div>', unsafe_allow_html=True)

    # 2초 텀 후 상대방 답장 출력
    pending = st.session_state.get("pending_reply")
    if (
        st.session_state.phase == "phone"
        and st.session_state.phone_view == "chat"
        and pending
        and pending["cid"] == st.session_state.active_chat
    ):
        time.sleep(2)
        resolve_pending_reply()
        st.rerun()

# [B] 엔딩 화면
elif st.session_state.phase == "ending":
    st.markdown(f"### {SURVIVE_ENDING['title']}")
    formatted = SURVIVE_ENDING["text"].replace("\n", "<br>")
    st.markdown(f'<div class="story-box">{formatted}</div>', unsafe_allow_html=True)
