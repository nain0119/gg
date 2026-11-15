import html
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마 + 스마트폰 채팅앱 CSS
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

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3.5rem;
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

/* 진짜 네모난 스마트폰 본체 */
.st-key-phone_shell {
    max-width: 410px !important;
    margin: 0 auto !important;
    background: #11100f !important;
    border: 3px solid #49413b !important;
    border-radius: 26px !important;
    padding: 12px 16px 12px 16px !important;
    box-shadow: 0 22px 50px rgba(0, 0, 0, 0.8), inset 0 0 0 1px #272320 !important;
}

/* 상단 노치 & 상태바 */
.phone-notch {
    width: 72px;
    height: 5px;
    background: #2f2a26;
    border-radius: 99px;
    margin: 2px auto 10px auto;
}

.phone-status {
    display: flex;
    justify-content: space-between;
    font-size: 0.74rem;
    color: #9b9389;
    padding: 0 4px 8px 4px;
    border-bottom: 1px solid #24201d;
    margin-bottom: 4px;
}

/* 앱 상단 바 */
.app-titlebar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 4px 10px 4px;
    border-bottom: 1px solid #2b2623;
    margin-bottom: 6px;
}

.app-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #e7e1d8;
}

.app-badge {
    font-size: 0.76rem;
    color: #cf6a6a;
    border: 1px solid #6f3434;
    padding: 2px 8px;
    border-radius: 99px;
}

/* 채팅방 상대 헤더 */
.room-profile {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 2px 0;
}

.avatar-lg {
    width: 34px;
    height: 34px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    color: #f3ede5;
    flex-shrink: 0;
}

.room-name {
    font-size: 0.96rem;
    font-weight: 700;
    color: #e7e1d8;
    line-height: 1.2;
}

.room-status {
    font-size: 0.74rem;
    color: #9b9389;
}

/* 스크롤 가능한 채팅창 (자동으로 하단 고정) */
.chat-scroll {
    height: 350px;
    overflow-y: auto;
    display: flex;
    flex-direction: column-reverse;
    background: #171514;
    border: 1px solid #2b2623;
    border-radius: 10px;
    padding: 12px 10px;
    margin: 4px 0 8px 0;
}

.chat-scroll::-webkit-scrollbar {
    width: 5px;
}

.chat-scroll::-webkit-scrollbar-thumb {
    background: #3a332e;
    border-radius: 99px;
}

.chat-inner {
    display: flex;
    flex-direction: column;
}

/* 말풍선 */
.msg-sys {
    align-self: center;
    background: #23201d;
    color: #9b9389;
    font-size: 0.74rem;
    padding: 3px 10px;
    border-radius: 99px;
    margin: 10px 0;
}

.msg-npc-wrap {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 10px;
}

.avatar-sm {
    width: 28px;
    height: 28px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.78rem;
    color: #f3ede5;
    flex-shrink: 0;
    margin-top: 2px;
}

.msg-npc-body {
    display: flex;
    flex-direction: column;
    max-width: 78%;
}

.msg-name {
    font-size: 0.73rem;
    color: #9b9389;
    margin-bottom: 3px;
}

.bubble-row {
    display: flex;
    align-items: flex-end;
    gap: 5px;
}

.bubble-npc {
    background: #282422;
    border: 1px solid #3c3530;
    color: #e7e1d8;
    padding: 8px 12px;
    border-radius: 3px 12px 12px 12px;
    font-size: 0.89rem;
    line-height: 1.55;
    word-break: break-word;
}

.msg-me-wrap {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    gap: 5px;
    margin-bottom: 10px;
}

.bubble-me {
    background: #612e2e;
    border: 1px solid #824040;
    color: #f5efe8;
    padding: 8px 12px;
    border-radius: 12px 3px 12px 12px;
    max-width: 75%;
    font-size: 0.89rem;
    line-height: 1.55;
    word-break: break-word;
}

.msg-time {
    font-size: 0.68rem;
    color: #7d756d;
    white-space: nowrap;
}

