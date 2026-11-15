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
    .stApp,
    header[data-testid="stHeader"],
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] {
        border-right: 1px solid #333333;
    }
    h1, h2, h3, h4, p, span, label, div {
        color: #ffffff;
    }
    .story-box {
        background-color: #000000;
        border: 1px solid #ffffff;
        padding: 22px 26px;
        border-radius: 6px;
        line-height: 1.85;
        font-size: 1.05rem;
        margin-bottom: 18px;
    }
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.88rem;
        font-weight: 600;
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #ffffff;
        margin-top: 8px;
    }
    div.stButton > button {
        width: 100%;
        text-align: left;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #666666 !important;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 0.98rem;
    }
    div.stButton > button:hover {
        background-color: #1a1a1a !important;
        border-color: #ffffff !important;
        color: #ffffff !important;
    }
    div[data-testid="stProgress"] > div > div > div > div {
        background-color: #ffffff !important;
    }
    div[data-testid="stProgress"] > div > div > div {
        background-color: #262626 !important;
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
        (1, 0): {
            "id": "prologue",
            "title": "DAY 1 오전 - 낯선 천, 한쪽 눈의 어둠",
            "text": (
                "눈을 뜨자 지독한 소독약 냄새와 함께 폐부 깊숙이 묵직한 통증이 스친다. "
                "시야 한쪽은 완전히 어둡고, 얼굴 위에는 얇은 천이 드리워져 있다.\n\n"
                "당신은 포트 마피아 9년 차 말단이자 시한부 생존주의자, **'기시 유스케'**의 몸에 빙의했다.\n\n"
                "그때 문이 열리며 누군가 들어온다. 천 너머로 비친 상대의 얼굴은 **나카하라 츄야**다. "
                "아니, 이능력 「검은 집」 때문에 상대가 가장 믿는 인물로 보이는 것뿐일지도 모른다.\n\n"
                "\"어이, 기시. 아직도 자빠져 자고 있냐? 모리 보스께서 부르시던데.\""
            ),
            "choices": [
                {
                    "label": "1. (반말 유지) \"아, 시끄러워. 알아서 갈 테니까 넌 네 할 일이나 해.\"",
                    "hp_delta": 0,
                    "result": (
                        "상대는 혀를 차더니 \"여전히 싸가지 없네\"라며 문을 닫고 나갔다. "
                        "자연스럽게 넘어갔다."
                    ),
                },
                {
                    "label": "2. (일반인 습관) \"아, 죄송합니다! 지금 바로 가겠습니다!\"",
                    "hp_delta": -15,
                    "result": (
                        "\"...뭐야, 너 어디 잘못 먹었냐? 기시가 존댓말을 다 하고?\" "
                        "수상한 시선을 피해 급히 빠져나오느라 진이 다 빠졌다."
                    ),
                },
                {
                    "label": "3. 천을 벗어 얼굴을 확인한다. (「검은 집」 발동)",
                    "hp_delta": -10,
                    "result": (
                        "천을 걷자 조직원이 사색이 되어 \"츄, 츄야 님?!\" 하고 허리를 90도로 꺾었다. "
                        "능글맞게 넘기긴 했지만 이능력 사용 탓에 기력이 소모됐다."
                    ),
                },
            ],
        },
        (1, 1): {
            "id": "shredder",
            "title": "DAY 1 오후 - 말단의 책상과 파쇄기",
            "text": (
                "유스케의 책상 위에는 서류가 수북이 쌓여 있고, 옆에는 **문서 파쇄기**가 놓여 있다. "
                "원래 유스케는 서류를 받자마자 파쇄기에 갈아버리는 인간이다."
            ),
            "choices": [
                {
                    "label": "1. 고민 없이 서류 뭉치를 통째로 파쇄기에 처넣는다.",
                    "hp_delta": 5,
                    "result": (
                        "시원하게 갈려나가는 서류를 보며 주변 조직원들이 고개를 끄덕인다. "
                        "일도 안 하고 편하게 쉬었다."
                    ),
                },
                {
                    "label": "2. 양심상 꼼꼼히 분류해서 결재를 올린다.",
                    "hp_delta": -15,
                    "result": (
                        "상급자가 \"너 갑자기 왜 일을 해?\"라며 의심스럽게 뜯어보는 통에 "
                        "온몸에 식은땀이 흐르고 피로가 몰려왔다."
                    ),
                },
            ],
        },
        (1, 2): {
            "id": "mori_clinic_1",
            "title": "DAY 1 밤 - 모리 오가이의 진료실",
            "text": (
                "포트 마피아 보스 **모리 오가이**가 생글생글 웃으며 약봉지를 준비하고 있다. "
                "유스케는 모리를 일방적으로 혐오하며 반말을 쓰고, 모리는 그런 유스케를 즐긴다.\n\n"
                "\"유스케 군, 오늘도 기특하게 살아 있구나? 컨디션은 어때?\""
            ),
            "choices": [
                {
                    "label": "1. \"보면 몰라? 모리 씨 얼굴 보니까 수명이 더 줄어드는 기분인데.\"",
                    "hp_delta": 20,
                    "result": (
                        "모리가 쿡쿡 웃으며 만족스러운 듯 약을 건넸다. "
                        "\"하하, 기운이 넘치는 걸 보니 다행이네.\" 약 덕분에 체력이 회복됐다."
                    ),
                },
                {
                    "label": "2. \"보스님, 신경 써주셔서 감사합니다. 약 잘 먹겠습니다.\"",
                    "hp_delta": -20,
                    "result": (
                        "모리의 미소가 서늘하게 굳었다. 추궁을 피하려고 억지로 헛소리를 늘어놓다 "
                        "정신이 피폐해지고 체력도 크게 깎였다."
                    ),
                },
            ],
        },
        (3, 1): {
            "id": "real_chuuya",
            "title": "DAY 3 오후 - 진짜 나카하라 츄야와의 조우",
            "text": (
                "복도 모퉁이를 돌다 **진짜 나카하라 츄야**와 마주쳤다.\n"
                "\"어이, 기시. 아까부터 어슬렁거리면서 뭘 쳐다보는 거야? 기분 나쁘게.\""
            ),
            "choices": [
                {
                    "label": "1. \"하아? 사방에 네 얼굴이 널려 있어서 토 나올 것 같다고.\"",
                    "hp_delta": -5,
                    "result": (
                        "츄야가 주먹을 부르르 떨었지만, 이능력 때문인 걸 떠올리고는 혀를 차며 지나갔다. "
                        "약간의 위압감에 눌렸지만 무사히 넘겼다."
                    ),
                },
                {
                    "label": "2. \"우와, 진짜 츄야 씨다! 사진이랑 똑같네요!\"",
                    "hp_delta": -35,
                    "result": (
                        "\"...너 돌았냐?\" 츄야의 발길질에 벽으로 날아가 처박혔다. "
                        "뼈가 부러지지 않은 게 기적이다."
                    ),
                },
            ],
        },
        (4, 2): {
            "id": "dazai_encounter",
            "title": "DAY 4 밤 - 요코하마 뒷골목, 다자이 오사무",
            "text": (
                "항구 근처 골목에서 **다자이 오사무**와 마주쳤다. "
                "어릴 적 유일한 친구이자 사상이 정반대인 가장 위험한 인물이다.\n\n"
                "\"어라? 이 죽지 못해 안달 난 기척은 유스케잖아? 혹시 요즘엔 죽고 싶어졌니?\""
            ),
            "choices": [
                {
                    "label": "1. \"개소리 마, 다자이. 역겹고 의미 없는 삶이라도 죽는 것보단 낫거든.\"",
                    "hp_delta": 5,
                    "result": (
                        "다자이가 지루하다는 듯 한숨을 쉰다. \"흥, 재미없어.\" "
                        "완벽하게 유스케답게 받아쳐 위기를 넘겼다."
                    ),
                },
                {
                    "label": "2. \"솔직히 요즘 힘들어서 나도 가끔 그럴 때가 있어…\"",
                    "hp_delta": -30,
                    "result": (
                        "다자이의 눈이 서늘한 암흑으로 가라앉았다. \"너, 안에 들어있는 게 누구지?\" "
                        "필사적으로 얼버무리며 도망치느라 체력을 크게 소모했다."
                    ),
                },
            ],
        },
        (6, 1): {
            "id": "teacher_shadow",
            "title": "DAY 6 오후 - 총격전과 '선생님'의 그림자",
            "text": (
                "외부 심부름 중 적대 조직의 습격에 휘말렸다. 잔해 아래에 **어린아이**가 갇혀 울고 있다. "
                "유스케를 키웠던 '선생님'도 아이들을 구하다 죽었기에, 유스케는 남을 버리고 살아남는 길을 택해 왔다."
            ),
            "choices": [
                {
                    "label": "1. 유스케답게 외면하고 내 살길만 찾아 도망친다.",
                    "hp_delta": -5,
                    "result": (
                        "마음은 무겁지만 몸은 생존 본능대로 움직여 큰 부상 없이 현장을 빠져나왔다."
                    ),
                },
                {
                    "label": "2. 무리해서 아이를 구하고 몰래 빠져나온다.",
                    "hp_delta": -25,
                    "result": (
                        "「검은 집」을 써서 아이를 안심시키고 구해냈지만, 허약한 몸에 무리가 와 크게 다쳤다."
                    ),
                },
            ],
        },
        (7, 2): {
            "id": "final_night",
            "title": "DAY 7 밤 - 마지막 진료",
            "text": (
                "일주일째의 밤. 모리 오가이의 진료실에서 마지막 검진을 받는다.\n"
                "\"유스케 군, 일주일 동안 잘 버텼구나. 앞으로도 살아남을 준비는 되어 있니?\""
            ),
            "choices": [
                {
                    "label": "1. \"쓸데없는 소리 말고 약이나 놔, 모리 씨. 무슨 짓을 해서든 살 거니까.\"",
                    "hp_delta": 15,
                    "result": (
                        "모리가 웃으며 약을 놓아주었다. 길고 위태로웠던 일주일이 마침내 끝을 맺는다."
                    ),
                },
                {
                    "label": "2. 아무 말 없이 조용히 고개만 끄덕인다.",
                    "hp_delta": 5,
                    "result": (
                        "모리가 의미심장한 미소를 지으며 주사를 놔주었다. 무사히 마지막 밤을 넘겼다."
                    ),
                },
            ],
        },
    }


