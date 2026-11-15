import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마 (기존 스타일 유지 + DoL식 인라인 텍스트 & HUD 보완)
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

/* DoL 스타일 인라인 텍스트 강조 */
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

/* DoL 스타일 상단 상태 변화 로그 */
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
# 1. 프롤로그 데이터 (빙의 직후의 혼란)
# -------------------------------------------------
PROLOGUE_SCENES = {
    "intro_1": {
        "heading": "도입 — 낯선 숨결",
        "paragraphs": [
            "가장 먼저 느껴진 것은 지독하리만치 차가운 소독약 냄새였다. 알코올과 오래된 종이, 그리고 콘크리트 벽에 배어 나온 축축한 곰팡이 냄새가 뒤섞여 코끝을 찔렀다. 잠에서 덜 깬 머릿속이 웅웅 울리는 가운데, 당신은 익숙한 휴대폰 알람 소리 대신 낡은 형광등이 미세하게 떨리는 소리를 들었다.",
            "천천히 눈꺼풀을 밀어 올렸지만, 무언가 이상했다. 한쪽 시야가 아예 열리지 않는 것처럼 새까만 어둠에 잠겨 있었다. 남은 한쪽 눈마저도 흐릿했다. 눈앞을 가로막은 것은 <span class='t-blue'>얇고 어두운 천</span>이었다. 숨을 들이쉴 때마다 얼굴 위로 내려앉은 천이 코와 입술 근처에서 미세하게 들썩거렸다.",
            "<span class='t-muted'>‘...뭐야, 여기 어디야?’</span>",
            "놀라서 상체를 일으키려던 순간, <span class='t-red'>폐부 깊숙한 곳에서 쇳소리 비슷한 얕은 기침이 터져 나왔다.</span> 흉곽이 좁고 뻐근했다. 겨우 몸을 일으켜 침대 가장자리에 걸터앉자마자 눈앞이 핑 돌며 구역질이 치밀었다. 다리는 힘없이 떨렸고, 손목을 내려다보자 평소 내 것이라 믿었던 것보다 훨씬 가늘고 핏기 없는 손이 시야에 들어왔다.",
            "어설프게 흔들리는 손으로 얼굴을 덮고 있던 천을 걷어 올렸다. 차가운 공기가 뺨에 닿자마자 소름이 돋았다. 방 안은 지나치게 좁고 단조로웠다. 벽에 걸린 구겨진 검은 정장, 구석에 놓인 문서 파쇄기, 그리고 철제 책상 위에 아무렇게나 굴러다니는 하얀 약병들. 분명 내 방이 아니었다. 꿈이라고 하기엔 발바닥에 닿는 장판의 한기와 목 안쪽의 비릿한 쇳내가 너무도 생생했다."
        ],
        "next_scene": "intro_2",
        "minutes": 5,
    },
    "intro_2": {
        "heading": "도입 — 거울 속의 타인",
        "paragraphs": [
            "비틀거리며 작은 세면대 앞까지 걸어간 당신은 벽에 붙은 낡은 거울을 마주 보았다. 그리고 그 자리에 그대로 못 박힌 듯 멈춰 서고 말았다.",
            "거울 속에 서 있는 것은 내가 아니었다. 지나치게 창백한 피부에 마른 체구, 낯선 윤곽의 짧은 머리카락. 그리고 한쪽 눈은 마치 처음부터 빛을 잃어버린 것처럼 어둡고 공허하게 비어 있었다. 살아 있는 사람의 눈빛이라기엔 어딘가 비틀리고 나른한, 묘하게 기분 나쁜 인상이었다.",
            "순간 머릿속에서 엉켜 있던 퍼즐 조각들이 끔찍한 속도로 제자리를 찾아갔다. 검은 천. 실명한 한쪽 눈. 좁은 숙소의 문서 파쇄기와 정체 모를 약병. 그리고 혀끝에 맴도는 낯설고도 익숙한 이름 하나.",
            "<span class='t-blue'>기시 유스케.</span>",
            "심장이 발끝까지 떨어지는 기분이었다. 아니, 말도 안 된다. 이건 그냥 내가 설정을 짜고 좋아하던 세계관, 그중에서도 가장 살벌한 요코하마의 포트 마피아 소속 자캐의 몸이었다. <span class='t-red'>전투력이라곤 전무한 데다 시한부 인생이고, 사방이 적투성이며, 보스인 모리 오가이에게도 거리낌 없이 반말을 내뱉는 9년 차 말단 조직원.</span>",
            "갑자기 숨이 가빠졌다. 좁은 가슴통이 조여오며 다시 한번 거친 기침이 쏟아졌다. 손등으로 입을 막고 나서야 손바닥에 희미한 열기와 함께 몸이 얼마나 망가져 있는지 실감이 났다. 평범하게 살던 내가, 총질과 이능력이 난무하는 이 도시에서, 하필이면 이 몸으로 살아남아야 한다고? 손끝이 떨려와 세면대 모서리를 꽉 움켜쥐었다."
        ],
        "next_scene": "intro_3",
        "minutes": 5,
        "deltas": {"hp": -8, "stress": 12},
    },
    "intro_3": {
        "heading": "도입 — 문 너머의 발소리",
        "paragraphs": [
            "현실을 부정할 틈조차 주어지지 않았다. 복도 저편에서 규칙적이고도 거친 구둣발 소리가 점점 가까워지고 있었다. 당신은 반사적으로 세면대 옆에 떨어져 있던 검은 천을 집어 들어 머리 위로 뒤집어썼다. 심장이 귓가에서 쿵쿵 울려 대며 숨소리를 집어삼킬 것만 같았다.",
            "발소리가 정확히 이 방 문 앞에서 멈췄다. 짧은 침묵 뒤, 노크도 없이 문고리가 거칠게 돌아갔다. 끼익, 하고 낡은 경첩이 우는 소리와 함께 복도의 불빛이 방 안으로 길게 쏟아져 들어왔다.",
            "문이 열리고 누군가 문턱에 섰다. 당신은 숨을 죽인 채 천 너머로 상대를 바라보았다. 그 순간, 온몸의 피가 차갑게 식는 것 같았다.",
            "검은 모자에 주황빛 머리카락, 날카롭게 찌푸린 미간. 문 앞에 서 있는 것은 포트 마피아의 간부, <span class='t-red'>나카하라 츄야</span>였다.",
            "<span class='t-muted'>‘잠깐만. 아니야, 진정해.’</span>",
            "패닉에 빠진 머릿속 한구석에서 이능력 <span class='t-blue'>「검은 집」</span>의 설정이 번뜩 떠올랐다. 천을 쓴 채 상대를 바라보면, 상대가 실제로 어떤 얼굴을 하고 있든 그 사람이 가장 신뢰하는 인물의 모습으로 왜곡되어 보인다. 포트 마피아 말단 조직원 대부분이 가장 신뢰하는 인물은 츄야다. 그러니까 지금 눈앞에 츄야처럼 보이는 저 사람은 그냥 평범한 동료일 수도 있고… 아니면 정말로 진짜 나카하라 츄야일 수도 있다는 뜻이다.",
            "\"어이, 기시. 아직도 자빠져 자고 있냐?\" 상대가 귀찮다는 듯 문틀에 기대며 낮게 중얼거렸다. \"모리 보스께서 진료 시간 늦지 말라고 전하라더라. 근데 넌 뭘 그렇게 멍하니 서 있어? 또 어디 아픈 척 꾀병 부리려는 건 아니지?\"",
            "목소리에 힘이 잔뜩 들어가 있고 시선이 꽤 날카롭다. 마피아에 9년이나 굴러먹은 기시 유스케라면 절대 저런 말에 주눅 들지 않는다. 하지만 당황한 나머지 평소의 버릇대로 공손하게 대답해 버렸다간, 당장 그 자리에서 의심을 살 게 뻔했다."
        ],
        "choices": [
            {
                "label": "떨리는 목을 가다듬고, 최대한 유스케처럼 퉁명스럽게 반말로 받아친다. (0:05)",
                "next_scene": "scene_1_a",
                "minutes": 5,
                "deltas": {"stress": 4, "suspicion": -2},
            },
            {
                "label": "목소리가 떨릴 것 같아 입을 다물고, 거친 기침으로 대답을 대신한다. (0:05)",
                "next_scene": "scene_1_b",
                "minutes": 5,
                "deltas": {"hp": -5, "stress": 2},
            },
            {
                "label": "극도의 긴장 속에서 그만 평소 습관대로 고개를 숙이며 공손히 대답한다. (0:05)",
                "next_scene": "scene_1_c",
                "minutes": 5,
                "deltas": {"stress": 12, "suspicion": 18},
            },
        ],
    },
    "scene_1_a": {
        "heading": "도입 — 어설픈 가면",
        "paragraphs": [
            "당신은 천 아래에서 어금니를 꽉 깨물었다. 목소리가 갈라지면 끝장이다. 기시 유스케라면 지금 어떤 표정을 지을까. 분명 속으로는 욕을 하면서도 겉으로는 사람 약 올리듯 느긋하게 비아냥거렸을 것이다.",
            "\"...아, 시끄러워. 알아서 갈 거니까 남의 방 앞에서 떠들지 말고 너나 잘해.\"",
            "생각보다 목소리가 낮고 건조하게 나왔다. 다행히 이 몸의 성대가 원래 그런 톤에 익숙해져 있는 모양이었다. 문 앞에 서 있던 상대—목소리를 잘 들어보니 츄야가 아니라 낯선 말단 조직원의 음성이었다—가 어이없다는 듯 혀를 차더니 어깨를 으쓱했다.",
            "\"하, 여전히 싸가지라곤 눈 씻고 찾아볼 수가 없네. 늦어서 보스한테 뒤져도 난 모른다.\"",
            "쾅, 하고 문이 거칠게 닫혔다. 발소리가 멀어지는 것을 확인한 뒤에야 당신은 다리에 힘이 풀려 침대 위로 주저앉았다. 얇은 천 안쪽이 땀으로 축축하게 젖어 있었다. <span class='t-gold'>적어도 첫 번째 위기에서 말투가 새어 나가는 것은 막아냈다.</span>",
            "이제 어떡해야 하지. 언제까지 이 좁은 방에 틀어박혀 있을 수만은 없다. 슬슬 움직여야 할 시간이었다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_b": {
        "heading": "도입 — 침묵과 기침",
        "paragraphs": [
            "입을 열었다간 분명 말투에서 틈이 보일 것 같았다. 당신은 천 너머로 상대의 시선을 피하며 목 안쪽을 일부러 긁어 거친 기침을 내뱉었다. 그러자 아까의 현기증과 맞물려 진짜로 가래 끓는 기침이 연달아 터져 나왔다. <span class='t-red'>숨이 턱 막히며 가슴이 아팠다.</span>",
            "문 앞의 인물이 미간을 찌푸리며 한 발 물러섰다. 츄야의 얼굴을 한 조직원이 인상을 구기며 중얼거렸다.",
            "\"...하여튼 병약한 새끼, 피 튀길 거면 문 닫고 기침해라. 귀찮게 옮기지 말고. 시간 맞춰서 진료실로 기어 나와.\"",
            "병약하고 시한부라는 설정이 이런 식으로 먹혀들 줄이야. 상대는 짜증 섞인 한숨과 함께 문을 닫고 사라졌다. 입을 막았던 손끝에 피로감이 남았지만, 적어도 정체를 의심받지는 않고 시간을 버는 데는 성공했다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
    "scene_1_c": {
        "heading": "도입 — 미끄러진 말투",
        "paragraphs": [
            "\"아, 죄송합니다! 지금 바로 준비해서 가겠습니다!\"",
            "긴장한 탓에 머릿속에서 경보가 울리기도 전에, 입이 먼저 현대 사회에서 몸에 밴 공손한 어조를 내뱉어 버렸다. 말끝이 허공에 흩어지자마자 방 안의 공기가 얼음장처럼 굳어졌다.",
            "문 앞의 사내가 미간을 깊게 구기며 한 걸음 안으로 들어섰다. 천 너머로 보이는 츄야의 얼굴이 서늘하게 일그러져 있었다.",
            "\"...야, 기시. 너 방금 뭐라고 했냐?\"",
            "심장이 미친 듯이 날뛰었다. 당신은 황급히 뒷걸음질 치며 목소리를 억지로 쥐어짰다. \"아, 아니, 장난친 거라고. 놀라는 꼴이 웃기잖아.\" 하지만 9년 동안 한 번도 본 적 없는 기시 유스케의 갑작스러운 존댓말에 <span class='t-red'>상대의 눈빛엔 짙은 의구심이 서려 있었다.</span>",
            "\"...이상한 놈. 정신 나간 거 아니면 빨리 나오기나 해.\"",
            "문이 닫힌 뒤에도 한동안 식은땀이 멈추지 않았다. 겨우 첫날, 첫 번째 대화에서부터 치명적인 실수를 저지르고 말았다."
        ],
        "enter_roam": True,
        "minutes": 5,
    },
}


# -------------------------------------------------
# 2. 랜덤 / 특수 이벤트 풀 (DoL 스타일 인카운터)
# -------------------------------------------------
EVENTS = {
    "akane_bump": {
        "heading": "복도 — 보이지 않는 충돌",
        "paragraphs": [
            "천을 뒤집어쓴 채 복도 모퉁이를 돌던 순간이었다. 분명 한쪽 눈으로 확인한 복도 앞쪽은 텅 비어 있었다. 그런데 <span class='t-red'>둔탁한 충격음과 함께 누군가의 어깨에 정면으로 부딪히고 말았다.</span>",
            "바닥에 주저앉아 천을 고쳐 잡으며 앞을 보니, 익숙한 실루엣이 엉덩이를 털고 일어서고 있다. 모리의 집에서 함께 자란 유사 가족, <span class='t-blue'>아카네</span>였다.",
            "아무도 믿지 못하는 아카네의 시선에는 유스케의 머리가 아예 보이지 않고, 천을 쓴 유스케의 눈에도 아카네가 보이지 않는다. 그래서 두 사람은 함께 지낸 세월만큼이나 자주 이렇게 부딪히곤 한다.",
            "\"...아파.\" 아카네가 무덤덤한 목소리로 중얼거렸다. \"기시, 앞 좀 보고 걸어. 어차피 안 보이겠지만.\""
        ],
        "choices": [
            {
                "label": "\"너도 안 보이긴 마찬가지잖아. 조심 좀 해, 아카네.\"",
                "result": [
                    "당신이 무심하게 툭 쏘아붙이자 아카네는 별말 없이 고개를 한 번 끄덕이고는 복도 저편으로 걸어갔다. 서로에게 별다른 기대도, 의심도 없는 관계 덕분에 마음이 조금 놓인다."
                ],
                "deltas": {"hp": -3, "stress": -6, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "\"미안! 많이 다쳤어? 어디 부딪힌 데는 없고?\"",
                "result": [
                    "무심결에 튀어나온 친절한 말투에 아카네의 발걸음이 멈췄다. 아카네는 한동안 아무 말 없이 당신을 가만히 바라보다가 낮게 중얼거렸다. <span class='t-red'>\"...기분 나쁘게 왜 갑자기 상냥한 척해?\"</span> 그 시선이 꽤 오래 머물렀다."
                ],
                "deltas": {"hp": -3, "stress": 8, "suspicion": 14},
                "minutes": 10,
            },
        ],
    },
    "chuuya_hallway": {
        "heading": "복도 — 사방이 츄야인 지옥",
        "paragraphs": [
            "교대 시간과 겹쳤는지 복도에 포트 마피아 조직원들이 꽤 많이 오가고 있다. 문제라면 천 너머로 비치는 <span class='t-blue'>지나가는 사람들의 얼굴이 죄다 나카하라 츄야</span>로 보인다는 점이다.",
            "어딜 둘러봐도 츄야, 뒤를 돌아봐도 츄야. 마피아 말단들이 가장 신뢰하는 이가 그 사람인 탓에 시야 전체가 똑같은 얼굴로 채워져 숨이 막힌다. 하필이면 맞은편에서 걸어오던 한 '츄야'가 당신과 어깨가 스치자 걸음을 멈췄다.",
            "\"어이, 기시. 눈을 가리고 다니면 앞을 좀 살피든가.\""
        ],
        "choices": [
            {
                "label": "목소리를 잘 구분해 말단임을 확인하고, 태연하게 들고 있던 심부름 봉투를 떠넘긴다.",
                "result": [
                    "높낮이를 들어보니 간부가 아닌 하급 조직원이었다. \"바빠 죽겠으니까 네가 대신 전해.\" 뻔뻔하게 봉투를 안기고 돌아서자 뒤에서 욕하는 소리가 들렸지만, <span class='t-gold'>완벽한 유스케다운 처세술이었다.</span>"
                ],
                "deltas": {"stress": -4, "suspicion": -3},
                "minutes": 10,
            },
            {
                "label": "혹시 진짜 츄야일까 봐 잔뜩 긴장한 채 고개만 숙이고 빠르게 지나간다.",
                "result": [
                    "상대가 \"뭐야 저 기분 나쁜 놈은\" 하고 중얼거렸지만 다행히 붙잡지는 않았다. 다만 심장이 쫄깃해진 탓에 피로가 쌓였다."
                ],
                "deltas": {"stress": 6, "suspicion": 2},
                "minutes": 5,
            },
        ],
    },
    "real_chuuya": {
        "heading": "복도 — 진짜 나카하라 츄야",
        "paragraphs": [
            "복도 모퉁이를 도는 순간, 공기부터가 달랐다. 사방에 널려 있던 허상들과 달리 묵직한 위압감과 날카로운 시선이 정면으로 꽂혔다. 검은 모자 아래로 뻗은 주황빛 머리카락. 이번엔 <span class='t-red'>100% 진짜 나카하라 츄야</span>다.",
            "원래 유스케는 모리 다음으로 츄야를 싫어하고, 츄야 역시 다자이와 비슷한 결이면서도 어딘가 더 불쾌하다며 유스케를 싫어한다. 츄야가 불쾌하다는 듯 미간을 찌푸리며 당신을 멈춰 세웠다.",
            "\"어이, 기시. 아까부터 복도에서 어슬렁거리면서 뭘 그렇게 흘끔거리는 거야?\""
        ],
        "choices": [
            {
                "label": "\"하아? 여기 사방에 네 얼굴이 널려 있어서 토 나올 것 같다고.\"",
                "result": [
                    "츄야의 관자놀이에 핏줄이 섰다. \"뭐, 뭐라고 이 자식이...?!\" 금방이라도 주먹이 날아올 것 같았지만, 이내 네 녀석 이능력 때문이라는 걸 떠올린 듯 거칠게 혀를 차며 지나갔다. <span class='t-gold'>위험천만한 줄타기였지만 의심은 완전히 피했다.</span>"
                ],
                "deltas": {"stress": 10, "suspicion": -6},
                "minutes": 10,
            },
            {
                "label": "\"아, 아니요! 아무것도 안 봤습니다. 먼저 가겠습니다!\"",
                "result": [
                    "순간 너무 쫄아서 공손하게 대답하고 말았다. 츄야의 걸음이 우뚝 멈추더니, 당신의 멱살을 잡아 벽으로 밀어붙였다. <span class='t-red'>\"...너 오늘 왜 이렇게 굼뜨고 기분 나쁘게 굴어? 무슨 꿍꿍이냐?\"</span> 간신히 둘러대고 풀려났지만 온몸이 쑤시고 멍이 들었다."
                ],
                "deltas": {"hp": -20, "stress": 20, "suspicion": 22},
                "minutes": 15,
            },
        ],
    },
    "shohei_lunch": {
        "heading": "구내식당 — 쇼헤이와 지독한 냄새",
        "paragraphs": [
            "구내식당 구석 자리에 앉아 있자, 맞은편 의자가 드르륵 끌리며 누군가 앉았다. 투톤 머리에 한쪽 눈을 가린 <span class='t-blue'>쇼헤이</span>였다. 겉과 속이 다르고 한쪽 눈을 잃었다는 점까지 유스케와 닮은 구석이 많은, 그나마 말이 통하는 상대다.",
            "쇼헤이가 한숨을 푹 쉬더니 쟁반 하나를 당신 쪽으로 밀어 놓았다. 그 위에 놓인 것은 코끝을 찌를 듯이 강렬한 향신료 냄새를 풍기는 매운 마늘 카레였다.",
            "머릿속 기억이 경고를 울린다. 기시 유스케는 <span class='t-red'>향이 강한 음식을 끔찍하게 싫어한다.</span>"
        ],
        "choices": [
            {
                "label": "\"야, 나 냄새 지독한 거 싫어하는 거 알면서 일부러 이러지?!\"",
                "result": [
                    "쇼헤이가 피식 웃으며 카레 쟁반을 도로 가져갔다. \"여전히 까다롭기는. 자, 여기 냄새 안 나는 흰 죽이나 드시지.\" 투닥거리긴 했지만 <span class='t-gold'>속 편하게 식사를 마치고 기력을 조금 채웠다.</span>"
                ],
                "deltas": {"hp": 12, "stress": -8, "suspicion": -4},
                "minutes": 30,
            },
            {
                "label": "배가 고파서 그냥 참고 한 숟갈 크게 떠먹는다.",
                "result": [
                    "강렬한 향신료가 목을 넘어가는 순간 <span class='t-red'>위가 뒤집히는 듯한 격통과 구역질이 몰려왔다.</span> 쇼헤이가 경악하며 쳐다보았다. \"너 진짜 미쳤어? 그걸 왜 쳐먹어?\" 한동안 화장실에서 나오지 못했다."
                ],
                "deltas": {"hp": -16, "stress": 12, "suspicion": 12},
                "minutes": 30,
            },
        ],
    },
    "dazai_alley": {
        "heading": "요코하마 뒷골목 — 어릴 적 유일한 친구",
        "paragraphs": [
            "어두워진 뒷골목을 걷던 중, 가로등 불빛 아래 난간에 걸터앉아 있는 모래색 코트의 사내와 눈이 마주쳤다. 아니, 천 너머로도 그 나른하고 공허한 분위기만큼은 단번에 알아볼 수 있었다. <span class='t-red'>다자이 오사무</span>였다.",
            "어릴 적부터 함께 자랐으나 놀라울 정도로 사상이 반대여서 서로 친구라고도 생각하지 않는 관계. 하지만 오래 지낸 만큼 상대의 미세한 변화도 귀신같이 꿰뚫어 보는 <span class='t-red'>가장 위험한 인물</span>이다.",
            "다자이가 고개를 갸웃거리며 천을 쓴 당신을 빤히 쳐다보았다. \"어라? 이 죽지 못해 안달 난 기분 나쁜 기척은 유스케잖아? 그런데 오늘따라 공기가 좀 색다르네. 설마 너도 드디어 죽고 싶어졌니?\""
        ],
        "choices": [
            {
                "label": "\"개소리 마, 다자이. 역겹고 의미 없는 삶이라도 죽어버리는 것보다 사는 게 낫거든.\"",
                "result": [
                    "다자이가 흥미가 식었다는 듯 길게 한숨을 내쉬었다. \"흥, 여전히 꽉 막힌 생존주의자네. 재미없어.\" <span class='t-gold'>유스케의 본질 그대로 받아친 덕분에 다자이의 예리한 시선을 무사히 따돌렸다.</span>"
                ],
                "deltas": {"stress": 6, "suspicion": -10},
                "minutes": 20,
            },
            {
                "label": "\"그건 그렇고, 츄야 얘기나 할까?\" (억지로 화제를 돌린다)",
                "result": [
                    "다자이의 입꼬리가 씩 올라갔다. \"오~ 모처럼 장단이 맞으려나?\" 잠깐 동안 시시한 잡담을 나누며 위기를 넘겼지만, 헤어질 때 다자이가 묘한 눈빛으로 당신의 뒷모습을 훑는 느낌이 들었다."
                ],
                "deltas": {"stress": 12, "suspicion": 4},
                "minutes": 20,
            },
            {
                "label": "\"솔직히 요즘 너무 힘들어서 나도 가끔 그럴 때가 있어…\"",
                "result": [
                    "다자이의 두 눈에서 빛이 싹 사라졌다. <span class='t-red'>\"…잠깐. 유스케가 방금 '죽고 싶다' 비슷한 소리를 했나? 너, 안에 들어앉아 있는 게 누구지?\"</span> 식은땀을 쏟으며 농담이었다고 둘러댔지만 등골이 서늘하게 얼어붙었다."
                ],
                "deltas": {"stress": 28, "suspicion": 32},
                "minutes": 20,
            },
        ],
    },
    "rainy_stranger": {
        "heading": "요코하마 뒷골목 — 쓰러진 행인",
        "paragraphs": [
            "부슬비가 내리는 골목길 끝, 누군가 젖은 아스팔트 위에 쓰러져 신음하고 있다. 평범한 시민이었던 당신의 양심은 당장 다가가 부축하라고 소리치지만, 유스케의 기억은 차갑게 속삭인다.",
            "유스케를 키웠던 <span class='t-blue'>'선생님'</span> 역시 테러 와중에 아이들의 울음소리를 외면하지 못하고 뛰어들었다가 목숨을 잃었다. 그 뒤로 유스케는 타인의 목숨보다 자신의 생존을 최우선으로 삼는 이기주의자가 되었고, 선생님과 비슷한 부류의 인간을 볼 때마다 노골적으로 경계심을 드러낸다."
        ],
        "choices": [
            {
                "label": "\"타살은 기회, ■■은 권리 포기야. 살고 싶으면 네 발로 기어서라도 살아남아.\" 구급차만 부르고 돌아선다.",
                "result": [
                    "가슴 한구석이 묵직하게 아렸지만, 최소한의 조치만 남기고 유스케답게 자리를 떴다. 정체성도 지키고 무리도 하지 않았다."
                ],
                "deltas": {"stress": 4, "suspicion": -3},
                "minutes": 15,
            },
            {
                "label": "비에 젖은 행인을 직접 부축해 큰길 병원 앞까지 데려다준다.",
                "result": [
                    "허약한 몸으로 성인 한 명을 부축하느라 <span class='t-red'>숨이 턱까지 차오르고 기침이 터졌다.</span> 겨우 숙소 쪽으로 돌아왔지만 체력이 크게 빠졌다."
                ],
                "deltas": {"hp": -15, "stress": -4, "suspicion": 6},
                "minutes": 35,
            },
        ],
    },
}


# -------------------------------------------------
# 3. 장소별 기본 묘사 & 행동 정의
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
        "머리에 쓴 얇은 천 너머로 세계가 한 겹 가라앉아 보인다."
        if cloth_on
        else "천을 벗고 있어 한쪽 눈으로나마 주변 사물이 또렷하게 들어온다. 다만 누구와 마주치면 곧장 <span class='t-blue'>「검은 집」</span>이 발동할 것이다."
    )

    if loc == "room":
        return [
            f"포트 마피아 말단에게 배정된 좁은 숙소다. 창문 틈으로 요코하마의 {period} 공기가 스며든다. 구석에는 서류 파쇄기와 낡은 세면대, 그리고 단단한 매트리스의 침대가 놓여 있다.",
            cloth_note,
        ]
    elif loc == "corridor":
        return [
            f"서늘한 회색빛 벽지가 이어진 포트 마피아 본부 복도다. {period} 시간대라 그런지 간간이 구둣발 소리가 들려온다. 이곳에서라면 본부 내 각 구역으로 이동할 수 있다.",
            "천 너머로 보이는 조직원들의 얼굴이 전부 츄야로 왜곡되어 스쳐 지나갈 때마다 심장이 덜컥 내려앉는다."
            if cloth_on
            else "<span class='t-red'>천을 벗은 채 복도에 서 있자니 지나가는 조직원과 눈이 마주칠까 봐 등골이 오싹하다.</span>",
        ]
    elif loc == "office":
        return [
            "말단 조직원들이 몰려 있는 하부 사무실이다. 당신의 책상 위에는 오늘 처리해야 할 문서 뭉치가 수북이 쌓여 있고, 바로 옆에는 유난히 잘 닦인 문서 파쇄기가 입을 벌리고 있다.",
            "주변 동료들은 당신이 또 서류를 파쇄기에 갈아버릴 거라 당연하게 여기는 눈치다."
        ]
    elif loc == "clinic":
        return [
            "보스실 안쪽에 딸린 모리 오가이의 간이 진료실이다. 차가운 약품 냄새가 코를 찌른다. 책상 뒤편에서 모리 오가이가 생글생글 웃으며 당신을 내려다보고 있다.",
            "\"어머, 유스케 군. 오늘도 살아 있구나? 몸 상태는 좀 어떠니?\""
        ]
    elif loc == "cafeteria":
        return [
            "포트 마피아 구내식당. 향신료와 기름 냄새가 은은하게 퍼져 있어, 향이 강한 음식을 싫어하는 이 몸은 입구에서부터 미간이 찌푸려진다.",
            f"현재 소지금은 <span class='t-gold'>{st.session_state.money:,}엔</span>이다."
        ]
    elif loc == "roof":
        return [
            f"본부 건물 옥상. 철조망 너머로 요코하마 항구와 바다가 한눈에 내려다보인다. {period}의 바닷바람이 뺨을 스치며 답답했던 폐부를 조금이나마 식혀 준다.",
            "아무도 찾지 않는 구석이라 이곳에서만큼은 가면의 무게를 잠시 내려놓을 수 있다."
        ]
    elif loc == "alley":
        return [
            f"본부 바깥의 요코하마 뒷골목이다. {period}의 눅눅한 공기와 낡은 간판 불빛이 어지럽게 섞여 있다. 마피아 건물 안과는 달리, 이곳에서는 누구와 마주칠지 한 치 앞을 알 수 없다.",
            cloth_note,
        ]
    return [""]


# -------------------------------------------------
# 4. 상태 초기화 및 시간/행동 처리 엔진
# -------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def init_game():
    st.session_state.mode = "prologue"  # prologue | roam | event | event_result | ending
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
            fb.append(f"<span class='t-gold'>체력이 {d} 회복되었다.</span>")
        else:
            fb.append(f"<span class='t-red'>체력이 {abs(d)} 감소했다.</span>")

    if "stress" in deltas and deltas["stress"] != 0:
        d = deltas["stress"]
        st.session_state.stress = clamp(st.session_state.stress + d)
        if d > 0:
            fb.append(f"<span class='t-red'>스트레스가 {d} 쌓였다.</span>")
        else:
            fb.append(f"<span class='t-gold'>스트레스가 {abs(d)} 가라앉았다.</span>")

    if "suspicion" in deltas and deltas["suspicion"] != 0:
        d = deltas["suspicion"]
        st.session_state.suspicion = clamp(st.session_state.suspicion + d)
        if d > 0:
            fb.append(f"<span class='t-red'>주변의 의심이 {d} 높아졌다.</span>")
        else:
            fb.append(f"<span class='t-blue'>의심이 {abs(d)} 줄어들었다.</span>")

    if "money" in deltas and deltas["money"] != 0:
        d = deltas["money"]
        st.session_state.money = max(0, st.session_state.money + d)
        if d > 0:
            fb.append(f"<span class='t-gold'>{d:,}엔을 얻었다.</span>")
        else:
            fb.append(f"<span class='t-muted'>{abs(d):,}엔을 사용했다.</span>")

    return fb


def advance_time(minutes: int):
    st.session_state.minute_of_day += minutes
    extra_fb = []
    while st.session_state.minute_of_day >= 1440:
        st.session_state.minute_of_day -= 1440
        st.session_state.day += 1
        # 하루가 지날 때마다 시한부 신체의 자연 피로
        if not st.session_state.mori_visited_today:
            st.session_state.hp = clamp(st.session_state.hp - 12)
            st.session_state.stress = clamp(st.session_state.stress + 8)
            extra_fb.append("<span class='t-red'>진료를 거른 채 날이 바뀌어 시한부 몸에 무리가 왔다.</span>")
        else:
            st.session_state.hp = clamp(st.session_state.hp - 5)
        st.session_state.mori_visited_today = False
    return extra_fb


def check_status_triggers():
    # 배드 엔딩 체크
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

    # DoL 스타일 스트레스 100 한계 돌파 -> 과호흡 기절 후 진료실 기상
    if st.session_state.stress >= 100:
        st.session_state.stress = 55
        st.session_state.hp = clamp(st.session_state.hp - 18)
        st.session_state.suspicion = clamp(st.session_state.suspicion + 10)
        st.session_state.location = "clinic"
        st.session_state.mori_visited_today = True
        advance_time(120)
        st.session_state.narrative = [
            "<span class='t-red'>한계치까지 치솟은 긴장과 공포 끝에 시야가 새하얗게 점멸했다.</span> 숨을 들이마실 수 없었다. 차가운 바닥으로 무너지던 감각을 끝으로 의식이 끊어졌다.",
            "얼마나 지났을까. 눈을 떴을 때 당신은 모리의 진료실 간이 침대에 누워 있었다. 손등에는 링거가 꽂혀 있었고, 침대 머리맡에는 모리 오가이가 턱을 괸 채 흥미롭다는 듯 웃고 있었다.",
            "\"어머나, 유스케 군. 요즘 들어 유독 발작이 잦네? 무슨 낯선 걱정거리라도 생긴 거니?\""
        ]
        st.session_state.feedback = [
            "<span class='t-red'>스트레스 한계로 기절해 2시간 뒤 진료실에서 깨어났다.</span>"
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
            "당신은 겨우 떨림을 가라앉히며 천 너머로 좁은 숙소를 둘러보았다. 이제부터가 진짜 시작이다. 모리 오가이의 진료실에 들러 약을 타거나, 사무실로 가 말단 노릇을 하거나, 일단 숨을 좀 돌려야 한다."
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

    # 이동 중 랜덤 인카운터 확률 (DoL 스타일)
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
            "딱딱한 침대 위에 몸을 눕히고 천을 옆으로 내려놓았다. 눈을 감자 팽팽하게 당겨져 있던 신경이 조금씩 풀려나갔다. <span class='t-gold'>짧지만 귀중한 수면 덕분에 거칠던 숨소리가 한결 고르게 가라앉았다.</span>"
        ]
        fb += apply_deltas({"hp": 14, "stress": -18})

    elif action_id == "mirror_practice":
        minutes = 15
        st.session_state.cloth_on = False
        nar = [
            "세면대 거울 앞에서 천을 벗고, 거울 속에 비친 유스케의 얼굴을 마주 보았다. 아무도 없는 곳에서 어둠을 벗어나니 얼굴은 익숙한 유스케의 모습으로 고정되어 있다.",
            "당신은 입꼬리를 비뚤어지게 올리며 '보쿠'라는 1인칭과 특유의 나른한 말투를 소리 내어 연습했다. <span class='t-blue'>거울 속의 타인이 조금은 내 얼굴처럼 느껴지기 시작했다.</span>"
        ]
        fb += apply_deltas({"stress": -4, "suspicion": -6})

    elif action_id == "toggle_cloth":
        minutes = 5
        st.session_state.cloth_on = not st.session_state.cloth_on
        if st.session_state.cloth_on:
            nar = ["머리 위로 검은 천을 다시 깊게 눌러썼다. 시야가 한 겹 어두워지며 마음이 미세하게 진정되었다."]
        else:
            nar = ["답답한 천을 걷어 내렸다. 찬 공기가 얼굴에 닿는다. <span class='t-red'>누군가와 눈이 마주치면 즉시 「검은 집」이 발동될 것이다.</span>"]

    elif action_id == "shred_papers":
        minutes = 25
        nar = [
            "당신은 책상 위에 쌓여 있던 보고서 뭉치를 한 치의 망설임도 없이 문서 파쇄기 입구에 밀어 넣었다. 위이잉— 하는 날카로운 소음과 함께 종이들이 산산조각 나 떨어졌다.",
            "옆자리 동료가 힐끗 보더니 \"여전하네, 저 미친놈\" 하고 중얼거리며 고개를 돌렸다. <span class='t-gold'>기시 유스케답게 구는 것만으로도 의심을 크게 덜어낼 수 있었다.</span>"
        ]
        fb += apply_deltas({"stress": -8, "suspicion": -10, "money": 400})

    elif action_id == "work_papers":
        minutes = 40
        nar = [
            "차마 전부 갈아버릴 수 없어 서류들을 꼼꼼히 분류해 결재판에 끼워 넣었다. 그러자 지나가던 상급자가 걸음을 멈추고 섬뜩하다는 눈빛으로 당신을 뜯어보았다.",
            "\"...기시, 너 보스한테 암살 지령이라도 받았냐? 왜 갑자기 일을 하고 지랄이야?\" 일당은 조금 챙겼지만 <span class='t-red'>등 뒤로 쏟아지는 의심의 눈초리가 따가웠다.</span>"
        ]
        fb += apply_deltas({"hp": -6, "stress": 12, "suspicion": 16, "money": 1200})

    elif action_id == "mori_rude":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"보면 몰라? 모리 씨 얼굴 보니까 수명이 더 깎이는 기분인데. 약이나 빨리 내놔.\"",
            "모리 오가이가 쿡쿡 웃으며 책상 서랍에서 약봉지와 주사기를 꺼냈다. \"하하, 오늘도 기운이 넘쳐 보이니 다행이구나. 자, 얌전히 팔 내밀렴.\" <span class='t-gold'>약물이 혈관을 타고 돌자 답답하던 폐부가 한결 편안해졌다.</span>"
        ]
        fb += apply_deltas({"hp": 25, "stress": 4, "suspicion": -8})

    elif action_id == "mori_polite":
        minutes = 20
        st.session_state.mori_visited_today = True
        nar = [
            "\"아, 보스님. 항상 챙겨주셔서 감사합니다. 약 잘 받겠습니다.\"",
            "말을 끝내기도 전에 모리의 미소가 차갑게 가라앉았다. 그는 주사기를 손가락 사이에서 굴리며 나지막이 속삭였다. <span class='t-red'>\"...보스님? 유스케 군, 네가 나한테 그런 말을 쓰다니. 머리를 어딘가 세게 부딪힌 건 아니겠지?\"</span> 약은 받았지만 심장이 떨어질 듯했다."
        ]
        fb += apply_deltas({"hp": 12, "stress": 18, "suspicion": 24})

    elif action_id == "eat_bland":
        minutes = 25
        if st.session_state.money >= 500:
            nar = [
                "향신료 냄새를 피해 가장 슴슴하고 따뜻한 흰 죽과 맑은 국을 주문해 먹었다. 자극적이지 않은 온기가 식도를 타고 내려가며 허기진 속을 부드럽게 채워 주었다."
            ]
            fb += apply_deltas({"hp": 16, "stress": -10, "money": -500})
        else:
            nar = ["주머니를 뒤져 보았지만 식사 값이 부족하다. <span class='t-muted'>500엔이 필요하다.</span>"]
            minutes = 5

    elif action_id == "roof_breeze":
        minutes = 30
        nar = [
            "차가운 난간에 팔을 기대고 요코하마의 바다를 내려다보았다. 짙은 소금기와 바람이 뒤엉켜 불어왔다. 이 빌어먹을 마피아 건물 안에서 유일하게 숨통이 트이는 순간이었다.",
            "<span class='t-gold'>머리를 짓누르던 불안감이 바람과 함께 조금씩 흩어졌다.</span>"
        ]
        fb += apply_deltas({"stress": -22, "hp": 3})

    elif action_id == "alley_walk":
        minutes = 30
        nar = [
            "낯선 요코하마의 뒷골목을 천천히 걸으며 도망칠 만한 루트가 있는지, 주변 지형은 어떤지 머릿속에 새겨 두었다. 당장 탈출할 수는 없지만, 바깥 공기를 마시니 숨이 조금 쉬어졌다."
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
# 6. 엔딩 텍스트
# -------------------------------------------------
ENDINGS = {
    "ending_survive": {
        "heading": "생존 기록 종료 — 살아가는 것만으로도 수고했어",
        "paragraphs": [
            "아슬아슬한 줄타기 같았던 7일이 마침내 지나갔다. 당장이라도 숨이 끊어질 듯했던 허약한 몸을 이끌고, 언제 들킬지 모르는 살얼음판 위에서 당신은 끝내 버텨냈다.",
            "여전히 모리 오가이의 약에 목숨줄을 빚지고 있고, 복도를 걸을 때마다 사방이 츄야로 보이며, 다자이와 마주칠 때마다 심장이 내려앉지만… 그럼에도 오늘 당신은 살아 있다.",
            "<span class='t-gold'>\"역겹고 의미 없는 삶이라도 살아가도록 해, 죽어버리는 것보다 살아가는 것이 더 나으니까.\"</span>"
        ],
    },
    "ending_hp": {
        "heading": "기록 중단 — 무너진 호흡",
        "paragraphs": [
            "끝내 한계에 다다른 <span class='t-red'>시한부의 몸이 비명을 지르며 무너져 내렸다.</span>",
            "어두운 바닥 위로 붉은 핏방울이 번져 나가는 가운데, 눈앞을 덮은 천 너머의 세계가 서서히 짙은 어둠 속으로 가라앉는다. 기시 유스케의 짧은 생존 기록은 여기서 멈추었다."
        ],
    },
    "ending_caught": {
        "heading": "기록 중단 — 벗겨진 가면",
        "paragraphs": [
            "누적된 위화감이 마침내 임계점을 넘고 말았다.",
            "어느 밤, 굳게 닫혀 있던 숙소 문이 소리 없이 열렸다. 문틈 사이로 비친 서늘한 눈빛이 당신의 껍데기를 꿰뚫어 보듯 내려다보았다.",
            "<span class='t-red'>\"기시 유스케는 그런 눈을 하지 않아. 자, 네 안에 들어앉은 낯선 손님과 이야기를 좀 해볼까?\"</span>",
            "포트 마피아의 지하 심문실로 끌려가는 것을 끝으로, 당신의 생존기는 막을 내렸다."
        ],
    },
}


if "mode" not in st.session_state:
    init_game()


# -------------------------------------------------
# 7. DoL 스타일 사이드바 HUD
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

# [D] DoL 스타일 자유 행동 및 이동 모드
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
        st.button("거울 앞에서 유스케의 말투와 표정을 연습한다 (0:15)", on_click=do_action, args=("mirror_practice",), key="act_mirror")
        cloth_btn_lbl = "얼굴을 덮은 천을 벗는다 (0:05)" if st.session_state.cloth_on else "얼굴에 천을 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_r")

    elif loc == "corridor":
        cloth_btn_lbl = "천을 살짝 걷어 본다 (0:05)" if st.session_state.cloth_on else "천을 급히 다시 뒤집어쓴다 (0:05)"
        st.button(cloth_btn_lbl, on_click=do_action, args=("toggle_cloth",), key="act_cloth_c")

    elif loc == "office":
        st.button("서류 뭉치를 통째로 파쇄기에 갈아버린다 (0:25)", on_click=do_action, args=("shred_papers",), key="act_shred")
        st.button("양심상 서류를 분류해 결재를 올린다 (0:40)", on_click=do_action, args=("work_papers",), key="act_work")

    elif loc == "clinic":
        st.button("모리에게 혐오 어린 반말을 내뱉으며 약을 타간다 (0:20)", on_click=do_action, args=("mori_rude",), key="act_mori_r")
        st.button("긴장해서 모리에게 공손하게 인사하고 약을 받는다 (0:20)", on_click=do_action, args=("mori_polite",), key="act_mori_p")

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
