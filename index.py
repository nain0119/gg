import random
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
    padding-top: 2.5rem;
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

/* 인라인 텍스트 강조 */
.t-red { color: #cf6a6a; }
.t-gold { color: #d1b37c; }
.t-blue { color: #84a1b8; }
.t-muted { color: #9b9389; }

/* 이야기 상자 */
.story-box {
    background: var(--panel);
    border: 1px solid var(--line);
    border-left: 3px solid #6f3434;
    padding: 26px 28px;
    border-radius: 3px;
    line-height: 2.05;
    font-size: 1.01rem;
    margin: 16px 0 22px 0;
}

.story-box p {
    margin-bottom: 1.15em;
}

.story-box p:last-child {
    margin-bottom: 0;
}

/* 상단 상태 변화 로그 */
.log-strip {
    background: #1c1a18;
    border: 1px solid var(--line);
    padding: 10px 16px;
    border-radius: 3px;
    font-size: 0.9rem;
    margin-bottom: 14px;
    line-height: 1.6;
}

.section-label {
    color: #9b9389;
    font-size: 0.82rem;
    letter-spacing: 2px;
    margin-top: 14px;
    margin-bottom: 8px;
}

/* 버튼 */
div.stButton > button {
    width: 100%;
    min-height: 2.85rem;
    text-align: left;
    background: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 3px;
    padding: 10px 16px;
    font-size: 0.96rem;
    transition: 0.18s;
}

div.stButton > button:hover {
    background: #302522 !important;
    border-color: var(--accent) !important;
    color: #ffffff !important;
}

/* 게이지 */
[data-testid="stProgress"] > div > div > div > div {
    background: var(--accent) !important;
}

[data-testid="stProgress"] > div > div > div {
    background: #39322e !important;
}

hr {
    border-color: var(--line) !important;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1.8rem 1rem;
    }
    .story-box {
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)


WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

LOCATIONS = {
    "room": "말단 숙소",
    "corridor": "포트 마피아 본부 복도",
    "office": "하부 사무실",
    "clinic": "모리의 진료실",
    "cafeteria": "구내식당",
    "roof": "본부 옥상",
    "alley": "요코하마 뒷골목",
}


# -------------------------------------------------
# 1. 프롤로그 데이터 (쿠소개그물 / 현재형)
# -------------------------------------------------
PROLOGUE_SCENES = {
    "intro_1": {
        "heading": "프롤로그 — 일단 눈을 뜬다",
        "paragraphs": [
            "눈을 뜬다. 그런데 오른쪽 눈이 안 열린다. 고장 난 건가 싶어 손가락으로 꾹 눌러 보지만 여전히 암흑이다.",
            "설상가상으로 얼굴 위에는 웬 <span class='t-blue'>거무튀튀한 천 조각</span>이 덮여 있다. 숨을 들이쉴 때마다 천이 콧구멍으로 빨려 들어온다. 암살당하기 전에 질식사하기 딱 좋은 구조다.",
            "천을 걷어내고 침대에서 내려온다. 다리가 후들거린다. 발밑에 굴러다니는 알약통을 밟아 문워크를 추며 겨우 균형을 잡는다. 구석에는 책상보다 듬직해 보이는 문서 파쇄기가 전원을 켠 채 대기 중이고, 옷걸이에는 헐렁한 검은 정장이 걸려 있다."
        ],
        "next_scene": "intro_2",
        "minutes": 5,
    },
    "intro_2": {
        "heading": "프롤로그 — 대환장 스펙 확인",
        "paragraphs": [
            "세면대 거울 앞에 선다. 거울 속에는 웬 다크서클이 턱 밑까지 내려온 낯선 인간이 서 있다. 한쪽 눈은 실명이고, 체격은 바람 불면 요코하마 앞바다로 날아갈 판이다.",
            "방금 밟을 뻔한 약통, 파쇄기, 얼굴에 썼던 검은 천. 딱 봐도 포트 마피아 9년 차 말단, <span class='t-blue'>기시 유스케</span>다.",
            "대충 스펙을 훑어본다. <span class='t-red'>전투력 0. 시한부. 사방이 적. 특기는 서류 파쇄기 직행. 취미는 보스한테 반말 까기.</span> 하필이면 이 동네에서 가장 몸 약하고 친구 없는 놈 당첨이다.",
            "헛기침을 한 번 했다가 진짜로 폐가 삐걱거리며 기침 발작이 터진다. 내구도가 종잇장이다."
        ],
        "next_scene": "intro_3",
        "minutes": 5,
        "deltas": {"hp": -8, "stress": 10},
    },
    "intro_3": {
        "heading": "프롤로그 — 문 앞의 츄야(?)",
        "paragraphs": [
            "복도에서 쿵쾅거리는 발소리가 들린다. 반사적으로 세면대 옆 검은 천을 집어 머리 위에 다시 뒤집어쓴다.",
            "노크도 없이 문이 발로 차인 듯 열린다. 천 너머로 검은 모자와 주황색 머리카락이 보인다. <span class='t-red'>나카하라 츄야</span>다.",
            "물론 진짜일 확률은 낮다. <span class='t-blue'>「검은 집」</span>의 저주 때문에 천을 쓰고 남을 보면 상대가 가장 믿는 사람 얼굴로 변환되어 보인다. 즉, 포트 마피아 말단 대다수가 츄야 팬클럽이라는 소리다. 목소리를 듣기 전까진 이 녀석이 진짜 간부인지 아니면 그냥 말단 A인지 알 길이 없다.",
            "\"어이, 기시. 아직도 자빠져 자고 있냐? 모리 보스가 진료실로 기어 나오라신다. 뭘 그렇게 뻣뻣하게 서 있어? 또 꾀병 부리려고?\"",
            "눈빛이 꽤 매섭다. 9년 차 말단 유스케는 누구한테나 반말을 찍찍 내뱉는 놈이다."
        ],
        "choices": [
            {
                "label": "\"아, 시끄러워. 알아서 갈 테니까 넌 네 갈 길 가.\" (국룰 반말 시전) (0:05)",
                "next_scene": "scene_1_a",
                "minutes": 5,
                "deltas": {"stress": 4, "suspicion": -2},
            },
            {
                "label": "목소리 톤 조절에 실패할 것 같으니 입을 닫고 기침만 콜록거린다. (0:05)",
                "next_scene": "scene_1_b",
                "minutes": 5,
                "deltas": {"hp": -5, "stress": 2},
            },
            {
                "label": "\"네! 알겠습니다! 지금 바로 뛰어가겠습니다!\" (K-직장인 사회생활 모드) (0:05)",
                "next_scene": "scene_1_c",
                "minutes": 5,
                "deltas": {"stress": 12, "suspicion": 18},
            },
        ],
    },
    "scene_1_a": {
        "heading": "프롤로그 — 성공적인 어그로",
        "paragraphs": [
            "\"아, 시끄러워. 알아서 갈 거니까 넌 네 갈 길 가.\"",
            "목소리를 들어보니 진짜 츄야가 아니라 흔한 말단 A의 목소리다. 상대는 어이없다는 듯 혀를 쯧쯧 찬다.",
            "\"하, 여전히 싸가지라곤 쌈 싸 먹었네. 늦어서 보스한테 뒤져도 난 모른다.\"",
            "문이 쾅 닫힌다. <span class='t-gold'>아무래도 어그로 끌기에 성공해 의심은 안 산 모양이다.</span> 이제 밖으로 나가서 생존을 도모할 시간이다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_b": {
        "heading": "프롤로그 — 시한부 쉴드 발동",
        "paragraphs": [
            "말 대신 목을 긁어 기침을 뱉는다. 그랬더니 이 부실한 몸뚱이가 장단을 맞춰 진짜 가래 끓는 기침을 연사한다. <span class='t-red'>가슴팍이 묵직하게 울린다.</span>",
            "츄야 얼굴을 한 말단이 질색하며 뒷걸음질 친다. \"으악, 피 튀길 거면 문 닫고 기침해라! 보균자 새끼야, 시간 맞춰서 기어 나오기나 해!\"",
            "문이 쾅 닫힌다. 병약 설정 덕분에 말 한마디 안 하고 넘어갔다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_c": {
        "heading": "프롤로그 — 사회생활의 비극",
        "paragraphs": [
            "\"네! 알겠습니다! 지금 바로 뛰어가겠습니다!\"",
            "입이 자동으로 움직였다. 문 앞의 츄야 얼굴이 순식간에 정색으로 바뀐다.",
            "\"...야, 기시. 너 방금 존댓말 썼냐? 너 어디 머리 박았어?\"",
            "당황해서 급히 \"장난친 거야, 놀라는 꼴이 웃기잖아\" 하고 둘러대지만 <span class='t-red'>상대의 눈빛이 완전 '저 새끼 미쳤나' 모드다.</span> 등줄기에 식은땀이 폭포수처럼 흐른다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
}


# -------------------------------------------------
# 2. 랜덤 / 특수 이벤트 풀 (쿠소개그물 / 현재형)
# -------------------------------------------------
EVENTS = {
    "akane_bump": {
        "heading": "복도 — 스텔스 정면 충돌",
        "paragraphs": [
            "천을 뒤집어쓰고 복도를 걸어가는데, 분명 앞이 텅 비어 있었건만 <span class='t-red'>어깨끼리 쾅! 하고 정면으로 부딪혀 둘 다 바닥에 나뒹군다.</span>",
            "유사 가족 <span class='t-blue'>아카네</span>다. 아무도 안 믿는 아카네 눈엔 유스케가 대가리 없는 투명인간으로 보이고, 천을 쓴 유스케 눈엔 아카네가 스텔스 모드다. 포트 마피아 복도에서 맨날 일어나는 교통사고다.",
            "\"...아파.\" 아카네가 엉덩이를 털며 말한다. \"기시, 앞 좀 보고 다녀. 안 보이겠지만.\""
        ],
        "choices": [
            {
                "label": "\"너도 눈 뜬 장님이지? 조심 좀 해, 아카네.\"",
                "result": [
                    "아카네는 별다른 타격 없이 \"응\" 한 마디만 남기고 다시 스텔스 모드로 사라진다. 역시 서로 신경 끄는 게 제일 편하다."
                ],
                "deltas": {"hp": -3, "stress": -6, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "\"어머나! 아카네 많이 다쳤어? 파스라도 붙여줄까?\"",
                "result": [
                    "아카네가 5초간 멈춰 서서 이쪽을 뚫어져라 쳐다본다. <span class='t-red'>\"...기분 나쁘게 왜 갑자기 엄마처럼 굴어?\"</span> 스산한 눈초리가 꽂힌다."
                ],
                "deltas": {"hp": -3, "stress": 8, "suspicion": 14},
                "minutes": 10,
            },
        ],
    },
    "chuuya_hallway": {
        "heading": "복도 — 나카하라 츄야 양산 공장",
        "paragraphs": [
            "교대 시간이라 복도에 사람이 바글바글하다. 문제는 천 너머로 비치는 <span class='t-blue'>지나가는 놈들 얼굴이 100% 나카하라 츄야</span>라는 것이다.",
            "앞에도 츄야, 뒤에도 츄야, 소화기 옆에도 츄야가 서 있다. 츄야 복제 인간 전시장에 갇힌 기분이다. 그때 츄야 32호쯤 되는 인물이 어깨를 부딪치며 멈춰 선다.",
            "\"어이, 기시. 눈을 가리고 다니면 앞을 좀 살피든가.\""
        ],
        "choices": [
            {
                "label": "목소리로 짭츄야(말단)임을 간파하고 들고 있던 서류를 떠넘긴다.",
                "result": [
                    "목소리가 전형적인 말단 B의 톤이다. \"바빠 죽겠으니까 네가 대신 갖다 줘.\" 뻔뻔하게 떠넘기고 도망치자 뒤에서 쌍욕이 날아오지만 <span class='t-gold'>아무도 이상하게 보진 않는다.</span>"
                ],
                "deltas": {"stress": -4, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "혹시 찐츄야일까 봐 벽에 납작 엎드려 게걸음으로 지나간다.",
                "result": [
                    "상대가 \"뭐야 저 변태는\" 하고 혀를 찬다. 목숨은 부지했지만 멘탈이 깎인다."
                ],
                "deltas": {"stress": 6, "suspicion": 2},
                "minutes": 5,
            },
        ],
    },
    "real_chuuya": {
        "heading": "복도 — 이번엔 진짜가 나타났다",
        "paragraphs": [
            "모퉁이를 도는데 공기가 묵직하다. 아우라부터가 중력급이다. 이번엔 짭이 아니라 <span class='t-red'>100% 순도 리얼 나카하라 츄야</span>다.",
            "츄야가 미간을 사정없이 구기며 앞을 가로막는다. \"어이, 기시. 아까부터 복도에서 뭘 그렇게 흘끔거리는 거야? 기분 나쁘게.\""
        ],
        "choices": [
            {
                "label": "\"하아? 복도 전체에 네 얼굴이 복붙돼 있어서 멀미 난다고.\"",
                "result": [
                    "츄야의 주먹이 들썩이다가 '아 저 놈 능력이지' 하고 떠올린 듯 씩씩거리며 지나간다. <span class='t-gold'>한 방에 중력 가루가 될 뻔했으나 무사히 넘겼다.</span>"
                ],
                "deltas": {"stress": 10, "suspicion": -6},
                "minutes": 10,
            },
            {
                "label": "\"와, 실물이 훨씬 잘생기셨네요! 팬입니다!\"",
                "result": [
                    "그 말을 끝으로 천장이 빙글 돌더니 <span class='t-red'>벽지 무늬와 한 몸이 되어 처박힌다.</span> \"너 오늘 진짜 돌았냐?!\" 뼈는 안 부러졌으나 영혼이 탈곡당한다."
                ],
                "deltas": {"hp": -20, "stress": 20, "suspicion": 22},
                "minutes": 15,
            },
        ],
    },
    "shohei_lunch": {
        "heading": "구내식당 — 식고문의 현장",
        "paragraphs": [
            "구내식당 구석에 앉자 맞은편에 <span class='t-blue'>쇼헤이</span>가 앉는다. 투톤 머리에 한쪽 눈 실명, 거기다 겉과 속이 다른 점까지 나랑 판박이인 녀석이다.",
            "쇼헤이가 한숨을 푹 쉬더니 <span class='t-red'>화생방 훈련용 매운 마늘 카레</span>를 테이블 위로 밀어 놓는다. 이 몸은 향 강한 음식을 먹으면 영혼이 코 밖으로 빠져나가는 체질이다."
        ],
        "choices": [
            {
                "label": "\"야, 나 냄새 지독한 거 싫어하는 거 알면서 독살하려고 이러지?!\"",
                "result": [
                    "쇼헤이가 씩 웃더니 카레를 치우고 맹물 같은 흰 죽을 내민다. \"예예, 까다로우시네요.\" <span class='t-gold'>평화롭게 한 끼를 때운다.</span>"
                ],
                "deltas": {"hp": 12, "stress": -8, "suspicion": -4},
                "minutes": 30,
            },
            {
                "label": "아까우니까 코 막고 한 숟갈 크게 떠먹는다.",
                "result": [
                    "향신료가 혀에 닿자마자 <span class='t-red'>위장이 쿠데타를 일으킨다.</span> 쇼헤이가 경악하며 쳐다본다. \"너 진짜 미쳤어? 그걸 왜 먹어?\" 이후 30분간 화장실 지박령이 된다."
                ],
                "deltas": {"hp": -16, "stress": 12, "suspicion": 12},
                "minutes": 30,
            },
        ],
    },
    "dazai_alley": {
        "heading": "요코하마 뒷골목 — 수상한 붕대 거지(?)",
        "paragraphs": [
            "뒷골목을 걷다가 가로등 밑 난간에 걸터앉은 모래색 코트 사내와 마주친다. <span class='t-red'>다자이 오사무</span>다.",
            "어릴 적부터 같이 자랐으나 서로 친구 취급도 안 하는 최악의 사상 대립 관계다. 다자이가 낄낄 웃으며 손을 흔든다.",
            "\"어라? 이 죽지 못해 안달 난 기분 나쁜 기척은 유스케잖아? 오늘 항구 물 온도가 딱 좋은데, 혹시 나랑 같이 입수라도 할 생각 들었니?\""
        ],
        "choices": [
            {
                "label": "\"개소리 마, 다자이. 개똥밭에 굴러도 이승이 낫거든.\"",
                "result": [
                    "다자이가 시시하다는 듯 입을 내민다. \"흥, 여전히 재미없는 생존주의자네.\" <span class='t-gold'>역시 미친놈에겐 정면 반박이 약이다.</span>"
                ],
                "deltas": {"stress": 6, "suspicion": -10},
                "minutes": 20,
            },
            {
                "label": "\"그건 그렇고 츄야가 어제 모자 가게에서…\" 하며 츄야 뒷담화를 깐다.",
                "result": [
                    "다자이의 눈이 반짝인다. \"오, 그 꼬맹이 얘기?\" 20분 동안 신나게 츄야를 씹다가 헤어진다. 다만 다자이의 눈빛이 뭔가 꿰뚫어 보는 듯해 싸하다."
                ],
                "deltas": {"stress": 12, "suspicion": 4},
                "minutes": 20,
            },
            {
                "label": "\"사실 요즘 회사 생활 너무 빡세서 나도 좀 고민 중이야…\"",
                "result": [
                    "다자이의 표정에서 장난기가 0.1초 만에 증발한다. <span class='t-red'>\"…잠깐. 유스케가 방금 죽고 싶다는 뉘앙스를 풍겼나? 너, 안에 들어있는 게 누구지?\"</span> 식은땀을 한 바가지 쏟으며 농담이었다고 우겨 겨우 도망친다."
                ],
                "deltas": {"stress": 28, "suspicion": 32},
                "minutes": 20,
            },
        ],
    },
    "rainy_stranger": {
        "heading": "요코하마 뒷골목 — 길바닥의 행인",
        "paragraphs": [
            "비 오는 골목길에 웬 아저씨가 쓰러져 끙끙거리고 있다.",
            "원래 유스케는 남 구하다 죽은 <span class='t-blue'>'선생님'</span> 때문에 착한 사람 공포증이 있는 극단적 이기주의자다. 여기서 호구처럼 달려들었다간 체력도 날아가고 의심도 산다."
        ],
        "choices": [
            {
                "label": "\"타살은 기회, ■■은 권리 포기! 살고 싶으면 알아서 기어가라!\" 119만 눌러주고 튄다.",
                "result": [
                    "구급차 사이렌 소리가 멀리서 들려온다. 신고는 했으니 할 도리는 다 한 셈 치고 쿨하게 갈 길을 간다."
                ],
                "deltas": {"stress": 4, "suspicion": -3},
                "minutes": 15,
            },
            {
                "label": "이 몸으로 호기롭게 행인을 들쳐업고 병원까지 뛰어본다.",
                "result": [
                    "<span class='t-red'>10미터 가기도 전에 허리가 삐끗하고 기침 발작이 터져 행인 옆에 나란히 드러눕는다.</span> 구급차가 와서 둘 다 실어 갈 뻔한다."
                ],
                "deltas": {"hp": -15, "stress": -4, "suspicion": 6},
                "minutes": 35,
            },
        ],
    },
}


# -------------------------------------------------
# 3. 장소별 기본 묘사 (쿠소개그물 / 현재형)
# -------------------------------------------------
def get_time_period(minute_of_day: int) -> str:
    if 300 <= minute_of_day < 720:
        return "오전"
    elif 720 <= minute_of_day < 1080:
        return "오후"
    elif 1080 <= minute_of_day < 1320:
        return "저녁"
    else:
        return "심야"


def format_clock(minute_of_day: int) -> str:
    h = (minute_of_day // 60) % 24
    m = minute_of_day % 60
    return f"{h:02d}:{m:02d}"


def get_location_intro(loc: str, period: str, cloth_on: bool) -> list[str]:
    cloth_note = (
        "머리에 뒤집어쓴 검은 천 덕분에 세상이 선글라스 낀 것처럼 어둡다."
        if cloth_on
        else "천을 벗어 맨얼굴 상태다. 누구랑 눈 마주치면 즉시 <span class='t-blue'>「검은 집」</span> 코스프레 쇼가 개막한다."
    )

    if loc == "room":
        return [
            f"포트 마피아 9년 차 말단에게 주어진 단칸방이다. 창밖은 {period}의 요코하마 풍경이 펼쳐져 있다. 방 안엔 딱딱한 침대 하나와 애지중지 관리되는 문서 파쇄기뿐이다.",
            cloth_note,
        ]
    elif loc == "corridor":
        return [
            f"포트 마피아 본부 복도다. {period} 시간대라 군데군데 조직원들이 돌아다닌다. 여기서 다른 구역으로 이동할 수 있다.",
            "천 너머로 스쳐 지나가는 녀석들이 죄다 츄야 얼굴이라 1분마다 심장이 쫄깃하다."
            if cloth_on
            else "<span class='t-red'>맨얼굴로 복도를 배회하는 바람에 지나가는 사람마다 눈 마주칠까 봐 진땀이 난다.</span>",
        ]
    elif loc == "office":
        return [
            "월급 루팡의 성지, 하부 사무실이다. 책상 위에는 오늘 처리해야 할 서류 뭉치가 산더미처럼 쌓여 있고, 옆에서는 문서 파쇄기가 우렁차게 돌아가고 있다.",
            "주변 동료들은 내가 오늘도 서류를 갈아버릴 거라 굳게 믿고 있다."
        ]
    elif loc == "clinic":
        return [
            "보스실 옆 간이 진료실이다. 모리 오가이가 하얀 가운을 팔락거리며 생글생글 웃고 있다. 보기만 해도 수명이 줄어드는 미소다.",
            "\"어머, 유스케 군. 오늘도 안 죽고 잘 살아 있구나?\""
        ]
    elif loc == "cafeteria":
        return [
            "포트 마피아 구내식당이다. 입구부터 마늘과 카레 냄새가 진동해서 코를 막고 싶어진다.",
            f"현재 주머니 속 전 재산은 <span class='t-gold'>{st.session_state.money:,}엔</span>이다."
        ]
    elif loc == "roof":
        return [
            f"본부 옥상이다. {period}의 바닷바람이 세차게 불어온다. 마피아 건물 안에서 유일하게 이상한 놈들이 안 찾아오는 청정 구역이다.",
            "난간 밖으로 떨어지지 않게 조심하면서 숨을 돌린다."
        ]
    elif loc == "alley":
        return [
            f"본부 바깥의 요코하마 뒷골목이다. {period}이라 그런지 가로등 아래로 수상쩍은 인물들이 하나둘씩 기어 나온다.",
            cloth_note,
        ]
    return [""]


# -------------------------------------------------
# 4. 상태 초기화 및 시간/행동 처리 엔진
# -------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def init_game():
    st.session_state.mode = "prologue"
    st.session_state.scene = "intro_1"
    st.session_state.location = "room"
    st.session_state.day = 1
    st.session_state.minute_of_day = 450  # 07:30
    st.session_state.hp = 100
    st.session_state.stress = 30
    st.session_state.suspicion = 5
    st.session_state.money = 2500
    st.session_state.cloth_on = True
    st.session_state.mori_visited_today = False
    st.session_state.narrative = []
    st.session_state.feedback = []
    st.session_state.active_event = None
    st.session_state.ending_key = None


def apply_deltas(deltas: dict):
    fb = []
    if "hp" in deltas and deltas["hp"] != 0:
        d = deltas["hp"]
        st.session_state.hp = clamp(st.session_state.hp + d)
        if d > 0:
            fb.append(f"<span class='t-gold'>체력이 조금 돌아온다. (체력 +{d})</span>")
        else:
            fb.append(f"<span class='t-red'>체력이 깎인다. (체력 {d})</span>")

    if "stress" in deltas and deltas["stress"] != 0:
        d = deltas["stress"]
        st.session_state.stress = clamp(st.session_state.stress + d)
        if d > 0:
            fb.append(f"<span class='t-red'>혈압이 오른다. (스트레스 +{d})</span>")
        else:
            fb.append(f"<span class='t-gold'>멘탈이 진정된다. (스트레스 {d})</span>")

    if "suspicion" in deltas and deltas["suspicion"] != 0:
        d = deltas["suspicion"]
        st.session_state.suspicion = clamp(st.session_state.suspicion + d)
        if d > 0:
            fb.append(f"<span class='t-red'>주변에서 이상한 놈 보듯 쳐다본다. (의심 +{d})</span>")
        else:
            fb.append(f"<span class='t-blue'>완벽한 기시 유스케로 인정받는다. (의심 {d})</span>")

    if "money" in deltas and deltas["money"] != 0:
        d = deltas["money"]
        st.session_state.money = max(0, st.session_state.money + d)
        if d > 0:
            fb.append(f"<span class='t-gold'>{d:,}엔을 줍는다.</span>")
        else:
            fb.append(f"<span class='t-muted'>{abs(d):,}엔이 털린다.</span>")

    return fb


def advance_time(minutes: int):
    st.session_state.minute_of_day += minutes
    extra_fb = []
    while st.session_state.minute_of_day >= 1440:
        st.session_state.minute_of_day -= 1440
        st.session_state.day += 1
        if not st.session_state.mori_visited_today:
            st.session_state.hp = clamp(st.session_state.hp - 12)
            st.session_state.stress = clamp(st.session_state.stress + 8)
            extra_fb.append("<span class='t-red'>진료 땡땡이친 대가로 자고 일어나니 몸이 두드려 맞은 것 같다.</span>")
        else:
            st.session_state.hp = clamp(st.session_state.hp - 5)
        st.session_state.mori_visited_today = False
    return extra_fb


def check_status_triggers():
    if st.session_state.hp <= 0:
        st.session_state.ending_key = "ending_hp"
        st.session_state.mode = "ending"
        return True
    if st.session_state.suspicion >= 100:
        st.session_state.ending_key = "ending_caught"
        st.session_state.mode = "ending"
        return True
    if st.session_state.day > 7:
        st.session_state.ending_key = "ending_survive"
        st.session_state.mode = "ending"
        return True

    # 스트레스 100 도달 시 기절
    if st.session_state.stress >= 100:
        st.session_state.stress = 55
        st.session_state.hp = clamp(st.session_state.hp - 18)
        st.session_state.suspicion = clamp(st.session_state.suspicion + 10)
        st.session_state.location = "clinic"
        st.session_state.mori_visited_today = True
        advance_time(120)
        st.session_state.narrative = [
            "<span class='t-red'>스트레스 게이지가 폭발해 거품 물고 그대로 바닥에 쓰러진다.</span>",
            "2시간 뒤, 눈을 뜨자 모리 진료실 천장이 보인다. 옆에는 모리 오가이가 특유의 능글맞은 미소로 주사기를 흔들고 있다.",
            "\"어머나, 유스케 군. 오늘도 장렬하게 기절했구나?\""
        ]
        st.session_state.feedback = [
            "<span class='t-red'>스트레스 100 달성으로 2시간 뒤 모리의 진료실에서 리스폰된다.</span>"
        ]
        st.session_state.mode = "roam"
        if st.session_state.hp <= 0:
            st.session_state.ending_key = "ending_hp"
            st.session_state.mode = "ending"
        return True
    return False


# -------------------------------------------------
# 5. 콜백 함수
# -------------------------------------------------
def step_prologue(next_key, minutes, deltas, enter_roam=False):
    fb = apply_deltas(deltas or {})
    fb += advance_time(minutes)
    st.session_state.feedback = fb

    if enter_roam:
        st.session_state.mode = "roam"
        st.session_state.location = "room"
        st.session_state.narrative = [
            "프롤로그 끝. 일단 방에서 나가 모리 약을 타 먹든, 서류를 갈아버리든, 7일간 살아남아야 한다."
        ]
    else:
        st.session_state.scene = next_key
    check_status_triggers()


def move_location(target_loc: str, minutes: int):
    fb = advance_time(minutes)
    st.session_state.location = target_loc
    st.session_state.feedback = fb

    if check_status_triggers():
        return

    roll = random.random()
    period = get_time_period(st.session_state.minute_of_day)

    if target_loc == "corridor" and roll < 0.45:
        ev_key = random.choices(
            ["akane_bump", "chuuya_hallway", "real_chuuya"],
            weights=[40, 45, 15],
        )[0]
        st.session_state.active_event = EVENTS[ev_key]
        st.session_state.mode = "event"
        return

    if target_loc == "alley" and roll < 0.55:
        if period in ("저녁", "심야") and random.random() < 0.55:
            st.session_state.active_event = EVENTS["dazai_alley"]
        else:
            st.session_state.active_event = EVENTS["rainy_stranger"]
        st.session_state.mode = "event"
        return

    if target_loc == "cafeteria" and roll < 0.45:
        st.session_state.active_event = EVENTS["shohei_lunch"]
        st.session_state.mode = "event"
        return

    st.session_state.narrative = get_location_intro(
        target_loc, period, st.session_state.cloth_on
    )


def do_action(action_id: str):
    fb = []
    nar = []
    minutes = 15

    if action_id == "rest_room":
        minutes = 60
        nar = [
            "침대에 대자로 뻗어 천을 벗어 던지고 1시간 동안 숙면을 취한다. <span class='t-gold'>최고의 복지다.</span>"
        ]
        fb += apply_deltas({"hp": 14, "stress": -18})

    elif action_id == "mirror_practice":
        minutes = 15
        st.session_state.cloth_on = False
        nar = [
            "거울을 보며 \"보쿠~\" 하고 느끼한 목소리 톤을 연습한다. <span class='t-blue'>어쩐지 양치기 소년 연기가 꽤 그럴듯해졌다.</span>"
        ]
        fb += apply_deltas({"stress": -4, "suspicion": -6})

    elif action_id == "toggle_cloth":
        minutes = 5
        st.session_state.cloth_on = not st.session_state.cloth_on
        if st.session_state.cloth_on:
            nar = ["머리에 검은 천을 다시 뒤집어쓴다. 시야가 절반으로 줄어들며 안전한 암흑 모드가 켜진다."]
        else:
            nar = ["답답한 천을 벗는다. <span class='t-red'>이제 남이랑 눈 마주치면 자동 변신 이벤트가 터진다.</span>"]

    elif action_id == "shred_papers":
        minutes = 25
        nar = [
            "서류를 보자마자 1초의 망설임도 없이 파쇄기에 풀 가동으로 처넣는다. 위이이잉—! 종이 가루가 눈처럼 쏟아진다.",
            "옆자리 말단이 감동한 눈빛으로 박수를 친다. \"역시 9년 차 대선배님! 변함없으시군요!\" <span class='t-gold'>일을 조졌는데 오히려 수당으로 400엔이 들어온다.</span>"
        ]
        fb += apply_deltas({"stress": -8, "suspicion": -10, "money": 400})

    elif action_id == "work_papers":
        minutes = 40
        nar = [
            "정상인처럼 서류를 분류해 결재판에 끼워 올린다. 상급자가 서류를 보자마자 기겁하며 뒷걸음질 친다.",
            "\"...너 뭐야, 쿠데타 준비하냐? 왜 갑자기 일을 해?!\" 일당 1,200엔은 챙겼지만 <span class='t-red'>사무실 전체가 이쪽을 경계하기 시작한다.</span>"
        ]
        fb += apply_deltas({"hp": -6, "stress": 12, "suspicion": 16, "money": 1200})

    elif action_id == "mori_rude":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"모리 씨, 면상 보니까 수명 3년은 깎이는 것 같은데 약이나 내놔.\"",
            "모리가 함박웃음을 지으며 특제 영양 주사를 놔준다. \"아하하! 오늘도 기운이 팔팔해서 보기 좋구나!\" <span class='t-gold'>패드립 수준의 반말 덕분에 체력이 쭉쭉 오른다.</span>"
        ]
        fb += apply_deltas({"hp": 25, "stress": 4, "suspicion": -8})

    elif action_id == "mori_polite":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"보스님! 오늘도 만수무강하십시오! 약 잘 먹겠습니다!\"",
            "모리의 웃음이 싹 사라지고 손에 든 메스가 번쩍인다. <span class='t-red'>\"...유스케 군? 방금 나한테 보스님이라고 했니? 해부 좀 해볼까?\"</span> 약은 얻었지만 지하실행 티켓에 한 발짝 가까워졌다."
        ]
        fb += apply_deltas({"hp": 12, "stress": 18, "suspicion": 24})

    elif action_id == "eat_bland":
        minutes = 25
        if st.session_state.money >= 500:
            nar = [
                "향신료 냄새를 피해 500엔짜리 맹물 흰 죽을 시켜 먹는다. 맛은 없지만 속이 편안하다."
            ]
            fb += apply_deltas({"hp": 16, "stress": -10, "money": -500})
        else:
            nar = ["주머니를 털어 봐도 500엔이 없다. <span class='t-muted'>서류라도 갈아서 돈 벌어 와야 한다.</span>"]
            minutes = 5

    elif action_id == "roof_breeze":
        minutes = 30
        nar = [
            "옥상 난간에 기대 요코하마 바닷바람을 쐰다. <span class='t-gold'>미친 마피아 본부 안에서 유일하게 제정신을 유지할 수 있는 시간이다.</span>"
        ]
        fb += apply_deltas({"stress": -22, "hp": 3})

    elif action_id == "alley_walk":
        minutes = 30
        nar = [
            "요코하마 뒷골목을 어슬렁거리며 도주 경로를 물색한다. 물론 이 저질 체력으론 50미터 뛰면 방전될 게 뻔하다."
        ]
        fb += apply_deltas({"hp": -4, "stress": -10})

    fb += advance_time(minutes)
    st.session_state.feedback = fb
    st.session_state.narrative = nar
    check_status_triggers()


def resolve_event_choice(idx: int):
    ev = st.session_state.active_event
    ch = ev["choices"][idx]
    fb = apply_deltas(ch.get("deltas", {}))
    fb += advance_time(ch.get("minutes", 10))
    st.session_state.feedback = fb
    st.session_state.narrative = ch["result"]
    st.session_state.mode = "event_result"
    check_status_triggers()


def finish_event_result():
    period = get_time_period(st.session_state.minute_of_day)
    st.session_state.narrative = get_location_intro(
        st.session_state.location, period, st.session_state.cloth_on
    )
    st.session_state.active_event = None
    st.session_state.mode = "roam"


# -------------------------------------------------
# 6. 엔딩 텍스트 (쿠소개그물 / 현재형)
# -------------------------------------------------
ENDINGS = {
    "ending_survive": {
        "heading": "생존 엔딩 — 어찌저찌 일주일 버팀",
        "paragraphs": [
            "놀랍게도 7일 동안 안 죽고 안 들키고 버텨낸다.",
            "여전히 복도에 나가면 온 세상이 츄야로 보이고, 서류는 파쇄기에 처넣으며, 보스한테 반말을 까야 약을 받는 기상천외한 삶이지만 어쨌든 숨은 붙어 있다.",
            "<span class='t-gold'>\"살아가는 것만으로도 수고했어! 역겹고 의미 없어도 일단 살아 있으니 개이득이다.\"</span>"
        ],
    },
    "ending_hp": {
        "heading": "배드 엔딩 — 내구도 소진",
        "paragraphs": [
            "전투력 0의 시한부 몸뚱이가 결국 체력 0을 찍고 로그아웃한다.",
            "<span class='t-red'>복도 한복판에서 쿨럭거리다 그대로 바닥과 물아일체가 된다.</span> 요코하마 생존기 完."
        ],
    },
    "ending_caught": {
        "heading": "배드 엔딩 — 정체 발각(지하실 1열)",
        "paragraphs": [
            "의심 수치 100 달성. 너무 착하게 굴었거나 존댓말을 너무 많이 쓴 모양이다.",
            "방문이 벌컥 열리더니 모리 오가이와 다자이 오사무가 동시에 씩 웃으며 걸어 들어온다.",
            "<span class='t-red'>\"자, 유스케 탈을 쓴 낯선 손님? 지하실 구경 좀 시켜줄까?\"</span> 그대로 사이좋게 손잡고 지하 심문실로 연행된다."
        ],
    },
}


if "mode" not in st.session_state:
    init_game()


# -------------------------------------------------
# 7. 사이드바 HUD
# -------------------------------------------------
weekday_str = WEEKDAYS[(st.session_state.day - 1) % 7]
clock_str = format_clock(st.session_state.minute_of_day)
period_str = get_time_period(st.session_state.minute_of_day)
loc_name = LOCATIONS[st.session_state.location] if st.session_state.mode != "prologue" else "말단 숙소"

with st.sidebar:
    st.subheader("STATUS")
    st.markdown(
        f"<p style='margin-bottom:4px;'><b>{st.session_state.day}일차 · {weekday_str}</b></p>"
        f"<p style='color:#9b9389; font-size:0.9rem; margin-bottom:10px;'>{clock_str} ({period_str}) · {loc_name}</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    st.write(f"체력 : {st.session_state.hp} / 100")
    st.progress(st.session_state.hp / 100)

    st.write(f"스트레스 : {st.session_state.stress} / 100")
    st.progress(st.session_state.stress / 100)

    st.write(f"의심 : {st.session_state.suspicion} / 100")
    st.progress(st.session_state.suspicion / 100)

    st.divider()

    cloth_txt = "착용 중 (시야 왜곡)" if st.session_state.cloth_on else "벗음 (변신 위험)"
    st.caption(f"천 상태 : {cloth_txt}")
    st.caption(f"소지금 : {st.session_state.money:,}엔")
    st.caption("PORT MAFIA / SURVIVAL RECORD")

    st.write("")
    st.button("처음부터 다시", on_click=init_game, key="sidebar_reset")


# -------------------------------------------------
# 8. 메인 화면 렌더링
# -------------------------------------------------
st.markdown(
    '<p style="color:#b56c65; letter-spacing:4px; font-size:12px;">'
    'PORT MAFIA  /  PERSONAL RECORD</p>',
    unsafe_allow_html=True
)
st.title("기시 유스케 생존 기록")
st.markdown(
    f'<p style="color:#9b9389;">요코하마 · {loc_name}</p>',
    unsafe_allow_html=True
)
st.divider()

# [A] 프롤로그 모드
if st.session_state.mode == "prologue":
    sc = PROLOGUE_SCENES[st.session_state.scene]
    st.markdown(f"### {sc['heading']}")

    if st.session_state.feedback:
        fb_html = "<br>".join(st.session_state.feedback)
        st.markdown(f'<div class="log-strip">{fb_html}</div>', unsafe_allow_html=True)

    p_html = "".join(f"<p>{p}</p>" for p in sc["paragraphs"])
    st.markdown(f'<div class="story-box">{p_html}</div>', unsafe_allow_html=True)

    if "choices" in sc:
        for idx, ch in enumerate(sc["choices"]):
            st.button(
                ch["label"],
                on_click=step_prologue,
                args=(ch["next_scene"], ch["minutes"], ch.get("deltas"), False),
                key=f"pro_ch_{st.session_state.scene}_{idx}",
            )
    else:
        st.button(
            "다음으로",
            on_click=step_prologue,
            args=(
                sc.get("next_scene"),
                sc.get("minutes", 5),
                sc.get("deltas"),
                sc.get("enter_roam", False),
            ),
            key=f"pro_next_{st.session_state.scene}",
        )

# [B] 이벤트 인카운터 모드
elif st.session_state.mode == "event":
    ev = st.session_state.active_event
    st.markdown(f"### {ev['heading']}")

    p_html = "".join(f"<p>{p}</p>" for p in ev["paragraphs"])
    st.markdown(f'<div class="story-box">{p_html}</div>', unsafe_allow_html=True)

    for idx, ch in enumerate(ev["choices"]):
        st.button(
            ch["label"],
            on_click=resolve_event_choice,
            args=(idx,),
            key=f"ev_ch_{idx}",
        )

# [C] 이벤트 결과 확인 모드
elif st.session_state.mode == "event_result":
    ev = st.session_state.active_event
    st.markdown(f"### {ev['heading']}")

    if st.session_state.feedback:
        fb_html = "<br>".join(st.session_state.feedback)
        st.markdown(f'<div class="log-strip">{fb_html}</div>', unsafe_allow_html=True)

    p_html = "".join(f"<p>{p}</p>" for p in st.session_state.narrative)
    st.markdown(f'<div class="story-box">{p_html}</div>', unsafe_allow_html=True)

    st.button("계속한다", on_click=finish_event_result, key="ev_done")

# [D] 자유 행동 및 이동 모드
elif st.session_state.mode == "roam":
    loc = st.session_state.location
    st.markdown(f"### {LOCATIONS[loc]}")

    if st.session_state.feedback:
        fb_html = "<br>".join(st.session_state.feedback)
        st.markdown(f'<div class="log-strip">{fb_html}</div>', unsafe_allow_html=True)

    p_html = "".join(f"<p>{p}</p>" for p in st.session_state.narrative)
    st.markdown(f'<div class="story-box">{p_html}</div>', unsafe_allow_html=True)

    # 현재 위치의 행동
    st.markdown('<p class="section-label">행동</p>', unsafe_allow_html=True)
    if loc == "room":
        st.button("침대에 대자로 뻗어 숙면한다 (1:00)", on_click=do_action, args=("rest_room",), key="act_rest")
        st.button("거울 앞에서 '보쿠' 말투를 연습한다 (0:15)", on_click=do_action, args=("mirror_practice",), key="act_mirror")
        cloth_btn_lbl = "얼굴을 덮은 천을 벗는다 (0:05)" if st.session_state.cloth_on else "얼굴에 천을 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_r")

    elif loc == "corridor":
        cloth_btn_lbl = "천을 살짝 걷어 본다 (0:05)" if st.session_state.cloth_on else "천을 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_c")

    elif loc == "office":
        st.button("서류 뭉치를 파쇄기에 통째로 갈아버린다 (0:25)", on_click=do_action, args=("shred_papers",), key="act_shred")
        st.button("정상인처럼 서류를 분류해 결재를 올린다 (0:40)", on_click=do_action, args=("work_papers",), key="act_work")

    elif loc == "clinic":
        st.button("모리에게 반말로 약을 요구한다 (0:20)", on_click=do_action, args=("mori_rude",), key="act_mori_r")
        st.button("모리에게 깍듯하게 인사하고 약을 받는다 (0:20)", on_click=do_action, args=("mori_polite",), key="act_mori_p")

    elif loc == "cafeteria":
        st.button("맹물 같은 흰 죽을 사 먹는다 · 500엔 (0:25)", on_click=do_action, args=("eat_bland",), key="act_eat")

    elif loc == "roof":
        st.button("난간에 기대 요코하마의 바닷바람을 쐰다 (0:30)", on_click=do_action, args=("roof_breeze",), key="act_roof")

    elif loc == "alley":
        st.button("도주 경로를 물색하며 뒷골목을 걷는다 (0:30)", on_click=do_action, args=("alley_walk",), key="act_alley")

    # 이동 구역
    st.markdown('<p class="section-label">이동</p>', unsafe_allow_html=True)
    if loc != "corridor":
        st.button("포트 마피아 본부 복도로 나간다 (0:05)", on_click=move_location, args=("corridor", 5), key="mv_corr")
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.button("말단 숙소로 돌아간다 (0:05)", on_click=move_location, args=("room", 5), key="mv_room")
            st.button("하부 사무실로 간다 (0:05)", on_click=move_location, args=("office", 5), key="mv_off")
            st.button("모리의 진료실로 간다 (0:10)", on_click=move_location, args=("clinic", 10), key="mv_cli")
        with col2:
            st.button("구내식당으로 간다 (0:05)", on_click=move_location, args=("cafeteria", 5), key="mv_caf")
            st.button("본부 옥상으로 올라간다 (0:10)", on_click=move_location, args=("roof", 10), key="mv_roof")
            st.button("본부 밖, 요코하마 뒷골목으로 나간다 (0:15)", on_click=move_location, args=("alley", 15), key="mv_alley")

# [E] 엔딩 모드
elif st.session_state.mode == "ending":
    end = ENDINGS[st.session_state.ending_key]
    st.markdown(f"### {end['heading']}")

    p_html = "".join(f"<p>{p}</p>" for p in end["paragraphs"])
    st.markdown(f'<div class="story-box">{p_html}</div>', unsafe_allow_html=True)

    st.button("처음부터 다시 시작하기", on_click=init_game, key="end_reset")
