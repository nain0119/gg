import html
import random
import re
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마 + 세로로 긴 아이폰/카톡 스타일 CSS
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

header[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    max-width: 900px;
    padding-top: 3.4rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Gowun Batang', serif !important;
    color: var(--text) !important;
}

p, span, label {
    color: var(--text);
}

[data-testid="stSidebar"] {
    background: #191817;
    border-right: 1px solid var(--line);
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
    padding: 12px 2px !important;
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
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1.15rem;
    color: #ffffff !important;
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

/* 실제 직접 입력 폼 (아이폰 하단 입력바 스타일) */
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

/* 하단 네비 버튼 (다음 날로) */
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

/* 게이지 색상 보정 */
[data-testid="stProgress"] [role="progressbar"],
[data-testid="stProgress"] > div > div > div {
    background-color: #39322e !important;
}

[data-testid="stProgress"] [role="progressbar"] > div,
[data-testid="stProgress"] > div > div > div > div {
    background-color: var(--accent) !important;
}

hr {
    border-color: var(--line) !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 1. 인물 및 일차별 첫 메시지 데이터
# -------------------------------------------------
CONTACTS = {
    "mori": {"name": "모리 오가이", "initial": "모", "color": "#8c3b3b"},
    "dazai": {"name": "다자이 오사무", "initial": "다", "color": "#55687a"},
    "chuuya": {"name": "나카하라 츄야", "initial": "츄", "color": "#b0653b"},
    "akane": {"name": "아카네", "initial": "아", "color": "#6e6a68"},
}

DAILY_INCOMING = {
    1: {
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
                "유스케~",
                "나 지금 다리 위인데 물 색깔 예술이야. 같이 뛰어내릴래?",
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
    },
    2: {
        "mori": {
            "time": "오전 10:05",
            "clock": "10:05",
            "lines": ["어제 보낸 약은 잘 먹었니? 오늘따라 안 보이니 심심하구나."],
        },
        "dazai": {
            "time": "오후 1:40",
            "clock": "13:40",
            "lines": ["심심해~ 나 방금 츄야 모자에 낙서했는데 같이 구경할래?"],
        },
        "chuuya": {
            "time": "오후 3:12",
            "clock": "15:12",
            "lines": ["어이, 어제 복도에서 마주칠 때마다 헛구역질 좀 하지 마. 열받으니까."],
        },
        "akane": {
            "time": "오후 12:15",
            "clock": "12:15",
            "lines": ["식당 안 가"],
        },
    },
    3: {
        "mori": {
            "time": "오후 9:10",
            "clock": "21:10",
            "lines": ["그러고 보니 유스케 군, 요즘 톡 말투가 묘하게 다를 때가 있더구나. 무슨 일 있니?"],
        },
        "dazai": {
            "time": "오후 10:03",
            "clock": "22:03",
            "lines": [
                "유스케",
                "요즘 왜 자꾸 폰으로만 떠들어? 설마 진짜 다른 사람으로 바뀐 건 아니지?",
            ],
        },
        "chuuya": {
            "time": "오후 10:41",
            "clock": "22:41",
            "lines": ["야. 내일 아침엔 기어 나와라. 또 방구석에 짱박히면 문 따고 들어간다."],
        },
        "akane": {
            "time": "오후 11:15",
            "clock": "23:15",
            "lines": ["살아있냐"],
        },
    },
}

ENDINGS = {
    "ending_survive": {
        "title": "생존 엔딩 — 방구석 톡방 마스터",
        "text": (
            "3일 동안 침대 밖으로 한 발짝도 안 나가고 직접 친 답장만으로 포트 마피아를 버텨낸다. "
            "여전히 모리의 약은 퀵으로 배달 오고, 다자이는 다리 위에서 톡을 보내며, 츄야는 문 따고 들어온다고 협박하지만 "
            "일단 정체는 안 들켰다. 살아가는 것만으로도 수고했다."
        ),
    },
    "ending_caught": {
        "title": "배드 엔딩 — 해킹 의심 및 방문 폭파",
        "text": (
            "의심 수치 100 달성. 답장 말투가 너무 수상하다.\n\n"
            "잠시 후 방문 밖에서 구둣발 소리가 들리더니 모리 오가이, 다자이 오사무, 나카하라 츄야가 동시에 들이닥친다. "
            "\"유스케 탈을 쓴 게 누구신가 볼까?\" 그대로 지하 심문실로 직행한다."
        ),
    },
    "ending_hp": {
        "title": "배드 엔딩 — 폰 보다가 기력 소진",
        "text": (
            "체력 0 달성. 원래부터 내구도가 종잇장인 시한부 몸뚱이가 톡만 치다가 방전된다. "
            "손에 쥔 핸드폰이 침대 밑으로 툭 떨어지며 생존기가 종료된다."
        ),
    },
}


# -------------------------------------------------
# 2. 직접 입력 답장 판정 & 대사 생성 엔진
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
            "보스님", "간부님", "선배님", "츄야님", "다자이님", "모리님", "아카네님",
            "다자이씨", "다자이 씨", "츄야씨", "츄야 씨", "아카네씨", "아카네 씨",
            "죄송", "송구", "감사", "말씀", "부탁드",
        ]
    ):
        return True
    return False


