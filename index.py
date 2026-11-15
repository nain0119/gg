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
# 1. 프롤로그 데이터 (현재형, 속마음 서술 배제)
# -------------------------------------------------
PROLOGUE_SCENES = {
    "intro_1": {
        "heading": "도입 — 낯선 숨결",
        "paragraphs": [
            "차가운 소독약 냄새가 코끝을 찌른다. 알코올과 오래된 종이, 축축한 콘크리트 냄새가 뒤섞여 숨을 들이쉴 때마다 목 안쪽이 칼칼하다. 귓가에는 낡은 형광등이 미세하게 떨리며 내는 낮은 전류음만 울린다.",
            "천천히 눈꺼풀을 밀어 올린다. 한쪽 눈은 아예 열리지 않는 것처럼 시야의 절반이 새까만 어둠에 잠겨 있다. 남은 한쪽 눈마저 흐릿하다. 얼굴 위로 <span class='t-blue'>얇고 어두운 천</span>이 드리워져 있어, 숨을 쉴 때마다 입술 근처에서 천이 미세하게 들썩거린다.",
            "상체를 일으키려 하자 <span class='t-red'>가슴 깊은 곳에서 쇳소리 섞인 기침이 터져 나온다.</span> 폐가 좁아진 것처럼 호흡이 얕고 거칠다. 겨우 몸을 세워 침대 가장자리에 걸터앉는 순간 시야가 한쪽으로 기운다. 매트리스 시트를 쥔 손이 가늘고 핏기 없이 희다. 손목의 굵기도, 손가락의 길이도 본래의 것이 아니다.",
            "떨리는 손끝으로 얼굴을 덮고 있던 천을 걷어 올린다. 서늘한 공기가 뺨에 닿는다. 방 안은 좁고 단조롭다. 벽에 걸린 구겨진 검은 정장, 구석에 놓인 문서 파쇄기, 철제 책상 위에 굴러다니는 라벨 없는 하얀 약병들. 장판의 한기와 혀끝에 감도는 비릿한 쇳내가 뚜렷하다."
        ],
        "next_scene": "intro_2",
        "minutes": 5,
    },
    "intro_2": {
        "heading": "도입 — 거울 속의 타인",
        "paragraphs": [
            "비틀거리며 작은 세면대 앞까지 걸어가 벽에 붙은 거울을 마주 본다. 거울 너머에 서 있는 인물은 전혀 낯선 얼굴이다.",
            "핏기 없는 창백한 피부에 마른 체격, 낯선 윤곽의 짧은 머리카락. 한쪽 눈은 빛을 잃은 채 어둡고 공허하게 비어 있고, 남은 한쪽 눈이 거울 밖을 응시한다. 손을 들어 뺨에 대자 거울 속의 인물도 똑같이 움직인다.",
            "얼굴을 가리던 검은 천, 실명한 한쪽 눈, 방 구석의 문서 파쇄기와 약병들. 눈앞의 단서들이 하나의 이름과 겹친다. <span class='t-blue'>기시 유스케.</span>",
            "요코하마의 포트 마피아에 소속된 9년 차 말단 조직원. <span class='t-red'>전투 능력이 전무하고 시한부의 몸을 끌며 사방에 적을 둔 채, 보스인 모리 오가이에게도 반말을 쓰는 인물이다.</span>",
            "호흡이 급격히 빨라진다. 좁은 흉곽이 조여 들며 다시 한번 거친 기침이 쏟아진다. 입을 막았던 손등에 열기와 얕은 습기가 남는다. 양손이 세면대 모서리를 세게 움켜쥔다."
        ],
        "next_scene": "intro_3",
        "minutes": 5,
        "deltas": {"hp": -8, "stress": 12},
    },
    "intro_3": {
        "heading": "도입 — 문 너머의 발소리",
        "paragraphs": [
            "복도 저편에서 규칙적인 구둣발 소리가 가까워진다. 반사적으로 세면대 옆에 떨어져 있던 검은 천을 집어 들어 머리 위로 뒤집어쓴다. 심장이 갈비뼈 안쪽을 두드리며 귀울림을 일으킨다.",
            "발소리가 방문 바로 앞에서 멈춘다. 짧은 정적 뒤, 노크 없이 문고리가 거칠게 돌아간다. 끼익, 하고 문이 열리며 복도의 불빛이 방 안으로 길게 들어온다.",
            "누군가 문턱에 선다. 천 너머로 비치는 상대의 윤곽을 바라본다. 검은 모자, 주황빛 머리카락, 날카롭게 찌푸린 미간. 포트 마피아의 간부, <span class='t-red'>나카하라 츄야</span>의 모습이다.",
            "이능력 <span class='t-blue'>「검은 집」</span>은 천 너머로 상대를 볼 때도 작용한다. 천에 가려진 상태에서 상대를 보면, 실제 모습이 아니라 상대방이 가장 신뢰하는 인물의 얼굴로 보인다. 포트 마피아 말단 대다수가 가장 믿는 사람은 츄야다. 눈앞의 인물이 평범한 조직원인지, 진짜 나카하라 츄야인지는 겉모습만으로 알 수 없다.",
            "\"어이, 기시. 아직도 자빠져 자고 있냐?\" 상대가 문틀에 기대며 퉁명스럽게 말한다. \"모리 보스께서 진료 시간 늦지 말라고 전하라더라. 근데 넌 뭘 그렇게 멍하니 서 있어? 또 어디 아픈 척 꾀병 부리려는 건 아니지?\"",
            "목소리에 날이 서 있다. 마피아 9년 차인 기시 유스케는 누구에게나 반말을 쓴다. 입안이 바짝 마른 채 방 한가운데에 서서 상대를 마주한다."
        ],
        "choices": [
            {
                "label": "\"...아, 시끄러워.\" 목을 가다듬고 반말로 퉁명스럽게 받아친다. (0:05)",
                "next_scene": "scene_1_a",
                "minutes": 5,
                "deltas": {"stress": 4, "suspicion": -2},
            },
            {
                "label": "입을 열지 않고 거친 기침으로 대답을 대신한다. (0:05)",
                "next_scene": "scene_1_b",
                "minutes": 5,
                "deltas": {"hp": -5, "stress": 2},
            },
            {
                "label": "고개를 숙이며 공손한 어조로 대답한다. (0:05)",
                "next_scene": "scene_1_c",
                "minutes": 5,
                "deltas": {"stress": 12, "suspicion": 18},
            },
        ],
    },
    "scene_1_a": {
        "heading": "도입 — 어설픈 가면",
        "paragraphs": [
            "천 아래에서 이를 악물고 목에 힘을 준다. 목소리가 갈라지지 않도록 낮고 건조한 어조를 내뱉는다.",
            "\"...아, 시끄러워. 알아서 갈 거니까 남의 방 앞에서 떠들지 말고 너나 잘해.\"",
            "이 몸의 성대가 본래 그 말투에 익숙한 듯 자연스럽게 음성이 흘러나온다. 문 앞의 사내—츄야가 아니라 낯선 말단 조직원의 목소리다—가 어이없다는 듯 혀를 찬다.",
            "\"하, 여전히 싸가지라곤 눈 씻고 찾아볼 수가 없네. 늦어서 보스한테 뒤져도 난 모른다.\"",
            "쾅, 하고 문이 닫힌다. 발소리가 복도 끝으로 멀어진 뒤, 다리의 힘이 풀리며 침대 위로 주저앉는다. 천 안쪽에 식은땀이 배어 있다. <span class='t-gold'>상대는 별다른 의심 없이 물러간다.</span>",
            "방 안에는 다시 정적이 내려앉는다. 문 너머에서 오늘 하루를 버텨야 한다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_b": {
        "heading": "도입 — 침묵과 기침",
        "paragraphs": [
            "입을 다문 채 고개를 비스듬히 돌리고 목 안쪽을 긁어 기침을 내뱉는다. 아까의 현기증과 겹쳐 진짜로 가래 끓는 기침이 연달아 터져 나온다. <span class='t-red'>가슴께가 묵직하게 욱신거린다.</span>",
            "문 앞의 인물이 미간을 구기며 한 걸음 물러선다. 츄야의 얼굴을 한 조직원이 인상을 찌푸리며 중얼거린다.",
            "\"...하여튼 병약한 새끼, 피 튀길 거면 문 닫고 기침해라. 귀찮게 옮기지 말고. 시간 맞춰서 진료실로 기어 나와.\"",
            "상대는 짜증 섞인 한숨을 내쉬며 문을 닫고 사라진다. 가슴의 통증은 남았지만, 상대는 그저 평소와 다름없는 기시 유스케로 받아들이고 자리를 뜬다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_c": {
        "heading": "도입 — 미끄러진 말투",
        "paragraphs": [
            "\"아, 죄송합니다! 지금 바로 준비해서 가겠습니다!\"",
            "목소리가 방 안에 울리자마자 공기가 싸늘하게 식는다. 문 앞의 사내가 미간을 깊게 찌푸리며 방 안으로 한 걸음 들어선다. 천 너머로 비치는 츄야의 얼굴이 서늘하게 굳는다.",
            "\"...야, 기시. 너 방금 뭐라고 했냐?\"",
            "뒷걸음질 치며 급히 비아냥거리는 어조를 쥐어짜 내뱉는다. \"아, 아니, 장난친 거라고. 놀라는 꼴이 웃기잖아.\" 그러나 9년 동안 한 번도 존댓말을 쓴 적 없는 유스케의 태도에 <span class='t-red'>상대의 눈빛에 짙은 의구심이 스민다.</span>",
            "\"...이상한 놈. 정신 나간 거 아니면 빨리 나오기나 해.\"",
            "문이 닫힌 뒤에도 등줄기로 식은땀이 흘러내린다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
}


# -------------------------------------------------
# 2. 랜덤 / 특수 이벤트 풀 (현재형, 속마음 서술 배제)
# -------------------------------------------------
EVENTS = {
    "akane_bump": {
        "heading": "복도 — 보이지 않는 충돌",
        "paragraphs": [
            "천을 쓴 채 복도 모퉁이를 도는 순간이다. 한쪽 눈으로 본 복도 앞은 비어 있었으나, <span class='t-red'>둔탁한 충격과 함께 누군가의 어깨에 정면으로 부딪히며 바닥에 나뒹군다.</span>",
            "주저앉아 천을 고쳐 잡는다. 맞은편에서 먼지를 털고 일어서는 인물은 모리의 집에서 함께 자란 유사 가족, <span class='t-blue'>아카네</span>다.",
            "아무도 믿지 못하는 아카네의 시선에는 유스케의 머리가 보이지 않고, 천을 쓴 유스케의 눈에도 아카네가 보이지 않는다. 두 사람은 마주칠 때마다 자주 이렇게 부딪힌다.",
            "\"...아파.\" 아카네가 무덤덤한 목소리로 말한다. \"기시, 앞 좀 보고 걸어. 어차피 안 보이겠지만.\""
        ],
        "choices": [
            {
                "label": "\"너도 안 보이긴 마찬가지잖아. 조심 좀 해, 아카네.\"",
                "result": [
                    "무심하게 대꾸하자 아카네는 별말 없이 고개를 한 번 끄덕이고는 복도 저편으로 걸어간다. 유스케에게 별다른 관심이 없는 태도 그대로다."
                ],
                "deltas": {"hp": -3, "stress": -6, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "\"미안! 많이 다쳤어? 부딪힌 데는 없고?\"",
                "result": [
                    "아카네의 걸음이 우뚝 멈춘다. 아카네는 한동안 아무 말 없이 이쪽을 바라보다가 낮게 중얼거린다. <span class='t-red'>\"...기분 나쁘게 왜 갑자기 상냥한 척해?\"</span> 그 시선이 꽤 오래 머문다."
                ],
                "deltas": {"hp": -3, "stress": 8, "suspicion": 14},
                "minutes": 10,
            },
        ],
    },
    "chuuya_hallway": {
        "heading": "복도 — 겹쳐지는 얼굴들",
        "paragraphs": [
            "교대 시간과 겹쳐 복도에 포트 마피아 조직원들이 많이 오간다. 천 너머로 보이는 <span class='t-blue'>지나가는 사람들의 얼굴이 전부 나카하라 츄야</span>로 비친다.",
            "앞을 봐도 츄야, 뒤를 돌아봐도 츄야의 모습뿐이다. 그때 맞은편에서 걸어오던 한 인물이 어깨를 스치며 걸음을 멈춘다.",
            "\"어이, 기시. 눈을 가리고 다니면 앞을 좀 살피든가.\""
        ],
        "choices": [
            {
                "label": "목소리로 말단임을 확인하고, 들고 있던 심부름 봉투를 떠넘긴다.",
                "result": [
                    "음성의 높낮이는 간부가 아닌 하급 조직원의 것이다. \"바쁘니까 네가 대신 전해.\" 봉투를 안기고 돌아서자 뒤에서 욕설이 날아오지만, <span class='t-gold'>아무도 이쪽 행동을 수상히 여기지 않는다.</span>"
                ],
                "deltas": {"stress": -4, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "고개만 살짝 숙이고 빠르게 옆을 지나친다.",
                "result": [
                    "상대가 \"뭐야 저 기분 나쁜 놈은\" 하고 중얼거리지만 붙잡지는 않는다. 호흡이 조금 빨라진다."
                ],
                "deltas": {"stress": 6, "suspicion": 2},
                "minutes": 5,
            },
        ],
    },
    "real_chuuya": {
        "heading": "복도 — 진짜 나카하라 츄야",
        "paragraphs": [
            "복도 모퉁이를 도는 순간 공기의 무게가 달라진다. 그동안 복도에 비치던 허상들과 달리 날카로운 위압감이 정면에서 꽂힌다. 검은 모자 아래로 뻗은 주황빛 머리카락. <span class='t-red'>진짜 나카하라 츄야</span>다.",
            "유스케가 모리 다음으로 싫어하고, 츄야 역시 불쾌하게 여기는 상대다. 츄야가 노골적으로 인상을 구기며 앞을 가로막는다.",
            "\"어이, 기시. 아까부터 복도에서 어슬렁거리면서 뭘 그렇게 흘끔거리는 거야?\""
        ],
        "choices": [
            {
                "label": "\"하아? 여기 사방에 네 얼굴이 널려 있어서 토 나올 것 같다고.\"",
                "result": [
                    "츄야의 관자놀이에 핏줄이 선다. \"뭐, 뭐라고 이 자식이...?!\" 금방이라도 주먹을 휘두를 듯하지만, 곧 이능력 탓임을 떠올린 듯 거칠게 혀를 차며 지나간다. <span class='t-gold'>츄야는 불쾌한 기색을 남긴 채 시선을 거둔다.</span>"
                ],
                "deltas": {"stress": 10, "suspicion": -6},
                "minutes": 10,
            },
            {
                "label": "\"아, 아니요! 아무것도 안 봤습니다. 먼저 가겠습니다!\"",
                "result": [
                    "츄야의 걸음이 멈추고, 멱살이 잡힌 채 벽에 밀어붙여진다. <span class='t-red'>\"...너 오늘 왜 이렇게 굼뜨고 기분 나쁘게 굴어? 무슨 꿍꿍이냐?\"</span> 가까스로 말을 돌려 풀려났지만 벽에 부딪힌 등이 욱신거린다."
                ],
                "deltas": {"hp": -20, "stress": 20, "suspicion": 22},
                "minutes": 15,
            },
        ],
    },
    "shohei_lunch": {
        "heading": "구내식당 — 쇼헤이와 매운 냄새",
        "paragraphs": [
            "구내식당 구석 자리에 앉아 있자, 맞은편 의자가 끌리며 누군가 앉는다. 투톤 머리에 한쪽 눈을 가린 <span class='t-blue'>쇼헤이</span>다.",
            "쇼헤이가 한숨을 내쉬더니 쟁반 하나를 테이블 위로 밀어 놓는다. 코끝을 찌를 듯한 강렬한 향신료 냄새를 풍기는 매운 마늘 카레다.",
            "기시 유스케의 몸은 <span class='t-red'>향이 강한 음식</span>을 받아들이지 못한다. 냄새만으로도 속이 울렁거린다."
        ],
        "choices": [
            {
                "label": "\"야, 나 냄새 지독한 거 싫어하는 거 알면서 일부러 이러지?!\"",
                "result": [
                    "쇼헤이가 피식 웃으며 카레 쟁반을 도로 가져간다. \"여전히 까다롭기는. 자, 여기 냄새 안 나는 흰 죽이나 드시지.\" <span class='t-gold'>흰 죽을 비우고 나니 빈속이 한결 가라앉는다.</span>"
                ],
                "deltas": {"hp": 12, "stress": -8, "suspicion": -4},
                "minutes": 30,
            },
            {
                "label": "그대로 숟가락을 들어 한 입 떠먹는다.",
                "result": [
                    "강렬한 향신료가 목을 넘어가는 순간 <span class='t-red'>위가 뒤집히는 듯한 구역질이 터져 나온다.</span> 쇼헤이가 눈을 크게 뜨며 쳐다본다. \"너 진짜 미쳤어? 그걸 왜 먹어?\" 한동안 화장실을 들락거린다."
                ],
                "deltas": {"hp": -16, "stress": 12, "suspicion": 12},
                "minutes": 30,
            },
        ],
    },
    "dazai_alley": {
        "heading": "요코하마 뒷골목 — 어릴 적 유일한 친구",
        "paragraphs": [
            "어두워진 뒷골목을 걷다 가로등 아래 난간에 걸터앉은 모래색 코트의 사내와 마주친다. 천 너머로 보아도 나른하고 공허한 태도만큼은 한눈에 알아볼 수 있다. <span class='t-red'>다자이 오사무</span>다.",
            "어릴 적부터 함께 자랐으나 사상이 정반대인 탓에 서로 친구라 여기지도 않는 관계. 오래 붙어 지낸 만큼 미세한 어긋남도 즉각 짚어 내는 인물이다.",
            "다자이가 고개를 갸웃거리며 이쪽을 빤히 바라본다. \"어라? 이 죽지 못해 안달 난 기분 나쁜 기척은 유스케잖아? 그런데 오늘따라 공기가 좀 색다르네. 설마 너도 드디어 죽고 싶어졌니?\""
        ],
        "choices": [
            {
                "label": "\"개소리 마, 다자이. 역겹고 의미 없는 삶이라도 죽어버리는 것보다 사는 게 낫거든.\"",
                "result": [
                    "다자이가 흥미가 식었다는 듯 길게 한숨을 내쉰다. \"흥, 여전히 꽉 막힌 생존주의자네. 재미없어.\" <span class='t-gold'>다자이는 그대로 고개를 돌리고 난간에서 뛰어내려 사라진다.</span>"
                ],
                "deltas": {"stress": 6, "suspicion": -10},
                "minutes": 20,
            },
            {
                "label": "\"그건 그렇고, 츄야 얘기나 할까?\" 하고 화제를 돌린다.",
                "result": [
                    "다자이의 입꼬리가 씩 올라간다. \"오~ 모처럼 장단이 맞으려나?\" 잠시 츄야에 대한 잡담이 오가지만, 헤어질 때 다자이의 시선이 등 뒤에 길게 남는다."
                ],
                "deltas": {"stress": 12, "suspicion": 4},
                "minutes": 20,
            },
            {
                "label": "\"솔직히 요즘 너무 힘들어서 나도 가끔 그럴 때가 있어…\"",
                "result": [
                    "다자이의 두 눈에서 빛이 싹 사라진다. <span class='t-red'>\"…잠깐. 유스케가 방금 '죽고 싶다' 비슷한 소리를 했나? 너, 안에 들어앉아 있는 게 누구지?\"</span> 황급히 농담이라며 말을 돌리고 자리를 피하지만 등줄기에 식은땀이 배어 나온다."
                ],
                "deltas": {"stress": 28, "suspicion": 32},
                "minutes": 20,
            },
        ],
    },
    "rainy_stranger": {
        "heading": "요코하마 뒷골목 — 쓰러진 행인",
        "paragraphs": [
            "부슬비가 내리는 골목길 끝, 젖은 아스팔트 위에 누군가 쓰러져 신음하고 있다.",
            "유스케를 키웠던 <span class='t-blue'>'선생님'</span>은 테러 와중에 아이들을 구하다 목숨을 잃었다. 그 이후 유스케는 타인의 생명보다 자신의 생존을 앞세우는 이기주의자가 되었고, 스스로를 희생하며 남을 돕는 부류의 인간을 볼 때마다 노골적인 경계를 드러낸다."
        ],
        "choices": [
            {
                "label": "\"타살은 기회, ■■은 권리 포기야. 살고 싶으면 네 발로 기어서라도 살아남아.\" 구급차만 부르고 돌아선다.",
                "result": [
                    "신고 전화만 간단히 마친 뒤 우산도 없이 발걸음을 돌린다. 비가 얇은 옷깃을 적신다."
                ],
                "deltas": {"stress": 4, "suspicion": -3},
                "minutes": 15,
            },
            {
                "label": "비에 젖은 행인을 부축해 큰길 병원 앞까지 옮긴다.",
                "result": [
                    "허약한 몸으로 성인 한 명을 부축하느라 <span class='t-red'>숨이 턱까지 차오르고 거친 기침이 터진다.</span> 병원 입구에 행인을 내려두고 돌아오자 팔다리가 떨린다."
                ],
                "deltas": {"hp": -15, "stress": -4, "suspicion": 6},
                "minutes": 35,
            },
        ],
    },
}


# -------------------------------------------------
# 3. 장소별 기본 묘사 (현재형, 속마음 서술 배제)
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
        "머리 위에 쓴 천 너머로 어둡고 흐릿한 시야가 이어진다."
        if cloth_on
        else "천을 벗은 상태라 한쪽 눈으로 주변 사물이 또렷이 들어온다. 누구와 눈이 마주치면 곧장 <span class='t-blue'>「검은 집」</span>이 발동한다."
    )

    if loc == "room":
        return [
            f"포트 마피아 말단에게 배정된 좁은 숙소다. 창문 틈으로 요코하마의 {period} 공기가 스며든다. 구석에는 문서 파쇄기와 낡은 세면대, 딱딱한 매트리스의 침대가 놓여 있다.",
            cloth_note,
        ]
    elif loc == "corridor":
        return [
            f"서늘한 회색 벽지가 이어진 포트 마피아 본부 복도다. {period} 시간대라 간간이 구둣발 소리가 들려온다. 여기서 본부 내 여러 구역으로 이동할 수 있다.",
            "천 너머로 스쳐 지나가는 조직원들의 얼굴이 전부 츄야의 모습으로 보인다."
            if cloth_on
            else "<span class='t-red'>천을 벗은 채 복도에 서 있는 탓에 오가는 인원들의 시선이 그대로 닿는다.</span>",
        ]
    elif loc == "office":
        return [
            "말단 조직원들이 모여 있는 하부 사무실이다. 책상 위에는 오늘 처리해야 할 서류 뭉치가 쌓여 있고, 바로 옆에는 문서 파쇄기가 전원을 켠 채 놓여 있다.",
            "주변 동료들은 이쪽 책상을 힐끗거리다가 다시 각자의 일로 시선을 돌린다."
        ]
    elif loc == "clinic":
        return [
            "보스실 안쪽에 딸린 모리 오가이의 간이 진료실이다. 차가운 소독약 냄새가 공기를 채운다. 책상 뒤편에서 모리 오가이가 생글생글 웃으며 이쪽을 바라본다.",
            "\"어머, 유스케 군. 오늘도 살아 있구나? 몸 상태는 좀 어떠니?\""
        ]
    elif loc == "cafeteria":
        return [
            "포트 마피아 구내식당이다. 입구에서부터 짙은 향신료와 기름 냄새가 퍼져 나와 위장이 미세하게 뒤틀린다.",
            f"주머니 속 소지금은 <span class='t-gold'>{st.session_state.money:,}엔</span>이다."
        ]
    elif loc == "roof":
        return [
            f"본부 건물 옥상이다. 철조망 너머로 요코하마 항구와 바다가 내려다보인다. {period}의 바닷바람이 뺨을 스치고 지나간다.",
            "인적이 드문 구석이라 주변을 맴도는 시선이 없다."
        ]
    elif loc == "alley":
        return [
            f"본부 바깥의 요코하마 뒷골목이다. {period}의 눅눅한 공기와 낡은 간판 불빛이 어지럽게 섞여 있다.",
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
            fb.append(f"<span class='t-gold'>몸 상태가 조금 나아진다. (체력 +{d})</span>")
        else:
            fb.append(f"<span class='t-red'>몸에 무리가 간다. (체력 {d})</span>")

    if "stress" in deltas and deltas["stress"] != 0:
        d = deltas["stress"]
        st.session_state.stress = clamp(st.session_state.stress + d)
        if d > 0:
            fb.append(f"<span class='t-red'>신경이 날카로워진다. (스트레스 +{d})</span>")
        else:
            fb.append(f"<span class='t-gold'>호흡이 한결 가라앉는다. (스트레스 {d})</span>")

    if "suspicion" in deltas and deltas["suspicion"] != 0:
        d = deltas["suspicion"]
        st.session_state.suspicion = clamp(st.session_state.suspicion + d)
        if d > 0:
            fb.append(f"<span class='t-red'>주변의 시선이 머문다. (의심 +{d})</span>")
        else:
            fb.append(f"<span class='t-blue'>의심이 옅어진다. (의심 {d})</span>")

    if "money" in deltas and deltas["money"] != 0:
        d = deltas["money"]
        st.session_state.money = max(0, st.session_state.money + d)
        if d > 0:
            fb.append(f"<span class='t-gold'>{d:,}엔을 손에 넣는다.</span>")
        else:
            fb.append(f"<span class='t-muted'>{abs(d):,}엔을 지불한다.</span>")

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
            extra_fb.append("<span class='t-red'>진료를 거른 채 하루가 지나며 시한부 신체의 피로가 누적된다.</span>")
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
            "<span class='t-red'>시야가 새하얗게 점멸하며 숨이 막힌다.</span> 바닥으로 무너지는 감각을 끝으로 의식이 끊어진다.",
            "눈을 뜨자 모리의 진료실 간이 침대 위다. 손등에는 링거가 꽂혀 있고, 침대 머리맡에서는 모리 오가이가 턱을 괸 채 내려다보고 있다.",
            "\"어머나, 유스케 군. 요즘 들어 유독 발작이 잦네? 무슨 낯선 걱정거리라도 생긴 거니?\""
        ]
        st.session_state.feedback = [
            "<span class='t-red'>과호흡으로 기절해 2시간 뒤 모리의 진료실에서 깨어난다.</span>"
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
            "숨을 고른 뒤 천 너머로 좁은 숙소를 둘러본다. 구석의 파쇄기와 책상, 닫힌 방문이 시야에 들어온다."
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
            "딱딱한 침대 위에 몸을 눕히고 얼굴의 천을 잠시 벗어 둔다. 눈을 감자 팽팽하게 당겨져 있던 어깨의 힘이 조금씩 풀린다. <span class='t-gold'>짧은 수면 뒤, 거칠던 숨소리가 한결 고르게 가라앉는다.</span>"
        ]
        fb += apply_deltas({"hp": 14, "stress": -18})

    elif action_id == "mirror_practice":
        minutes = 15
        st.session_state.cloth_on = False
        nar = [
            "세면대 거울 앞에서 천을 벗고 비친 얼굴을 마주 본다. 아무도 없는 곳에서 어둠을 벗어나자 얼굴은 알려진 모습 그대로 고정된다.",
            "입꼬리를 비뚤어지게 올리며 '보쿠'라는 1인칭과 나른한 말투를 몇 번이고 소리 내어 되풀이한다. <span class='t-blue'>입술과 혀에 특유의 억양이 조금씩 익는다.</span>"
        ]
        fb += apply_deltas({"stress": -4, "suspicion": -6})

    elif action_id == "toggle_cloth":
        minutes = 5
        st.session_state.cloth_on = not st.session_state.cloth_on
        if st.session_state.cloth_on:
            nar = ["머리 위로 검은 천을 다시 깊게 눌러쓴다. 시야가 한 겹 어두워진다."]
        else:
            nar = ["천을 걷어 내린다. 찬 공기가 맨얼굴에 닿는다. <span class='t-red'>누군가와 눈이 마주치면 곧장 「검은 집」이 발동한다.</span>"]

    elif action_id == "shred_papers":
        minutes = 25
        nar = [
            "책상 위에 쌓여 있던 보고서 뭉치를 문서 파쇄기 입구에 밀어 넣는다. 위이잉— 하는 날카로운 소음과 함께 종이들이 산산조각 난다.",
            "옆자리 동료가 힐끗 보더니 \"여전하네, 저 미친놈\" 하고 중얼거리며 고개를 돌린다. <span class='t-gold'>더 이상 이쪽을 신경 쓰는 사람은 없다.</span>"
        ]
        fb += apply_deltas({"stress": -8, "suspicion": -10, "money": 400})

    elif action_id == "work_papers":
        minutes = 40
        nar = [
            "책상 위 서류들을 종류별로 분류해 결재판에 끼워 넣는다. 그러자 지나가던 상급자가 걸음을 멈추고 이쪽을 뜯어본다.",
            "\"...기시, 너 보스한테 암살 지령이라도 받았냐? 왜 갑자기 일을 하고 지랄이야?\" 일당은 조금 더 들어오지만 <span class='t-red'>등 뒤로 날카로운 시선이 따라붙는다.</span>"
        ]
        fb += apply_deltas({"hp": -6, "stress": 12, "suspicion": 16, "money": 1200})

    elif action_id == "mori_rude":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"보면 몰라? 모리 씨 얼굴 보니까 수명이 더 깎이는 기분인데. 약이나 빨리 내놔.\"",
            "모리 오가이가 쿡쿡 웃으며 서랍에서 약봉지와 주사기를 꺼낸다. \"하하, 오늘도 기운이 넘쳐 보이니 다행이구나. 자, 얌전히 팔 내밀렴.\" <span class='t-gold'>약물이 혈관을 타고 돌자 답답하던 가슴이 한결 편안해진다.</span>"
        ]
        fb += apply_deltas({"hp": 25, "stress": 4, "suspicion": -8})

    elif action_id == "mori_polite":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"아, 보스님. 항상 챙겨주셔서 감사합니다. 약 잘 받겠습니다.\"",
            "모리의 미소가 순식간에 차갑게 가라앉는다. 그는 주사기를 손가락 사이에서 굴리며 나지막이 속삭인다. <span class='t-red'>\"...보스님? 유스케 군, 네가 나한테 그런 말을 쓰다니. 머리를 어딘가 세게 부딪힌 건 아니겠지?\"</span> 약을 건네받는 손끝에 식은땀이 맺힌다."
        ]
        fb += apply_deltas({"hp": 12, "stress": 18, "suspicion": 24})

    elif action_id == "eat_bland":
        minutes = 25
        if st.session_state.money >= 500:
            nar = [
                "향신료 냄새를 피해 가장 슴슴하고 따뜻한 흰 죽과 맑은 국을 받아 먹는다. 자극적이지 않은 온기가 식도를 타고 내려가며 빈속을 채운다."
            ]
            fb += apply_deltas({"hp": 16, "stress": -10, "money": -500})
        else:
            nar = ["주머니 속 잔돈이 부족하다. <span class='t-muted'>500엔이 필요하다.</span>"]
            minutes = 5

    elif action_id == "roof_breeze":
        minutes = 30
        nar = [
            "차가운 난간에 팔을 기대고 요코하마의 바다를 내려다본다. 짙은 소금기와 바람이 뒤섞여 불어온다.",
            "<span class='t-gold'>바닷바람이 머리와 목덜미를 식히며 거칠던 호흡이 잦아든다.</span>"
        ]
        fb += apply_deltas({"stress": -22, "hp": 3})

    elif action_id == "alley_walk":
        minutes = 30
        nar = [
            "요코하마의 뒷골목을 천천히 걸으며 골목의 갈래와 주변 지형을 눈에 익힌다. 서늘한 바깥 공기가 폐부로 들어온다."
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
# 6. 엔딩 텍스트 (현재형, 속마음 서술 배제)
# -------------------------------------------------
ENDINGS = {
    "ending_survive": {
        "heading": "생존 기록 종료 — 살아가는 것만으로도 수고했어",
        "paragraphs": [
            "일주일이 지나간다. 당장이라도 끊어질 듯했던 호흡을 이어 가며, 허약한 시한부의 몸은 끝내 7일째의 밤을 넘긴다.",
            "여전히 모리 오가이의 약에 수명을 빚지고 있고, 복도마다 츄야의 얼굴이 어른거리며, 뒷골목 어둠 속에서는 다자이가 불쑥 모습을 드러내지만… 그럼에도 심장은 여전히 뛰고 있다.",
            "<span class='t-gold'>\"역겹고 의미 없는 삶이라도 살아가도록 해, 죽어버리는 것보다 살아가는 것이 더 나으니까.\"</span>"
        ],
    },
    "ending_hp": {
        "heading": "기록 중단 — 무너진 호흡",
        "paragraphs": [
            "한계에 다다른 <span class='t-red'>시한부의 몸이 거친 발작과 함께 무너져 내린다.</span>",
            "어두운 바닥 위로 붉은 핏방울이 번져 나간다. 눈앞을 덮은 천 너머의 빛이 서서히 짙은 어둠 속으로 가라앉는다."
        ],
    },
    "ending_caught": {
        "heading": "기록 중단 — 벗겨진 가면",
        "paragraphs": [
            "누적된 위화감이 임계점을 넘는다.",
            "어느 밤, 굳게 닫혀 있던 숙소 문이 소리 없이 열린다. 문틈 사이로 비친 서늘한 눈빛이 이쪽을 꿰뚫어 보듯 내려다본다.",
            "<span class='t-red'>\"기시 유스케는 그런 눈을 하지 않아. 자, 네 안에 들어앉은 낯선 손님과 이야기를 좀 해볼까?\"</span>",
            "포트 마피아의 지하 심문실로 이어지는 계단 아래로 발걸음이 끌려간다."
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
        st.button("침대에 누워 눈을 감는다 (1:00)", on_click=do_action, args=("rest_room",), key="act_rest")
        st.button("거울 앞에서 말투와 표정을 연습한다 (0:15)", on_click=do_action, args=("mirror_practice",), key="act_mirror")
        cloth_btn_lbl = "얼굴을 덮은 천을 벗는다 (0:05)" if st.session_state.cloth_on else "얼굴에 천을 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_r")

    elif loc == "corridor":
        cloth_btn_lbl = "천을 살짝 걷어 본다 (0:05)" if st.session_state.cloth_on else "천을 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_c")

    elif loc == "office":
        st.button("서류 뭉치를 통째로 파쇄기에 넣는다 (0:25)", on_click=do_action, args=("shred_papers",), key="act_shred")
        st.button("서류를 분류해 결재판에 올린다 (0:40)", on_click=do_action, args=("work_papers",), key="act_work")

    elif loc == "clinic":
        st.button("모리에게 반말로 약을 요구한다 (0:20)", on_click=do_action, args=("mori_rude",), key="act_mori_r")
        st.button("모리에게 공손하게 인사하고 약을 받는다 (0:20)", on_click=do_action, args=("mori_polite",), key="act_mori_p")

    elif loc == "cafeteria":
        st.button("향이 없는 흰 죽을 사 먹는다 · 500엔 (0:25)", on_click=do_action, args=("eat_bland",), key="act_eat")

    elif loc == "roof":
        st.button("난간에 기대 요코하마의 바닷바람을 쐰다 (0:30)", on_click=do_action, args=("roof_breeze",), key="act_roof")

    elif loc == "alley":
        st.button("주변 지형을 익히며 뒷골목을 걷는다 (0:30)", on_click=do_action, args=("alley_walk",), key="act_alley")

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