/* 가짜 메시지 입력창 */
.faux-input {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1c1a18;
    border: 1px solid #332d29;
    border-radius: 18px;
    padding: 7px 14px;
    font-size: 0.82rem;
    color: #7d756d;
    margin-bottom: 6px;
}

.faux-send {
    color: #b56c65;
    font-weight: 700;
    font-size: 0.78rem;
}

/* 하단 홈 인디케이터 */
.phone-homebar {
    width: 110px;
    height: 4px;
    background: #49413b;
    border-radius: 99px;
    margin: 10px auto 2px auto;
}

/* 메모장 카드 */
.memo-scroll {
    height: 360px;
    overflow-y: auto;
    background: #171514;
    border: 1px solid #2b2623;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 10px;
}

.memo-item {
    background: #211e1c;
    border-left: 3px solid #824040;
    padding: 10px 12px;
    border-radius: 4px;
    margin-bottom: 9px;
    font-size: 0.86rem;
    line-height: 1.6;
}

/* 도입 & 엔딩 상자 */
.story-box {
    background: var(--panel);
    border: 1px solid var(--line);
    border-left: 3px solid #6f3434;
    padding: 22px 24px;
    border-radius: 3px;
    line-height: 1.9;
    margin: 14px 0 20px 0;
}

/* 기본 버튼 */
div.stButton > button {
    width: 100%;
    background: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.92rem;
    transition: 0.15s;
}

div.stButton > button:hover {
    background: #302522 !important;
    border-color: var(--accent) !important;
    color: #ffffff !important;
}

/* 채팅 목록 버튼 스타일 */
.st-key-phone_list button {
    text-align: left !important;
    background: #1a1817 !important;
    border: 1px solid #2d2824 !important;
    border-radius: 10px !important;
    padding: 11px 13px !important;
    font-size: 0.88rem !important;
    line-height: 1.45 !important;
}

.st-key-phone_list button:hover {
    background: #25211e !important;
    border-color: #6f3434 !important;
}

/* 답장 버튼 스타일 */
.st-key-phone_replies button {
    text-align: left !important;
    background: #271b1b !important;
    border: 1px solid #593535 !important;
    border-radius: 10px !important;
    padding: 9px 12px !important;
    font-size: 0.86rem !important;
    line-height: 1.45 !important;
}

.st-key-phone_replies button:hover {
    background: #3b2323 !important;
    border-color: #a34b4b !important;
}

/* 상단 뒤로가기 & 하단 탭 버튼 */
.st-key-phone_back button,
.st-key-phone_nav button {
    background: #1b1918 !important;
    border: 1px solid #352f2b !important;
    border-radius: 8px !important;
    padding: 6px 10px !important;
    font-size: 0.82rem !important;
    min-height: 2.2rem !important;
}

[data-testid="stProgress"] > div > div > div > div {
    background: var(--accent) !important;
}

[data-testid="stProgress"] > div > div > div {
    background: #39322e !important;
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
    "mori": {"name": "모리 오가이", "initial": "모", "color": "#7a3535", "status": "진료실 문 열려 있음"},
    "dazai": {"name": "다자이 오사무", "initial": "다", "color": "#4b5a69", "status": "입수하기 좋은 날"},
    "chuuya": {"name": "나카하라 츄야", "initial": "츄", "color": "#8a5233", "status": "건드리면 날아감"},
    "akane": {"name": "아카네", "initial": "아", "color": "#4c4846", "status": "."},
}