def get_pool_events():
    return [
        {
            "id": "akane_bump",
            "title": "복도의 불시 충돌 - 아카네",
            "text": (
                "천을 쓴 채 복도를 걷다 **아카네**와 정면으로 부딪혀 넘어졌다. "
                "아무도 믿지 못하는 아카네의 눈엔 유스케의 머리가 보이지 않고, "
                "천을 쓴 유스케의 눈에도 아카네가 보이지 않기 때문이다."
            ),
            "choices": [
                {
                    "label": "1. \"너도 안 보이긴 마찬가지잖아. 조심 좀 해, 아카네.\"",
                    "hp_delta": -5,
                    "result": "가볍게 타박상을 입었을 뿐 서로 아무렇지 않게 지나갔다.",
                },
                {
                    "label": "2. \"미안! 많이 다쳤어? 괜찮아?\"",
                    "hp_delta": -12,
                    "result": "아카네가 기분 나쁘다는 듯 경계하며 쏘아붙여 정신적 피로가 쌓였다.",
                },
            ],
        },
        {
            "id": "shohei_lunch",
            "title": "식당의 함정 - 쇼헤이와 점심",
            "text": (
                "**쇼헤이**가 당신 앞에 향신료 냄새가 진동하는 매운 마늘 카레를 밀어 놓는다. "
                "유스케는 **향이 강한 음식**을 끔찍하게 싫어한다."
            ),
            "choices": [
                {
                    "label": "1. \"야, 나 냄새 지독한 거 싫어하는 거 알면서 일부러 이러지?!\"",
                    "hp_delta": 10,
                    "result": "쇼헤이가 피식 웃으며 맹숭맹숭한 죽으로 바꿔주었다. 맛있게 먹고 체력을 회복했다.",
                },
                {
                    "label": "2. 아까워서 그냥 한 입 크게 떠먹는다.",
                    "hp_delta": -20,
                    "result": "강렬한 향에 속이 완전히 뒤집혀 한동안 앓아누웠다.",
                },
            ],
        },
        {
            "id": "chuuya_hallway",
            "title": "사방이 츄야인 복도",
            "text": (
                "천 너머로 보이는 조직원들의 얼굴이 전부 츄야로 보인다. 그중 한 명이 어깨를 부딪치며 시비를 건다."
            ),
            "choices": [
                {
                    "label": "1. 눈을 질끈 감고 무시한 채 빠르게 피한다.",
                    "hp_delta": -3,
                    "result": "기분은 찜찜하지만 무사히 화장실로 도피했다.",
                },
                {
                    "label": "2. 목소리를 구분해 말단임을 확인하고 내 심부름을 떠넘긴다.",
                    "hp_delta": 5,
                    "result": "이기적인 유스케답게 잡일을 넘기고 숙소에서 쉬었다.",
                },
            ],
        },
        {
            "id": "mirror_truth",
            "title": "거울 앞의 휴식",
            "text": (
                "아무도 없는 숙소. 천을 벗고 세면대 거울 앞에 섰다. 잠시나마 긴장을 풀고 쉴 수 있는 시간이다."
            ),
            "choices": [
                {
                    "label": "1. 눈을 감고 침대에 누워 푹 잔다.",
                    "hp_delta": 18,
                    "result": "꿀 같은 휴식 덕분에 체력이 크게 회복되었다.",
                },
                {
                    "label": "2. 거울을 보며 유스케의 비웃는 표정을 연습한다.",
                    "hp_delta": 5,
                    "result": "연기 연습도 하고 가볍게 숨을 돌렸다.",
                },
            ],
        },
        {
            "id": "mafia_debt_bluff",
            "title": "전투력 0의 협박 심부름",
            "text": (
                "상납금을 미룬 하청업자를 압박하라는 지시를 받았다. "
                "유스케의 전투 능력은 거의 0에 가깝다. 덩치 큰 업자가 쇠파이프를 들고 버티고 있다."
            ),
            "choices": [
                {
                    "label": "1. 포트 마피아 보스랑 간부 이름을 대며 태연하게 협박한다.",
                    "hp_delta": -5,
                    "result": "겁을 먹은 업자가 돈을 순순히 내놓아 싸우지 않고 해결했다.",
                },
                {
                    "label": "2. \"저기, 저도 먹고살려고 이러는 거라...\" 솔직히 사정한다.",
                    "hp_delta": -25,
                    "result": "약점을 잡힌 업자에게 두들겨 맞고 간신히 도망쳤다.",
                },
            ],
        },
        {
            "id": "cough_attack",
            "title": "시한부 몸의 발작",
            "text": (
                "계단을 오르던 중 폐가 찢어질 듯한 기침이 터져 나온다. 손수건에 붉은 핏방울이 번진다."
            ),
            "choices": [
                {
                    "label": "1. 비상용 약을 삼키고 구석에서 한숨 돌린다.",
                    "hp_delta": -5,
                    "result": "고통이 조금은 가라앉았다.",
                },
                {
                    "label": "2. 무리해서 일과를 계속 소화한다.",
                    "hp_delta": -18,
                    "result": "몸 상태가 눈에 띄게 악화되었다.",
                },
            ],
        },
        {
            "id": "akane_tea",
            "title": "옥상에서의 짧은 휴식",
            "text": (
                "옥상 구석에서 아카네가 캔 커피를 마시고 있다. 마피아 안에서 유일하게 긴장을 풀 수 있는 공간이다."
            ),
            "choices": [
                {
                    "label": "1. 옆에 앉아 아무 말 없이 바람을 쐰다.",
                    "hp_delta": 15,
                    "result": "고요한 시간 속에서 지친 몸을 추슬렀다.",
                },
                {
                    "label": "2. 커피 한 캔을 얻어 마시고 바로 자리에서 일어난다.",
                    "hp_delta": 8,
                    "result": "잠깐이지만 숨을 돌릴 수 있었다.",
                },
            ],
        },
        {
            "id": "shohei_banter",
            "title": "쇼헤이의 시선",
            "text": (
                "서류 창고에서 마주친 쇼헤이가 당신을 훑어본다.\n"
                "\"야, 너 요 며칠 안색이 영 별로다? 큰 병이라도 도졌냐?\""
            ),
            "choices": [
                {
                    "label": "1. \"내 걱정이나 해, 쇼헤이. 넌 주름이 늘었네?\"",
                    "hp_delta": 0,
                    "result": "가벼운 말장난으로 자연스럽게 넘어갔다.",
                },
                {
                    "label": "2. \"응, 사실 요즘 좀 어지럽긴 해.\"",
                    "hp_delta": 10,
                    "result": "쇼헤이가 한숨을 쉬며 진통제 한 알을 던져주었다. 체력이 조금 회복됐다.",
                },
            ],
        },
        {
            "id": "rainy_yokohama",
            "title": "비 오는 요코하마 거리",
            "text": (
                "비가 쏟아지는 밤, 다리 난간 위에서 자살 기도자처럼 보이는 남자가 위태롭게 서 있다. "
                "유스케의 신조는 '자살은 권리 포기! 역겨워도 살아가라'다."
            ),
            "choices": [
                {
                    "label": "1. \"야! 죽는 것보다 사는 게 낫다고!\" 독설을 퍼부으며 끌어내린다.",
                    "hp_delta": -10,
                    "result": "비를 맞고 몸은 좀 젖었지만 사람을 한 명 살렸다.",
                },
                {
                    "label": "2. 체력을 아끼기 위해 그냥 지나친다.",
                    "hp_delta": 0,
                    "result": "조용히 발걸음을 돌려 숙소로 돌아갔다.",
                },
            ],
        },
        {
            "id": "mori_extra_meds",
            "title": "모리의 간식 타임",
            "text": (
                "모리 오가이가 영양제와 약병을 흔들며 부른다.\n"
                "\"유스케 군, 오늘도 약 타러 왔니?\""
            ),
            "choices": [
                {
                    "label": "1. \"시끄럽고 빨리 내놔, 모리 씨.\"",
                    "hp_delta": 18,
                    "result": "모리가 웃으며 약을 챙겨주어 체력이 크게 회복됐다.",
                },
                {
                    "label": "2. 기분 나빠서 째려보고 돌아선다.",
                    "hp_delta": -8,
                    "result": "약을 안 받아온 탓에 저녁 내내 컨디션이 저조했다.",
                },
            ],
        },
    ]