def has_any(text: str, words: list[str]) -> bool:
    return any(w in text for w in words)


def judge_and_reply(cid: str, text: str) -> tuple[list[str], int, int]:
    t = text.strip()
    polite = is_polite_korean(t)

    # 1) 모리 오가이 판정
    if cid == "mori":
        if polite:
            return (
                random.choice([
                    ["...어라?", "방금 나한테 존댓말 썼니? 유스케 군 핸드폰 누가 훔쳐 갔니?"],
                    ["보스님이라니. 유스케 군 머리를 어디 세게 박은 건 아니지? ^^"],
                ]),
                -5,
                30,
            )
        if has_any(t, ["사랑", "좋아", "존경", "보고 싶", "보고싶", "최고", "착하"]):
            return (
                ["어머나. 약 기운이 잘못 돌았나 보구나. 확인하러 좀 갈까? ^^"],
                0,
                25,
            )
        if has_any(t, ["면상", "얼굴", "수명", "꺼져", "닥쳐", "죽", "귀찮", "시끄", "미친", "징그", "소름", "변태", "싫", "해부", "안 가", "안 감", "못 가", "못 나"]):
            return (
                random.choice([
                    ["어머 기운 넘치네.", "그럼 오늘 치 약은 퀵으로 보내줄게."],
                    ["하하, 그 험한 입을 보니 진짜 유스케 군이 맞구나. 약 챙겨둘게."],
                ]),
                10,
                -8,
            )
        if has_any(t, ["약", "진료", "아파", "아프", "병", "기침", "피", "살려", "사탕", "주사", "퀵"]):
            return (
                ["그래그래, 제 발로 기어 나올 리가 없지. 오늘 치 약 바로 보낸다."],
                12,
                -4,
            )
        return (
            random.choice([
                ["후후, 심심할 때마다 톡이나 하려무나. 약은 보내둘게."],
                ["하하 여전히 뻔뻔해서 안심했네. 잘 먹고 살아남으렴."],
            ]),
            5,
            -4,
        )

    # 2) 다자이 오사무 판정
    if cid == "dazai":
        if polite:
            return (
                random.choice([
                    ["...잠깐.", "유스케가 지금 나한테 존댓말을 쓴 거야? 너 누구냐."],
                    ["어라라? 유스케가 예의범절을 삼켰나? 수상한데~"],
                ]),
                0,
                30,
            )
        if has_any(t, ["츄야", "꼬맹", "모자", "낙서", "땅꼬마", "키", "중력"]):
            return (
                ["오~ 역시 츄야 놀릴 때만 장단이 척척 맞는다니까."],
                0,
                -8,
            )
        if has_any(t, ["개소리", "미친", "혼자", "싫", "안 해", "안 감", "살", "생존", "이승", "꺼져", "닥쳐", "안 죽", "죽기 싫", "의미", "면상"]):
            return (
                random.choice([
                    ["흥, 여전히 노잼 생존주의자네. 치사해."],
                    ["하긴 네가 나 좋아서 나올 리가 없지. 납득했어~"],
                ]),
                0,
                -8,
            )
        if has_any(t, ["좋아", "가자", "나도", "같이", "힘들", "지쳐", "우울", "죽고", "뛰어", "입수", "자살", "그래"]):
            return (
                ["...잠깐.", "유스케가 방금 나랑 같이 죽자는 뉘앙스를 풍겼어? 너 안에 들어앉은 게 누구지?"],
                0,
                35,
            )
        if has_any(t, ["밥", "먹자", "맛있", "힘내", "걱정", "도와", "사랑", "착하"]):
            return (
                ["유스케가 내 걱정을 다 해주고… 내일 해가 서쪽에서 뜨겠네. 정체가 뭐야?"],
                0,
                28,
            )
        return (
            random.choice([
                ["쳇, 뻔한 반응이네. 재미없어~"],
                ["뭐야 그 시큰둥한 답장은. 역시 살아있는 것밖에 모르는 놈."],
            ]),
            0,
            -4,
        )

    # 3) 나카하라 츄야 판정
    if cid == "chuuya":
        if polite or has_any(t, ["잘생", "멋", "존경", "팬", "사랑", "좋아"]):
            return (
                random.choice([
                    ["...너 오늘 뭘 잘못 처먹었냐? 사과하고 아부 떠는 거 더 기분 나쁘네."],
                    ["미쳤냐?! 소름 돋으니까 헛소리할 거면 차단한다."],
                ]),
                -5,
                28,
            )
        if has_any(t, ["키", "꼬맹", "땅꼬마", "작", "모자", "난쟁", "호빗"]):
            return (
                ["야!! 너 내일 아침에 보자마자 천장으로 처박아버린다!!"],
                -10,
                -8,
            )
        if has_any(t, ["능력", "얼굴", "복붙", "사방", "천", "눈", "똑같", "멀미", "토", "헛구역"]):
            return (
                ["아 젠장 또 네 놈 능력 얘기냐.", "천 뒤집어쓰고 방에 쳐박혀 있어 그럼."],
                -5,
                -8,
            )
        if has_any(t, ["파쇄", "서류", "난", "내", "아니", "뒤집", "마늘", "카레", "냄새", "오지", "꺼져", "닥쳐"]):
            return (
                random.choice([
                    ["하아?! 네 놈 전적이 몇 번인데 끝까지 오리발이야. 여튼 불쾌한 놈."],
                    ["누가 그런 거 들고 간댔냐. 여튼 내일 얼굴 본다."],
                ]),
                0,
                -6,
            )
        return (
            random.choice([
                ["뭐라는 거야, 기분 나쁜 놈. 내일 기어 나오기나 해."],
                ["하아?! 말투 한 번 띠껍네. 내일 보자."],
            ]),
            -2,
            -4,
        )

    # 4) 아카네 판정
    if polite or has_any(t, ["다쳤", "괜찮", "걱정", "연고", "사랑", "고마", "먹을래", "사줄", "엄마"]):
        return (
            random.choice([
                ["...너 누구야. 기시는 그런 말 안 해."],
                ["...기분 나쁘게 왜 갑자기 상냥한 척해?"],
            ]),
            0,
            25,
        )
    if has_any(t, ["안 보", "눈", "앞", "내 탓", "조심", "부딪", "너도"]):
        return (
            ["응. 너도 조심해."],
            0,
            -6,
        )
    if has_any(t, ["식당", "밥", "카레", "마늘", "냄새", "먹", "죽", "안 가"]):
        return (
            ["알겠어. 내 거 뺏어 먹지 마."],
            5,
            -5,
        )
    if has_any(t, ["살", "죽", "어", "응", "그래", "생존"]):
        return (
            ["그래. 내일 또 복도에서 부딪히지 마."],
            5,
            -5,
        )
    return (
        random.choice([
            ["응."],
            ["알겠어."],
        ]),
        0,
        -3,
    )