CHAT_SCRIPT = {
    1: {
        "mori": {
            "time": "09:02",
            "incoming": "유스케 군~ 진료 시간 10분 지났는데 아직도 이불 속이니? ^^",
            "choices": [
                {
                    "reply": "아 안 죽었어 모리 씨. 귀찮게 톡하지 마",
                    "npc_after": "어머 기운 넘치네. 그럼 오늘 치 약은 퀵으로 보내줄게.",
                    "hp": 10,
                    "suspicion": -5,
                },
                {
                    "reply": "죄송합니다 보스님!! 지금 바로 뛰어갈게요!!",
                    "npc_after": "...보스님? 유스케 군 핸드폰 누가 훔쳐 갔니?",
                    "hp": -5,
                    "suspicion": 35,
                },
                {
                    "reply": "몸 아파서 못 나감. 알아서 갖다 줘",
                    "npc_after": "하긴 네가 제 발로 올 리가 없지. 사람 보낼게.",
                    "hp": 5,
                    "suspicion": 0,
                },
            ],
        },
        "dazai": {
            "time": "09:11",
            "incoming": "유스케~ 나 지금 다리 위인데 물 색깔 예술이야. 같이 뛰어내릴래?",
            "choices": [
                {
                    "reply": "개소리 마. 역겹고 의미 없어도 살아있는 게 백 배 낫거든",
                    "npc_after": "흥, 여전히 노잼 생존주의자네. 치사해.",
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "무슨 일 있어? 나랑 맛있는 거라도 먹자",
                    "npc_after": "...잠깐. 유스케가 방금 나한테 밥 사준다고 했어? 너 누구냐.",
                    "hp": 0,
                    "suspicion": 35,
                },
            ],
        },
        "chuuya": {
            "time": "09:18",
            "incoming": "야 기시. 내 책상 위 결재 서류 파쇄기에 처넣은 거 너지",
            "choices": [
                {
                    "reply": "난 내 책상 것만 갈았거든? 나한테 뒤집어씌우지 마",
                    "npc_after": "하아?! 네 놈 전적이 몇 번인데 헛소리야. 여튼 불쾌한 놈.",
                    "hp": -5,
                    "suspicion": -5,
                },
                {
                    "reply": "정말 죄송합니다! 제가 지금 당장 다시 복구하겠습니다!",
                    "npc_after": "...너 오늘 뭘 잘못 처먹었냐? 사과하는 거 더 기분 나쁘네.",
                    "hp": 0,
                    "suspicion": 25,
                },
            ],
        },
        "akane": {
            "time": "09:24",
            "incoming": "아까 복도에서 들이받고 튄 거 너지",
            "choices": [
                {
                    "reply": "너도 나 안 보이면서 내 탓하지 마",
                    "npc_after": "응. 조심해.",
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "앗 아카네! 많이 다쳤어? 내가 연고 사다 줄까?",
                    "npc_after": "...너 누구야. 기시는 그런 말 안 해.",
                    "hp": 0,
                    "suspicion": 25,
                },
            ],
        },
    },
    2: {
        "mori": {
            "time": "10:05",
            "incoming": "어제 보낸 약은 잘 먹었니? 오늘따라 안 보이니 심심하구나.",
            "choices": [
                {
                    "reply": "약 맛없어. 사탕이나 끼워서 보내",
                    "npc_after": "하하 여전히 뻔뻔해서 안심했네. 내일 치도 챙겨둘게.",
                    "hp": 10,
                    "suspicion": -5,
                },
                {
                    "reply": "감사합니다! 덕분에 컨디션이 엄청 좋아졌어요!",
                    "npc_after": "느낌표까지 붙이고… 유스케 군 요즘 머리를 어디 박았니?",
                    "hp": 5,
                    "suspicion": 30,
                },
            ],
        },
        "dazai": {
            "time": "13:40",
            "incoming": "심심해~ 나 방금 츄야 모자에 낙서했는데 같이 구경할래?",
            "choices": [
                {
                    "reply": "아 그 꼬맹이? 모자 잃어버리면 울 텐데 잘했네",
                    "npc_after": "오~ 역시 츄야 놀릴 때만 손발이 척척 맞는다니까.",
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "남의 물건에 낙서하면 안 되지. 빨리 지우고 사과해.",
                    "npc_after": "어라라? 유스케가 도덕 교과서를 삼켰나. 수상하네.",
                    "hp": 0,
                    "suspicion": 30,
                },
            ],
        },
        "chuuya": {
            "time": "15:12",
            "incoming": "어이, 어제 복도에서 마주칠 때마다 헛구역질 좀 하지 마. 열받으니까.",
            "choices": [
                {
                    "reply": "사방에 네 얼굴이 복붙돼서 뜨는데 속이 안 뒤집히겠냐",
                    "npc_after": "아 젠장 또 네 놈 능력 얘기냐. 천 뒤집어쓰고 방에 쳐박혀 있어 그럼.",
                    "hp": -5,
                    "suspicion": -5,
                },
                {
                    "reply": "아뇨! 저 츄야 씨 엄청 좋아하고 존경해요!",
                    "npc_after": "미쳤냐?! 소름 돋으니까 헛소리할 거면 차단한다.",
                    "hp": -5,
                    "suspicion": 30,
                },
            ],
        },
        "akane": {
            "time": "12:15",
            "incoming": "식당 안 가",
            "choices": [
                {
                    "reply": "오늘 마늘 카레 냄새 나서 안 감",
                    "npc_after": "알겠어. 내 거 뺏어 먹지 마.",
                    "hp": 5,
                    "suspicion": -5,
                },
                {
                    "reply": "응! 같이 가자! 내가 맛있는 거 사줄게!",
                    "npc_after": "...돈도 없는 거지가 이상한 소리 하네.",
                    "hp": 0,
                    "suspicion": 20,
                },
            ],
        },
    },
    3: {
        "mori": {
            "time": "21:10",
            "incoming": "그러고 보니 유스케 군, 요즘 톡 말투가 묘하게 다를 때가 있더구나. 무슨 일 있니?",
            "choices": [
                {
                    "reply": "모리 씨 면상 안 봐서 기분이 왔다 갔다 하나 보지",
                    "npc_after": "후후, 그 험한 입을 보니 진짜 유스케 군이 맞나 보네. 잘 지내렴.",
                    "hp": 10,
                    "suspicion": -10,
                },
                {
                    "reply": "아뇨! 저 완전 멀쩡해요! 걱정 감사드립니다!",
                    "npc_after": "그래. 그럼 확인하러 조금 이따 방으로 직접 들를게 ^^",
                    "hp": -10,
                    "suspicion": 40,
                },
            ],
        },
        "dazai": {
            "time": "22:03",
            "incoming": "유스케, 요즘 왜 자꾸 폰으로만 떠들어? 설마 진짜 다른 사람으로 바뀐 건 아니지?",
            "choices": [
                {
                    "reply": "응 네 면상 보기 싫어서 안 나감. 수고",
                    "npc_after": "하긴 네가 나 보고 싶어서 나올 리가 없지. 납득했어~",
                    "hp": 0,
                    "suspicion": -10,
                },
                {
                    "reply": "무슨 소리야! 나 진짜 기시 유스케 맞아!",
                    "npc_after": "진짜 유스케는 그런 구차한 변명 안 해. 재미있어지네?",
                    "hp": 0,
                    "suspicion": 35,
                },
            ],
        },
        "chuuya": {
            "time": "22:41",
            "incoming": "야. 내일 아침엔 기어 나와라. 또 방구석에 짱박히면 문 따고 들어간다.",
            "choices": [
                {
                    "reply": "오든가 말든가. 대신 마늘 냄새 풍기면서 오지 마",
                    "npc_after": "누가 그런 거 들고 간댔냐. 여튼 내일 얼굴 본다.",
                    "hp": 0,
                    "suspicion": -5,
                },
                {
                    "reply": "네! 내일 일찍 출근해서 인사드리겠습니다!",
                    "npc_after": "...기시 너 진짜 누구야. 내일 보자마자 확인한다.",
                    "hp": -5,
                    "suspicion": 35,
                },
            ],
        },
        "akane": {
            "time": "23:15",
            "incoming": "살아있냐",
            "choices": [
                {
                    "reply": "어. 죽는 것보다 사는 게 낫잖아",
                    "npc_after": "그래. 내일 또 복도에서 부딪히지 마.",
                    "hp": 5,
                    "suspicion": -5,
                },
                {
                    "reply": "응응! 걱정해 줘서 너무 고마워 아카네!",
                    "npc_after": "...소름 돋아. 차단함.",
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


def next_minute_str(time_str: str, add_min: int) -> str:
    h, m = map(int, time_str.split(":"))
    total = h * 60 + m + add_min
    return f"{(total // 60) % 24:02d}:{total % 60:02d}"


def push_day_messages(day: int):
    day_data = CHAT_SCRIPT[day]
    for cid, data in day_data.items():
        st.session_state.histories[cid].append(
            {"sender": "sys", "text": f"{day}일차"}
        )
        st.session_state.histories[cid].append(
            {"sender": "npc", "text": data["incoming"], "time": data["time"]}
        )


def init_game():
    st.session_state.phase = "intro"
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


def open_phone():
    st.session_state.phase = "phone"
    st.session_state.phone_view = "list"


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
    t_me = next_minute_str(data["time"], 2)
    t_npc = next_minute_str(data["time"], 3)

    st.session_state.histories[cid].append(
        {"sender": "me", "text": ch["reply"], "time": t_me}
    )
    st.session_state.histories[cid].append(
        {"sender": "npc", "text": ch["npc_after"], "time": t_npc}
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
    '<p style="color:#b56c65; letter-spacing:4px; font-size:12px;">'
    'PORT MAFIA  /  YUSUKE SMARTPHONE</p>',
    unsafe_allow_html=True,
)
st.title("기시 유스케 생존 톡")
st.divider()

# [A] 도입
if st.session_state.phase == "intro":
    st.markdown(
        """
        <div class="story-box">
        눈을 뜬다. 한쪽 눈이 안 보이고 얼굴엔 검은 천이 덮여 있다.<br>
        거울을 보니 9년 차 말단 시한부, <strong>기시 유스케</strong>의 몸이다.<br><br>
        방 밖으로 나가면 100% 들키거나 맞아 죽을 게 뻔하다.
        일단 이불 속에 처박혀 옆에 놓인 <strong>유스케의 핸드폰</strong>으로 날아오는 연락부터 처리한다.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.button("핸드폰을 켠다", on_click=open_phone, key="open_phone_btn")

# [B] 진짜 네모난 스마트폰 화면
elif st.session_state.phase == "phone":
    with st.container(border=True, key="phone_shell"):
        # 상단 노치 & 상태바
        battery = max(12, st.session_state.hp)
        st.markdown(
            f'<div class="phone-notch"></div>'
            f'<div class="phone-status">'
            f'<span>DAY {st.session_state.day}</span>'
            f'<span>PORT-NET LTE</span>'
            f'<span>배터리 {battery}%</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # 1) 채팅 목록 화면
        if st.session_state.phone_view == "list":
            badge_txt = f"새 톡 {unread_count}" if unread_count > 0 else "모두 읽음"
            st.markdown(
                f'<div class="app-titlebar">'
                f'<span class="app-title">채팅</span>'
                f'<span class="app-badge">{badge_txt}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

            with st.container(key="phone_list"):
                for cid, info in CONTACTS.items():
                    is_unread = cid not in st.session_state.replied_today
                    tag = "[안읽음] " if is_unread else "[읽음] "
                    last_msg = st.session_state.histories[cid][-1]
                    preview = last_msg["text"]
                    if len(preview) > 22:
                        preview = preview[:22] + "..."
                    t_str = last_msg.get("time", "")
                    st.button(
                        f"{tag}**{info['name']}**  `{t_str}`\n\n{preview}",
                        on_click=open_chat,
                        args=(cid,),
                        key=f"chat_list_{cid}",
                    )

            st.write("")
            with st.container(key="phone_nav"):
                col1, col2 = st.columns(2)
                with col1:
                    st.button("메모장", on_click=go_view, args=("memo",), key="open_memo")
                with col2:
                    if unread_count == 0:
                        btn_txt = "3일차 마감" if st.session_state.day >= 3 else "다음 날로"
                        st.button(btn_txt, on_click=next_day, key="next_day_btn")
                    else:
                        st.button("답장 대기 중", disabled=True, key="wait_day_btn")

        # 2) 1:1 채팅방 화면
        elif st.session_state.phone_view == "chat":
            cid = st.session_state.active_chat
            info = CONTACTS[cid]

            col_back, col_prof = st.columns([1.1, 3.9])
            with col_back:
                with st.container(key="phone_back"):
                    st.button("< 목록", on_click=go_view, args=("list",), key="back_btn")
            with col_prof:
                st.markdown(
                    f'<div class="room-profile">'
                    f'<div class="avatar-lg" style="background:{info["color"]};">{info["initial"]}</div>'
                    f'<div>'
                    f'<div class="room-name">{info["name"]}</div>'
                    f'<div class="room-status">{info["status"]}</div>'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            # 스크롤 채팅창 (flex-direction: column-reverse 로 최신 메시지 하단 유지)
            items = []
            for msg in st.session_state.histories[cid]:
                safe_txt = html.escape(msg["text"])
                t_str = msg.get("time", "")
                if msg["sender"] == "sys":
                    items.append(f'<div class="msg-sys">{safe_txt}</div>')
                elif msg["sender"] == "npc":
                    items.append(
                        f'<div class="msg-npc-wrap">'
                        f'<div class="avatar-sm" style="background:{info["color"]};">{info["initial"]}</div>'
                        f'<div class="msg-npc-body">'
                        f'<div class="msg-name">{info["name"]}</div>'
                        f'<div class="bubble-row">'
                        f'<div class="bubble-npc">{safe_txt}</div>'
                        f'<span class="msg-time">{t_str}</span>'
                        f'</div>'
                        f'</div>'
                        f'</div>'
                    )
                else:
                    items.append(
                        f'<div class="msg-me-wrap">'
                        f'<span class="msg-time">{t_str}</span>'
                        f'<div class="bubble-me">{safe_txt}</div>'
                        f'</div>'
                    )

            if st.session_state.last_notice:
                items.append(f'<div class="msg-sys">{st.session_state.last_notice}</div>')

            chat_html = (
                '<div class="chat-scroll"><div class="chat-inner">'
                + "".join(items)
                + '</div></div>'
            )
            st.markdown(chat_html, unsafe_allow_html=True)

            # 하단 가짜 입력창 & 답장 선택지
            if cid not in st.session_state.replied_today:
                st.markdown(
                    '<div class="faux-input">'
                    '<span>보낼 답장을 고르세요...</span>'
                    '<span class="faux-send">전송</span>'
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
                    '<div class="faux-input">'
                    '<span>오늘 대화가 끝났습니다</span>'
                    '<span class="faux-send">완료</span>'
                    '</div>',
                    unsafe_allow_html=True,
                )

        # 3) 메모장 화면
        elif st.session_state.phone_view == "memo":
            col_back, col_prof = st.columns([1.1, 3.9])
            with col_back:
                with st.container(key="phone_back"):
                    st.button("< 목록", on_click=go_view, args=("list",), key="memo_back")
            with col_prof:
                st.markdown(
                    '<div class="room-profile">'
                    '<div>'
                    '<div class="room-name">메모장</div>'
                    '<div class="room-status">유스케의 생존 수칙</div>'
                    '</div>'
                    '</div>',
                    unsafe_allow_html=True,
                )

            notes_html = "".join(f'<div class="memo-item">{m}</div>' for m in MEMO_NOTES)
            st.markdown(f'<div class="memo-scroll">{notes_html}</div>', unsafe_allow_html=True)

        # 하단 아이폰 스타일 홈 바
        st.markdown('<div class="phone-homebar"></div>', unsafe_allow_html=True)

# [C] 엔딩 화면
elif st.session_state.phase == "ending":
    end = ENDINGS[st.session_state.ending_key]
    st.markdown(f"### {end['title']}")
    formatted = end["text"].replace("\n", "<br>")
    st.markdown(f'<div class="story-box">{formatted}</div>', unsafe_allow_html=True)
    st.button("처음부터 다시 시작하기", on_click=init_game, key="ending_retry")