ENDINGS = {
    "ending_survive": {
        "title": "[생존 엔딩] 살아가는 것만으로도 수고했어!",
        "text": (
            "아슬아슬했지만 당신은 포트 마피아에서 7일을 버텨냈다.\n\n"
            "허약한 시한부 몸을 끌고 아카네와 부딪히고, 쇼헤이의 눈치를 보며, "
            "모리에게 반말을 내뱉는 살얼음판의 연속이었지만 어쨌든 오늘도 살아 있다.\n\n"
            "**\"역겹고 의미 없는 삶이라도 살아가도록 해, 죽어버리는 것보다 살아가는 것이 더 나으니까!\"**"
        ),
    },
    "ending_hp": {
        "title": "[배드 엔딩] 쓰러진 말단",
        "text": (
            "체력이 0이 되어버렸다.\n\n"
            "원래부터 허약했던 기시 유스케의 몸은 누적된 부상과 무리를 견디지 못하고 어두운 복도에 쓰러졌다. "
            "그렇게 당신의 요코하마 생존기는 막을 내렸다."
        ),
    },
}


# ---------------------------------------------------------
# 3. 상태 관리 및 진행 로직
# ---------------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def init_game():
    st.session_state.phase = "title"
    st.session_state.day = 1
    st.session_state.slot = 0
    st.session_state.hp = 100
    st.session_state.used_pool = []
    st.session_state.current_event = None
    st.session_state.last_result = None
    st.session_state.ending_key = None


