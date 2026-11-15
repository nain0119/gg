import html
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마 + 확대된 아이폰/카톡 스타일 CSS
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
    padding-top: 3.6rem;
    padding-bottom: 4rem;
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

/* 기본 버튼 (사이드바, 엔딩 화면용) */
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
    margin-bottom: 18px;
}

/* 스마트폰 외형 (크기 확대: 470px) */
.st-key-phone_shell {
    max-width: 470px !important;
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
    padding: 8px 4px 12px 4px;
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

/* 채팅 목록 행 레이아웃 유지 */
.st-key-phone_list [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 8px 2px !important;
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

/* 카톡 스퀘어클 아바타 */
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

/* 카톡 우측 시간 + 주황색 뱃지 */
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

/* 카톡 목록 버튼 투명화 */
.st-key-phone_list div.stButton > button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    text-align: left !important;
    padding: 4px 6px !important;
    min-height: 3rem !important;
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

/* 아이폰 SMS 채팅창 (크기 확대: 460px) */
.ios-chat-scroll {
    height: 460px;
    overflow-y: auto;
    display: flex;
    flex-direction: column-reverse;
    background: #ffffff;
    padding: 12px 6px;
    margin-bottom: 10px;
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

/* 하단 문자 메시지 SMS 입력창 */
.ios-input-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
}

.ios-plus {
    width: 34px;
    height: 34px;
    border-radius: 99px;
    background: #f2f2f7;
    color: #3a3a3c !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    font-weight: 500;
    flex-shrink: 0;
}

.ios-pill-input {
    flex: 1;
    border: 1px solid #d1d1d6;
    border-radius: 99px;
    padding: 8px 16px;
    font-size: 0.88rem;
    color: #8e8e93 !important;
    background: #ffffff;
}

/* 답장 선택 버튼 */
.st-key-phone_replies div.stButton > button {
    background: #f2f2f7 !important;
    border: 1px solid #e5e5ea !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
    text-align: left !important;
    min-height: 2.6rem !important;
}

.st-key-phone_replies div.stButton > button:hover {
    background: #e5e5ea !important;
    border-color: #c7c7cc !important;
}

.st-key-phone_replies div.stButton > button p {
    color: #111111 !important;
    font-size: 0.91rem !important;
    line-height: 1.45 !important;
}

/* 하단 네비 버튼 */
.st-key-phone_nav [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 10px !important;
    margin-top: 10px;
}

.st-key-phone_nav div.stButton > button {
    background: #f2f2f7 !important;
    border: 1px solid #e5e5ea !important;
    border-radius: 12px !important;
    padding: 9px 12px !important;
    min-height: 2.6rem !important;
}

.st-key-phone_nav div.stButton > button:hover {
    background: #e5e5ea !important;
}

.st-key-phone_nav div.stButton > button p {
    color: #111111 !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
}

/* 메모장 화면 (크기 확대: 460px) */
.memo-scroll {
    height: 460px;
    overflow-y: auto;
    background: #fffdf5;
    border: 1px solid #ece6d2;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 10px;
}

.memo-item {
    padding: 12px 10px;
    border-bottom: 1px dashed #e3dcc5;
    font-size: 0.94rem;
    line-height: 1.65;
    color: #2c2820 !important;
}

.memo-item:last-child {
    border-bottom: none;
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
# 1. 인물 및 시나리오 데이터 (모리 / 다자이 / 츄야 / 아카네)
# -------------------------------------------------
CONTACTS = {
    "mori": {"name": "모리 오가이", "initial": "모", "color": "#8c3b3b"},
    "dazai": {"name": "다자이 오사무", "initial": "다", "color": "#55687a"},
    "chuuya": {"name": "나카하라 츄야", "initial": "츄", "color": "#b0653b"},
    "akane": {"name": "아카네", "initial": "아", "color": "#6e6a68"},
}

CHAT_SCRIPT = {
    1: {
        "mori": {
            "time": "오전 9:02",
            "clock": "09:02",
            "incoming": [
                "유스케 군~",
                "진료 시간 10분 지났는데 아직도 이불 속이니? ^^",
            ],
            "choices": [
                {
                    "reply": "아 안 죽었어 모리 씨. 귀찮게 톡하지 마",
                    "npc_after": ["어머 기운 넘치네.", "그럼 오늘 치 약은 퀵으로 보내줄게."],
                    "hp": 10,
                    "suspicion": -5,
                },
                {
                    "reply": "죄송합니다 보스님!! 지금 바로 뛰어갈게요!!",
                    "npc_after": ["...보스님?", "유스케 군 핸드폰 누가 훔쳐 갔니?"],
                    "hp": -5,
                    "suspicion": 35,
                },
                {
                    "reply": "몸 아파서 못 나감. 알아서 갖다 줘",
                    "npc_after": ["하긴 네가 제 발로 올 리가 없지. 사람 보낼게."],
                    "hp": 5,
                    "suspicion": 0,
                },
            ],
        },
        "dazai": {
            "time": "오전 9:11",
            "clock": "09:11",
            "incoming": [
                "유스케~",
                "나 지금 다리 위인데 물 색깔 예술이야. 같이 뛰어내릴래?",
            ],
            "choices": [
                {
                    "reply": "개소리 마. 역겹고 의미 없어도 살아있는 게 백 배 낫거든",
                    "npc_after": ["흥, 여전히 노잼 생존주의자네. 치사해."],
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "무슨 일 있어? 나랑 맛있는 거라도 먹자",
                    "npc_after": ["...잠깐.", "유스케가 방금 나한테 밥 사준다고 했어? 너 누구냐."],
                    "hp": 0,
                    "suspicion": 35,
                },
            ],
        },
        "chuuya": {
            "time": "오전 9:18",
            "clock": "09:18",
            "incoming": [
                "야 기시",
                "내 책상 위 결재 서류 파쇄기에 처넣은 거 너지",
            ],
            "choices": [
                {
                    "reply": "난 내 책상 것만 갈았거든? 나한테 뒤집어씌우지 마",
                    "npc_after": ["하아?! 네 놈 전적이 몇 번인데 헛소리야.", "여튼 불쾌한 놈."],
                    "hp": -5,
                    "suspicion": -5,
                },
                {
                    "reply": "정말 죄송합니다! 제가 지금 당장 다시 복구하겠습니다!",
                    "npc_after": ["...너 오늘 뭘 잘못 처먹었냐? 사과하는 거 더 기분 나쁘네."],
                    "hp": 0,
                    "suspicion": 25,
                },
            ],
        },
        "akane": {
            "time": "오전 9:24",
            "clock": "09:24",
            "incoming": ["아까 복도에서 들이받고 튄 거 너지"],
            "choices": [
                {
                    "reply": "너도 나 안 보이면서 내 탓하지 마",
                    "npc_after": ["응. 조심해."],
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "앗 아카네! 많이 다쳤어? 내가 연고 사다 줄까?",
                    "npc_after": ["...너 누구야. 기시는 그런 말 안 해."],
                    "hp": 0,
                    "suspicion": 25,
                },
            ],
        },
    },
    2: {
        "mori": {
            "time": "오전 10:05",
            "clock": "10:05",
            "incoming": ["어제 보낸 약은 잘 먹었니? 오늘따라 안 보이니 심심하구나."],
            "choices": [
                {
                    "reply": "약 맛없어. 사탕이나 끼워서 보내",
                    "npc_after": ["하하 여전히 뻔뻔해서 안심했네. 내일 치도 챙겨둘게."],
                    "hp": 10,
                    "suspicion": -5,
                },
                {
                    "reply": "감사합니다! 덕분에 컨디션이 엄청 좋아졌어요!",
                    "npc_after": ["느낌표까지 붙이고… 유스케 군 요즘 머리를 어디 박았니?"],
                    "hp": 5,
                    "suspicion": 30,
                },
            ],
        },
        "dazai": {
            "time": "오후 1:40",
            "clock": "13:40",
            "incoming": ["심심해~ 나 방금 츄야 모자에 낙서했는데 같이 구경할래?"],
            "choices": [
                {
                    "reply": "아 그 꼬맹이? 모자 잃어버리면 울 텐데 잘했네",
                    "npc_after": ["오~ 역시 츄야 놀릴 때만 손발이 척척 맞는다니까."],
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "남의 물건에 낙서하면 안 되지. 빨리 지우고 사과해.",
                    "npc_after": ["어라라? 유스케가 도덕 교과서를 삼켰나. 수상하네."],
                    "hp": 0,
                    "suspicion": 30,
                },
            ],
        },
        "chuuya": {
            "time": "오후 3:12",
            "clock": "15:12",
            "incoming": ["어이, 어제 복도에서 마주칠 때마다 헛구역질 좀 하지 마. 열받으니까."],
            "choices": [
                {
                    "reply": "사방에 네 얼굴이 복붙돼서 뜨는데 속이 안 뒤집히겠냐",
                    "npc_after": ["아 젠장 또 네 놈 능력 얘기냐.", "천 뒤집어쓰고 방에 쳐박혀 있어 그럼."],
                    "hp": -5,
                    "suspicion": -5,
                },
                {
                    "reply": "아뇨! 저 츄야 씨 엄청 좋아하고 존경해요!",
                    "npc_after": ["미쳤냐?! 소름 돋으니까 헛소리할 거면 차단한다."],
                    "hp": -5,
                    "suspicion": 30,
                },
            ],
        },
        "akane": {
            "time": "오후 12:15",
            "clock": "12:15",
            "incoming": ["식당 안 가"],
            "choices": [
                {
                    "reply": "오늘 마늘 카레 냄새 나서 안 감",
                    "npc_after": ["알겠어. 내 거 뺏어 먹지 마."],
                    "hp": 5,
                    "suspicion": -5,
                },
                {
                    "reply": "응! 같이 가자! 내가 맛있는 거 사줄게!",
                    "npc_after": ["...돈도 없는 거지가 이상한 소리 하네."],
                    "hp": 0,
                    "suspicion": 20,
                },
            ],
        },
    },
    3: {
        "mori": {
            "time": "오후 9:10",
            "clock": "21:10",
            "incoming": ["그러고 보니 유스케 군, 요즘 톡 말투가 묘하게 다를 때가 있더구나. 무슨 일 있니?"],
            "choices": [
                {
                    "reply": "모리 씨 면상 안 봐서 기분이 왔다 갔다 하나 보지",
                    "npc_after": ["후후, 그 험한 입을 보니 진짜 유스케 군이 맞나 보네. 잘 지내렴."],
                    "hp": 10,
                    "suspicion": -10,
                },
                {
                    "reply": "아뇨! 저 완전 멀쩡해요! 걱정 감사드립니다!",
                    "npc_after": ["그래.", "그럼 확인하러 조금 이따 방으로 직접 들를게 ^^"],
                    "hp": -10,
                    "suspicion": 40,
                },
            ],
        },
        "dazai": {
            "time": "오후 10:03",
            "clock": "22:03",
            "incoming": [
                "유스케",
                "요즘 왜 자꾸 폰으로만 떠들어? 설마 진짜 다른 사람으로 바뀐 건 아니지?",
            ],
            "choices": [
                {
                    "reply": "응 네 면상 보기 싫어서 안 나감. 수고",
                    "npc_after": ["하긴 네가 나 보고 싶어서 나올 리가 없지. 납득했어~"],
                    "hp": 0,
                    "suspicion": -10,
                },
                {
                    "reply": "무슨 소리야! 나 진짜 기시 유스케 맞아!",
                    "npc_after": ["진짜 유스케는 그런 구차한 변명 안 해.", "재미있어지네?"],
                    "hp": 0,
                    "suspicion": 35,
                },
            ],
        },
        "chuuya": {
            "time": "오후 10:41",
            "clock": "22:41",
            "incoming": ["야. 내일 아침엔 기어 나와라. 또 방구석에 짱박히면 문 따고 들어간다."],
            "choices": [
                {
                    "reply": "오든가 말든가. 대신 마늘 냄새 풍기면서 오지 마",
                    "npc_after": ["누가 그런 거 들고 간댔냐. 여튼 내일 얼굴 본다."],
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "네! 내일 일찍 출근해서 인사드리겠습니다!",
                    "npc_after": ["...기시 너 진짜 누구야. 내일 보자마자 확인한다."],
                    "hp": -5,
                    "suspicion": 35,
                },
            ],
        },
        "akane": {
            "time": "오후 11:15",
            "clock": "23:15",
            "incoming": ["살아있냐"],
            "choices": [
                {
                    "reply": "어. 죽는 것보다 사는 게 낫잖아",
                    "npc_after": ["그래. 내일 또 복도에서 부딪히지 마."],
                    "hp": 5,
                    "suspicion": -5,
                },
                {
                    "reply": "응응! 걱정해 줘서 너무 고마워 아카네!",
                    "npc_after": ["...소름 돋아. 차단함."],
                    "hp": 0,
                    "suspicion": 25,
                },
            ],
        },
    },
}

MEMO_NOTES = [
    "1. 보스(모리 씨) 포함해서 아무한테나 다 반말 깐다. 존댓말 쓰면 그날로 지하실 간다.",
    "2. 다자이한테 '힘들다', '죽고 싶다' 비슷한 소리 금지. 츄야 뒷담화는 잘 받아준다.",
    "3. 츄야랑 말 섞을 때 쫄지 마라. 사방에 츄야 얼굴 떠서 짜증 난다고 하면 납득한다.",
    "4. 아카네는 나한테 원래 별 관심 없다. 갑자기 걱정해 주면 의심받는다.",
    "5. 서류는 파쇄기 밥이다. 마늘이나 향 강한 음식 먹으면 위장 터진다.",
]

ENDINGS = {
    "ending_survive": {
        "title": "생존 엔딩 — 방구석 톡방 마스터",
        "text": (
            "3일 동안 침대 밖으로 한 발짝도 안 나가고 스마트폰 답장만으로 포트 마피아를 버텨낸다. "
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
# 2. 상태 관리 및 콜백
# -------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def next_minute_str(clock_str: str, add_min: int) -> str:
    h, m = map(int, clock_str.split(":"))
    total = h * 60 + m + add_min
    return f"{(total // 60) % 24:02d}:{total % 60:02d}"


def push_day_messages(day: int):
    day_data = CHAT_SCRIPT[day]
    for cid, data in day_data.items():
        st.session_state.histories[cid].append(
            {"sender": "sys", "text": f"{day}일차"}
        )
        for line in data["incoming"]:
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
    st.session_state.last_notice = ""
    st.session_state.ending_key = None
    st.session_state.histories = {cid: [] for cid in CONTACTS}
    push_day_messages(1)


def open_chat(cid: str):
    st.session_state.active_chat = cid
    st.session_state.phone_view = "chat"
    st.session_state.last_notice = ""


def go_view(view_name: str):
    st.session_state.phone_view = view_name
    st.session_state.last_notice = ""


def send_reply(cid: str, choice_idx: int):
    day = st.session_state.day
    data = CHAT_SCRIPT[day][cid]
    ch = data["choices"][choice_idx]
    t_me = next_minute_str(data["clock"], 2)
    t_npc = next_minute_str(data["clock"], 3)

    st.session_state.histories[cid].append(
        {"sender": "me", "text": ch["reply"], "time": t_me}
    )
    for line in ch["npc_after"]:
        st.session_state.histories[cid].append(
            {"sender": "npc", "text": line, "time": t_npc, "label_time": t_npc}
        )

    st.session_state.hp = clamp(st.session_state.hp + ch.get("hp", 0))
    st.session_state.suspicion = clamp(
        st.session_state.suspicion + ch.get("suspicion", 0)
    )

    if cid not in st.session_state.replied_today:
        st.session_state.replied_today.append(cid)

    hp_d = ch.get("hp", 0)
    sus_d = ch.get("suspicion", 0)
    notes = []
    if hp_d != 0:
        notes.append(f"체력 {'+' if hp_d > 0 else ''}{hp_d}")
    if sus_d != 0:
        notes.append(f"의심 {'+' if sus_d > 0 else ''}{sus_d}")
    st.session_state.last_notice = " / ".join(notes) if notes else "변화 없음"

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
    st.session_state.last_notice = ""

    if st.session_state.hp <= 0:
        st.session_state.ending_key = "ending_hp"
        st.session_state.phase = "ending"
        return

    push_day_messages(st.session_state.day)


if "phase" not in st.session_state:
    init_game()


# -------------------------------------------------
# 3. 사이드바 HUD
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
    st.button("처음부터 다시", on_click=init_game, key="reset_btn")


# -------------------------------------------------
# 4. 메인 화면
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
                col1, col2 = st.columns(2)
                with col1:
                    st.button("메모장", on_click=go_view, args=("memo",), key="open_memo")
                with col2:
                    if unread_count == 0:
                        btn_txt = "3일차 마감" if st.session_state.day >= 3 else "다음 날로"
                        st.button(btn_txt, on_click=next_day, key="next_day_btn")
                    else:
                        st.button(f"안 읽음 {unread_count}", disabled=True, key="wait_day_btn")

        # 2) 아이폰 문자 스타일 1:1 대화방 화면
        elif st.session_state.phone_view == "chat":
            cid = st.session_state.active_chat
            info = CONTACTS[cid]

            with st.container(key="phone_topbar_row"):
                c_back, c_prof, c_sp = st.columns([1, 2.5, 1])
                with c_back:
                    with st.container(key="phone_back"):
                        back_lbl = f"< {unread_count}" if unread_count > 0 else "< 목록"
                        st.button(back_lbl, on_click=go_view, args=("list",), key="back_btn")
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

            # 하단 SMS 입력창 + 답장 버튼
            if cid not in st.session_state.replied_today:
                st.markdown(
                    '<div class="ios-input-row">'
                    '<div class="ios-plus">+</div>'
                    '<div class="ios-pill-input">문자 메시지 · SMS</div>'
                    '</div>',
                    unsafe_allow_html=True,
                )
                with st.container(key="phone_replies"):
                    choices = CHAT_SCRIPT[st.session_state.day][cid]["choices"]
                    for idx, ch in enumerate(choices):
                        st.button(
                            ch["reply"],
                            on_click=send_reply,
                            args=(cid, idx),
                            key=f"reply_{st.session_state.day}_{cid}_{idx}",
                        )
            else:
                st.markdown(
                    '<div class="ios-input-row">'
                    '<div class="ios-plus">+</div>'
                    '<div class="ios-pill-input">답장 완료</div>'
                    '</div>',
                    unsafe_allow_html=True,
                )

        # 3) 메모장 화면
        elif st.session_state.phone_view == "memo":
            with st.container(key="phone_topbar_row"):
                c_back, c_prof, c_sp = st.columns([1, 2.5, 1])
                with c_back:
                    with st.container(key="phone_back"):
                        st.button("< 목록", on_click=go_view, args=("list",), key="memo_back")
                with c_prof:
                    st.markdown(
                        '<div class="ios-center-profile">'
                        '<div class="ios-name">메모장</div>'
                        '</div>',
                        unsafe_allow_html=True,
                    )
                with c_sp:
                    st.markdown("<div></div>", unsafe_allow_html=True)

            notes_html = "".join(f'<div class="memo-item">{m}</div>' for m in MEMO_NOTES)
            st.markdown(f'<div class="memo-scroll">{notes_html}</div>', unsafe_allow_html=True)

        # 하단 홈 바
        st.markdown('<div class="ios-homebar"></div>', unsafe_allow_html=True)

# [B] 엔딩 화면
elif st.session_state.phase == "ending":
    end = ENDINGS[st.session_state.ending_key]
    st.markdown(f"### {end['title']}")
    formatted = end["text"].replace("\n", "<br>")
    st.markdown(f'<div class="story-box">{formatted}</div>', unsafe_allow_html=True)
    st.button("처음부터 다시 시작하기", on_click=init_game, key="ending_retry")