# -------------------------------------------------
# 3. 상태 관리 및 콜백
# -------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def next_minute_str(clock_str: str, add_min: int) -> str:
    h, m = map(int, clock_str.split(":"))
    total = h * 60 + m + add_min
    return f"{(total // 60) % 24:02d}:{total % 60:02d}"


def push_day_messages(day: int):
    day_data = DAILY_INCOMING[day]
    for cid, data in day_data.items():
        st.session_state.histories[cid].append(
            {"sender": "sys", "text": f"{day}일차"}
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
    st.session_state.phase = "phone"
    st.session_state.phone_view = "list"
    st.session_state.active_chat = None
    st.session_state.day = 1
    st.session_state.hp = 85
    st.session_state.suspicion = 0
    st.session_state.replied_today = []
    st.session_state.msg_counts = {cid: 0 for cid in CONTACTS}
    st.session_state.last_notice = ""
    st.session_state.ending_key = None
    st.session_state.histories = {cid: [] for cid in CONTACTS}
    push_day_messages(1)


def open_chat(cid: str):
    st.session_state.active_chat = cid
    st.session_state.phone_view = "chat"
    st.session_state.last_notice = ""


def go_list():
    st.session_state.phone_view = "list"
    st.session_state.last_notice = ""


def process_free_reply(cid: str, user_text: str):
    day = st.session_state.day
    base_clock = DAILY_INCOMING[day][cid]["clock"]
    offset = st.session_state.msg_counts[cid] * 2 + 2
    t_me = next_minute_str(base_clock, offset)
    t_npc = next_minute_str(base_clock, offset + 1)
    st.session_state.msg_counts[cid] += 1

    st.session_state.histories[cid].append(
        {"sender": "me", "text": user_text, "time": t_me}
    )

    npc_lines, hp_d, sus_d = judge_and_reply(cid, user_text)
    first_today = cid not in st.session_state.replied_today

    if not first_today:
        hp_d = min(0, hp_d)
        sus_d = max(0, sus_d)

    for line in npc_lines:
        st.session_state.histories[cid].append(
            {"sender": "npc", "text": line, "time": t_npc, "label_time": t_npc}
        )

    st.session_state.hp = clamp(st.session_state.hp + hp_d)
    st.session_state.suspicion = clamp(st.session_state.suspicion + sus_d)

    if first_today:
        st.session_state.replied_today.append(cid)

    notes = []
    if hp_d != 0:
        notes.append(f"체력 {'+' if hp_d > 0 else ''}{hp_d}")
    if sus_d != 0:
        notes.append(f"의심 {'+' if sus_d > 0 else ''}{sus_d}")
    st.session_state.last_notice = " / ".join(notes) if notes else ""

    if st.session_state.suspicion >= 100:
        st.session_state.ending_key = "ending_caught"
        st.session_state.phase = "ending"
    elif st.session_state.hp <= 0:
        st.session_state.ending_key = "ending_hp"
        st.session_state.phase = "ending"


def next_day():
    if st.session_state.day >= 3:
        st.session_state.ending_key = "ending_survive"
        st.session_state.phase = "ending"
        return

    st.session_state.day += 1
    st.session_state.hp = clamp(st.session_state.hp - 8)
    st.session_state.replied_today = []
    st.session_state.msg_counts = {cid: 0 for cid in CONTACTS}
    st.session_state.last_notice = ""

    if st.session_state.hp <= 0:
        st.session_state.ending_key = "ending_hp"
        st.session_state.phase = "ending"
        return

    push_day_messages(st.session_state.day)


if "phase" not in st.session_state:
    init_game()


# -------------------------------------------------
# 4. 사이드바 HUD
# -------------------------------------------------
unread_count = len(CONTACTS) - len(st.session_state.replied_today)

with st.sidebar:
    st.subheader("STATUS")
    st.write(f"생존 일차 : {st.session_state.day} / 3일차")
    st.write(f"안 읽은 톡 : {unread_count}건")

    st.divider()

    st.write(f"체력 : {st.session_state.hp} / 100")
    st.progress(st.session_state.hp / 100)

    st.write(f"의심 : {st.session_state.suspicion} / 100")
    st.progress(st.session_state.suspicion / 100)

    st.divider()
    st.caption("PORT MAFIA / YUSUKE PHONE")


# -------------------------------------------------
# 5. 메인 화면
# -------------------------------------------------
st.markdown(
    '<p class="opening-line">눈앞에 핸드폰이 있다......</p>',
    unsafe_allow_html=True,
)

# [A] 처음부터 바로 핸드폰 화면
if st.session_state.phase == "phone":
    with st.container(border=True, key="phone_shell"):
        battery = max(12, st.session_state.hp)
        st.markdown(
            f'<div class="ios-statusbar">'
            f'<span>9:30</span>'
            f'<div class="ios-island"></div>'
            f'<span class="ios-battery">{battery}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # 1) 카톡 스타일 채팅 목록 화면
        if st.session_state.phone_view == "list":
            st.markdown(
                f'<div class="kakao-header">'
                f'<span class="kakao-title">채팅</span>'
                f'<span class="kakao-day">DAY {st.session_state.day}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

            with st.container(key="phone_list"):
                for cid, info in CONTACTS.items():
                    is_unread = cid not in st.session_state.replied_today
                    last_msg = st.session_state.histories[cid][-1]
                    preview = last_msg["text"]
                    if len(preview) > 22:
                        preview = preview[:22] + "..."
                    t_label = last_msg.get("label_time", last_msg.get("time", ""))

                    with st.container(key=f"row_{cid}"):
                        c_av, c_mid, c_meta = st.columns([0.9, 2.7, 1.0])
                        with c_av:
                            st.markdown(
                                f'<div class="k-avatar" style="background:{info["color"]};">'
                                f'{info["initial"]}</div>',
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
                if unread_count == 0:
                    btn_txt = "3일차 마감" if st.session_state.day >= 3 else "다음 날로"
                    st.button(btn_txt, on_click=next_day, key="next_day_btn")
                else:
                    st.button(f"안 읽음 {unread_count}", disabled=True, key="wait_day_btn")

        # 2) 아이폰 문자 스타일 1:1 대화방 (직접 입력)
        elif st.session_state.phone_view == "chat":
            cid = st.session_state.active_chat
            info = CONTACTS[cid]

            with st.container(key="phone_topbar_row"):
                c_back, c_prof, c_sp = st.columns([1, 2.5, 1])
                with c_back:
                    with st.container(key="phone_back"):
                        back_lbl = f"< {unread_count}" if unread_count > 0 else "< 목록"
                        st.button(back_lbl, on_click=go_list, key="back_btn")
                with c_prof:
                    st.markdown(
                        f'<div class="ios-center-profile">'
                        f'<div class="ios-avatar" style="background:{info["color"]};">{info["initial"]}</div>'
                        f'<div class="ios-name">{info["name"]}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with c_sp:
                    st.markdown("<div></div>", unsafe_allow_html=True)

            # 아이폰 말풍선 채팅창
            items = []
            for msg in st.session_state.histories[cid]:
                safe_txt = html.escape(msg["text"])
                t_str = msg.get("time", "")
                if msg["sender"] == "sys":
                    items.append(f'<div class="ios-sys">{safe_txt}</div>')
                elif msg["sender"] == "npc":
                    items.append(
                        f'<div class="ios-npc-row">'
                        f'<div class="ios-bubble-npc">{safe_txt}</div>'
                        f'<span class="ios-msg-time">{t_str}</span>'
                        f'</div>'
                    )
                else:
                    items.append(
                        f'<div class="ios-me-row">'
                        f'<span class="ios-msg-time">{t_str}</span>'
                        f'<div class="ios-bubble-me">{safe_txt}</div>'
                        f'</div>'
                    )

            if st.session_state.last_notice:
                items.append(f'<div class="ios-sys">{st.session_state.last_notice}</div>')

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
                        placeholder="문자 메시지 · SMS",
                        label_visibility="collapsed",
                        key=f"input_{cid}",
                    )
                with c_send:
                    submitted = st.form_submit_button("전송")

                if submitted and user_msg.strip():
                    process_free_reply(cid, user_msg.strip())
                    st.rerun()

        # 하단 홈 바
        st.markdown('<div class="ios-homebar"></div>', unsafe_allow_html=True)

# [B] 엔딩 화면
elif st.session_state.phase == "ending":
    end = ENDINGS[st.session_state.ending_key]
    st.markdown(f"### {end['title']}")
    formatted = end["text"].replace("\n", "<br>")
    st.markdown(f'<div class="story-box">{formatted}</div>', unsafe_allow_html=True)