def pick_event(day, slot):
    fixed = get_fixed_events()
    if (day, slot) in fixed:
        return fixed[(day, slot)]

    pool = get_pool_events()
    available = [ev for ev in pool if ev["id"] not in st.session_state.used_pool]
    if not available:
        available = pool
    chosen = random.choice(available)
    st.session_state.used_pool.append(chosen["id"])
    return chosen


def start_game():
    init_game()
    st.session_state.phase = "playing"
    st.session_state.current_event = pick_event(1, 0)


def handle_choice(choice_idx):
    ev = st.session_state.current_event
    choice = ev["choices"][choice_idx]
    delta = choice.get("hp_delta", 0)

    st.session_state.hp = clamp(st.session_state.hp + delta)

    sign = "+" if delta > 0 else ""
    st.session_state.last_result = {
        "text": choice["result"],
        "delta_text": f"체력 {sign}{delta}" if delta != 0 else "체력 변화 없음",
    }

    if st.session_state.hp <= 0:
        st.session_state.ending_key = "ending_hp"
        st.session_state.phase = "ending"
    else:
        st.session_state.phase = "result"


def next_turn():
    st.session_state.slot += 1
    if st.session_state.slot >= 3:
        st.session_state.slot = 0
        st.session_state.day += 1

    if st.session_state.day > 7:
        st.session_state.ending_key = "ending_survive"
        st.session_state.phase = "ending"
        return

    st.session_state.current_event = pick_event(
        st.session_state.day, st.session_state.slot
    )
    st.session_state.phase = "playing"


