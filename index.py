import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기시 유스케 생존기",
    page_icon="🕯️",
    layout="wide"
)

# 디자인 테마 (보내주신 스타일 유지 + 문단 간격 보완)
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
    padding: 28px 30px;
    border-radius: 3px;
    line-height: 2.05;
    font-size: 1.02rem;
    margin: 20px 0;
}

.story-box p {
    margin-bottom: 1.2em;
}

.story-box p:last-child {
    margin-bottom: 0;
}

/* 버튼 */
div.stButton > button {
    width: 100%;
    min-height: 3rem;
    text-align: left;
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
    .story-box {
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 소설형 시나리오 데이터
# -------------------------------------------------
SCENES = {
    "intro_1": {
        "heading": "첫째 날 — 낯선 숨결",
        "paragraphs": [
            "가장 먼저 느껴진 것은 지독하리만치 차가운 소독약 냄새였다. 알코올과 오래된 종이, 그리고 콘크리트 벽에 배어 나온 축축한 곰팡이 냄새가 뒤섞여 코끝을 찔렀다. 잠에서 덜 깬 머릿속이 웅웅 울리는 가운데, 당신은 익숙한 휴대폰 알람 소리 대신 낡은 형광등이 미세하게 떨리는 소리를 들었다.",
            "천천히 눈꺼풀을 밀어 올렸지만, 무언가 이상했다. 왼쪽인지 오른쪽인지 모를 시야 한쪽이 아예 열리지 않는 것처럼 새까만 어둠에 잠겨 있었다. 남은 한쪽 눈마저도 흐릿했다. 눈앞을 가로막은 것은 얇고 어두운 천이었다. 숨을 들이쉴 때마다 얼굴 위로 내려앉은 천이 코와 입술 근처에서 미세하게 들썩거렸다.",
            "‘...뭐야, 여기 어디야?’",
            "놀라서 상체를 일으키려던 순간, 폐부 깊숙한 곳에서 쇳소리 비슷한 얕은 기침이 터져 나왔다. 흉곽이 좁고 뻐근했다. 겨우 몸을 일으켜 침대 가장자리에 걸터앉자마자 눈앞이 핑 돌며 구역질이 치밀었다. 다리는 힘없이 떨렸고, 손목을 내려다보자 평소 내 것이라 믿었던 것보다 훨씬 가늘고 핏기 없는 손이 시야에 들어왔다.",
            "어설프게 흔들리는 손으로 얼굴을 덮고 있던 천을 걷어 올렸다. 차가운 공기가 뺨에 닿자마자 소름이 돋았다. 방 안은 지나치게 좁고 단조로웠다. 벽에 걸린 구겨진 검은 정장, 구석에 놓인 문서 파쇄기, 그리고 철제 책상 위에 아무렇게나 굴러다니는 하얀 약병들. 분명 내 방이 아니었다. 꿈이라고 하기엔 발바닥에 닿는 장판의 한기와 목 안쪽의 비릿한 쇳내가 너무도 생생했다."
        ],
        "next_scene": "intro_2",
        "hp_delta": 0,
    },
    "intro_2": {
        "heading": "첫째 날 — 거울 속의 타인",
        "paragraphs": [
            "비틀거리며 작은 세면대 앞까지 걸어간 당신은 벽에 붙은 낡은 거울을 마주 보았다. 그리고 그 자리에 그대로 못 박힌 듯 멈춰 서고 말았다.",
            "거울 속에 서 있는 것은 내가 아니었다. 지나치게 창백한 피부에 마른 체구, 낯선 윤곽의 짧은 머리카락. 그리고 한쪽 눈은 마치 처음부터 빛을 잃어버린 것처럼 어둡고 공허하게 비어 있었다. 살아 있는 사람의 눈빛이라기엔 어딘가 비틀리고 나른한, 묘하게 기분 나쁜 인상이었다.",
            "순간 머릿속에서 엉켜 있던 퍼즐 조각들이 끔찍한 속도로 제자리를 찾아갔다. 검은 천. 실명한 한쪽 눈. 좁은 숙소의 문서 파쇄기와 정체 모를 약병. 그리고 혀끝에 맴도는 낯설고도 익숙한 이름 하나.",
            "‘기시 유스케.’",
            "심장이 발끝까지 떨어지는 기분이었다. 아니, 말도 안 된다. 이건 그냥 내가 설정을 짜고 좋아하던 만화 속 세계관, 그중에서도 가장 살벌한 요코하마의 포트 마피아 소속 자캐의 몸이었다. 전투력이라곤 전무한 데다 시한부 인생이고, 사방이 적투성이며, 보스인 모리 오가이에게도 거리낌 없이 반말을 내뱉는 9년 차 말단 조직원.",
            "갑자기 숨이 가빠졌다. 좁은 가슴통이 조여오며 다시 한번 거친 기침이 쏟아졌다. 손등으로 입을 막고 나서야 손바닥에 희미한 열기와 함께 몸이 얼마나 망가져 있는지 실감이 났다. 평범하게 살던 내가, 총질과 이능력이 난무하는 이 도시에서, 하필이면 이 몸으로 살아남아야 한다고? 손끝이 떨려와 세면대 모서리를 꽉 움켜쥐었다."
        ],
        "next_scene": "intro_3",
        "hp_delta": -8,
    },
    "intro_3": {
        "heading": "첫째 날 — 문 너머의 발소리",
        "paragraphs": [
            "현실을 부정할 틈조차 주어지지 않았다. 복도 저편에서 규칙적이고도 거친 구둣발 소리가 점점 가까워지고 있었다. 당신은 반사적으로 세면대 옆에 떨어져 있던 검은 천을 집어 들어 머리 위로 뒤집어썼다. 심장이 귓가에서 쿵쿵 울려 대며 숨소리를 집어삼킬 것만 같았다.",
            "발소리가 정확히 이 방 문 앞에서 멈췄다. 짧은 침묵 뒤, 노크도 없이 문고리가 거칠게 돌아갔다. 끼익, 하고 낡은 경첩이 우는 소리와 함께 복도의 불빛이 방 안으로 길게 쏟아져 들어왔다.",
            "문이 열리고 누군가 문턱에 섰다. 당신은 숨을 죽인 채 천 너머로 상대를 바라보았다. 그 순간, 온몸의 피가 차갑게 식는 것 같았다.",
            "검은 모자에 주황빛 머리카락, 날카롭게 찌푸린 미간. 문 앞에 서 있는 것은 포트 마피아의 간부, 나카하라 츄야였다.",
            "‘잠깐만. 아니야, 진정해.’",
            "패닉에 빠진 머릿속 한구석에서 이능력 「검은 집」의 설정이 번뜩 떠올랐다. 천을 쓴 채 상대를 바라보면, 상대가 실제로 어떤 얼굴을 하고 있든 내가 가장 믿는 사람—아니, 상대방이 가장 신뢰하는 인물의 모습으로 왜곡되어 보인다고 했다. 포트 마피아 말단 조직원 대부분이 가장 신뢰하는 인물은 츄야다. 그러니까 지금 눈앞에 츄야처럼 보이는 저 사람은 그냥 평범한 동료일 수도 있고… 아니면 정말로 진짜 나카하라 츄야일 수도 있다는 뜻이다.",
            "\"어이, 기시. 아직도 자빠져 자고 있냐?\" 상대가 귀찮다는 듯 문틀에 기대며 낮게 중얼거렸다. \"모리 보스께서 진료 시간 늦지 말라고 전하라더라. 근데 넌 뭘 그렇게 멍하니 서 있어? 또 어디 아픈 척 꾀병 부리려는 건 아니지?\"",
            "목소리에 힘이 잔뜩 들어가 있고 시선이 꽤 날카롭다. 마피아에 9년이나 굴러먹은 기시 유스케라면 절대 저런 말에 주눅 들지 않는다. 하지만 당황한 나머지 평소의 버릇대로 공손하게 대답해 버렸다간, 당장 그 자리에서 의심을 살 게 뻔했다. 마른침이 목구멍을 넘어가지 않았다."
        ],
        "choices": [
            {
                "label": "떨리는 목을 가다듬고, 최대한 유스케처럼 퉁명스럽게 반말로 받아친다.",
                "next_scene": "scene_1_a",
                "hp_delta": 0,
            },
            {
                "label": "목소리가 떨릴 것 같아 입을 다물고, 거친 기침으로 대답을 대신한다.",
                "next_scene": "scene_1_b",
                "hp_delta": -5,
            },
            {
                "label": "순간적으로 패닉에 빠져 평소 습관대로 고개를 숙이며 공손히 대답한다.",
                "next_scene": "scene_1_c",
                "hp_delta": -15,
            },
        ],
    },
    "scene_1_a": {
        "heading": "첫째 날 — 어설픈 가면",
        "paragraphs": [
            "당신은 천 아래에서 어금니를 꽉 깨물었다. 목소리가 갈라지면 끝장이다. 기시 유스케라면 지금 어떤 표정을 지을까. 분명 속으로는 욕을 하면서도 겉으로는 사람 약 올리듯 느긋하게 비아냥거렸을 것이다.",
            "\"...아, 시끄러워. 알아서 갈 거니까 남의 방 앞에서 떠들지 말고 너나 잘해.\"",
            "생각보다 목소리가 낮고 건조하게 나왔다. 다행히 이 몸의 성대가 원래 그런 톤에 익숙해져 있는 모양이었다. 문 앞에 서 있던 상대—목소리를 잘 들어보니 츄야가 아니라 낯선 말단 조직원의 음성이었다—가 어이없다는 듯 혀를 차더니 어깨를 으쓱했다.",
            "\"하, 여전히 싸가지라곤 눈 씻고 찾아볼 수가 없네. 늦어서 보스한테 뒤져도 난 모른다.\"",
            "쾅, 하고 문이 거칠게 닫혔다. 발소리가 멀어지는 것을 확인한 뒤에야 당신은 다리에 힘이 풀려 침대 위로 주저앉았다. 얇은 천 안쪽이 땀으로 축축하게 젖어 있었다. 겨우 첫 고비를 넘겼을 뿐인데도, 당장 어디론가 도망치고 싶은 기분이 목 끝까지 차올랐다.",
            "하지만 도망칠 곳 따위는 없었다. 모리 오가이의 진료실로 가지 않으면, 당장 이 몸이 버티지 못할 테니까."
        ],
        "next_scene": "end_prologue",
        "hp_delta": 0,
    },
    "scene_1_b": {
        "heading": "첫째 날 — 침묵과 기침",
        "paragraphs": [
            "입을 열었다간 분명 말투에서 틈이 보일 것 같았다. 당신은 천 너머로 상대의 시선을 피하며 목 안쪽을 일부러 긁어 거친 기침을 내뱉었다. 그러자 아까의 현기증과 맞물려 진짜로 가래 끓는 기침이 연달아 터져 나왔다. 숨이 턱 막히며 가슴이 아팠다.",
            "문 앞의 인물이 미간을 찌푸리며 한 발 물러섰다. 츄야의 얼굴을 한 조직원이 인상을 구기며 중얼거렸다.",
            "\"...하여튼 병약한 새끼, 피 튀길 거면 문 닫고 기침해라. 귀찮게 옮기지 말고. 시간 맞춰서 진료실로 기어 나와.\"",
            "병약하고 시한부라는 설정이 이런 식으로 먹혀들 줄이야. 상대는 짜증 섞인 한숨과 함께 문을 닫고 사라졌다. 입을 막았던 손끝에 약간의 피로감이 남았지만, 적어도 정체를 의심받지는 않고 시간을 버는 데는 성공했다. 이제 숨을 고르고 밖으로 나갈 준비를 해야 했다."
        ],
        "next_scene": "end_prologue",
        "hp_delta": 0,
    },
    "scene_1_c": {
        "heading": "첫째 날 — 미끄러진 말투",
        "paragraphs": [
            "\"아, 죄송합니다! 지금 바로 준비해서 가겠습니다!\"",
            "긴장한 탓에 머릿속에서 경보가 울리기도 전에, 입이 먼저 현대 한국 사회에서 몸에 밴 공손한 어조를 내뱉어 버렸다. 말끝이 허공에 흩어지자마자 방 안의 공기가 얼음장처럼 굳어졌다.",
            "문 앞의 사내가 미간을 깊게 구기며 한 걸음 안으로 들어섰다. 천 너머로 보이는 츄야의 얼굴이 서늘하게 일그러져 있었다.",
            "\"...야, 기시. 너 방금 뭐라고 했냐?\"",
            "심장이 미친 듯이 날뛰었다. 당신은 황급히 뒷걸음질 치며 목소리를 억지로 쥐어짰다. \"아, 아니, 장난친 거라고. 놀라는 꼴이 웃기잖아.\" 하지만 9년 동안 한 번도 본 적 없는 기시 유스케의 갑작스러운 존댓말에 상대의 눈빛엔 짙은 의구심이 서려 있었다.",
            "\"...이상한 놈. 정신 나간 거 아니면 빨리 나오기나 해.\"",
            "문이 닫힌 뒤에도 한동안 식은땀이 멈추지 않았다. 겨우 첫날, 첫 번째 대화에서부터 치명적인 실수를 저지르고 말았다. 정신을 차리지 않으면 이 도시에서 하루도 버티지 못할 것이 분명했다."
        ],
        "next_scene": "end_prologue",
        "hp_delta": 0,
    },
    "end_prologue": {
        "heading": "프롤로그 완료",
        "paragraphs": [
            "천을 다시 고쳐 쓰고 문고리에 손을 올린다. 문 너머에는 피와 이능력이 뒤엉킨 포트 마피아의 복도와, 당신의 목숨줄을 쥔 모리 오가이가 기다리고 있다.",
            "어떻게든 들키지 않고, 죽지 않고, 살아남아야 한다. 기시 유스케의 껍데기를 뒤집어쓴 채 시작하는 기묘한 생존기가 이제 막 첫 장을 넘겼다."
        ],
        "is_end": True,
    },
}


# -------------------------------------------------
# 상태 초기화 및 이동 함수
# -------------------------------------------------
def init_game():
    st.session_state.scene = "intro_1"
    st.session_state.hp = 100
    st.session_state.last_hp_msg = ""


def move_to(next_key, hp_delta=0):
    st.session_state.hp = max(0, min(100, st.session_state.hp + hp_delta))
    if hp_delta < 0:
        st.session_state.last_hp_msg = f"체력이 {abs(hp_delta)} 감소했습니다."
    elif hp_delta > 0:
        st.session_state.last_hp_msg = f"체력이 {hp_delta} 회복되었습니다."
    else:
        st.session_state.last_hp_msg = ""
    st.session_state.scene = next_key


if "scene" not in st.session_state:
    init_game()


# -------------------------------------------------
# 메인 화면
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
    st.write(f"체력 : {st.session_state.hp} / 100")
    st.progress(st.session_state.hp / 100)

    st.divider()

    st.caption("PORT MAFIA")
    st.caption("SURVIVAL RECORD")


# 콘텐츠 영역
current = SCENES[st.session_state.scene]
st.markdown(f"### {current['heading']}")

if st.session_state.last_hp_msg:
    st.markdown(
        f'<p style="color:#b56c65; font-size:0.9rem;">{st.session_state.last_hp_msg}</p>',
        unsafe_allow_html=True,
    )

paragraphs_html = "".join(f"<p>{p}</p>" for p in current["paragraphs"])
st.markdown(
    f'<div class="story-box">{paragraphs_html}</div>',
    unsafe_allow_html=True,
)

# 버튼 분기
if current.get("is_end"):
    st.button("처음부터 다시 읽기", on_click=init_game, key="restart_btn")
elif "choices" in current:
    for idx, ch in enumerate(current["choices"]):
        st.button(
            ch["label"],
            on_click=move_to,
            args=(ch["next_scene"], ch.get("hp_delta", 0)),
            key=f"btn_{st.session_state.scene}_{idx}",
        )
else:
    st.button(
        "다음으로",
        on_click=move_to,
        args=(current["next_scene"], current.get("hp_delta", 0)),
        key=f"next_{st.session_state.scene}",
    )