if "phase" not in st.session_state:
    init_game()


# ---------------------------------------------------------
# 4. 사이드바 (체력만 표시)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(f"### 체력 : {st.session_state.hp} / 100")
    st.progress(st.session_state.hp / 100)


# ---------------------------------------------------------
# 5. 메인 화면
# ---------------------------------------------------------
st.title("기시 유스케 빙의 생존기")

if st.session_state.phase == "title":
    intro_text = (
        "**「타살은 기회, ■■은 권리 포기! 역겹고 의미 없는 삶이라도 살아가도록 해.」**\n\n"
        "당신은 문호 스트레이 독스의 자캐 **기시 유스케**의 몸에 빙의했습니다.\n"
        "7일 동안 체력을 유지하며 무사히 살아남으세요."
    )
    st.markdown(
        f'<div class="story-box">{to_html(intro_text)}</div>',
        unsafe_allow_html=True,
    )
    st.button("눈을 뜬다", on_click=start_game, key="start_btn")

elif st.session_state.phase == "playing":
    ev = st.session_state.current_event
    st.subheader(f"{ev['title']}")
    st.markdown(
        f'<div class="story-box">{to_html(ev["text"])}</div>',
        unsafe_allow_html=True,
    )

    for idx, ch in enumerate(ev["choices"]):
        st.button(
            ch["label"],
            on_click=handle_choice,
            args=(idx,),
            key=f"choice_{st.session_state.day}_{st.session_state.slot}_{idx}",
        )

elif st.session_state.phase == "result":
    res = st.session_state.last_result
    st.markdown(
        f'<div class="story-box">{to_html(res["text"])}<br><br><span class="badge">{res["delta_text"]}</span></div>',
        unsafe_allow_html=True,
    )
    st.button("다음으로", on_click=next_turn, key="next_btn")

elif st.session_state.phase == "ending":
    if st.session_state.last_result:
        st.markdown(
            f'<div class="story-box">{to_html(st.session_state.last_result["text"])}</div>',
            unsafe_allow_html=True,
        )

    end = ENDINGS[st.session_state.ending_key]
    st.markdown(
        f'<div class="story-box"><h3>{end["title"]}</h3><hr style="border-color:#444444;">{to_html(end["text"])}</div>',
        unsafe_allow_html=True,
    )
    st.button("다시 시작하기", on_click=start_game, key="retry_btn")
