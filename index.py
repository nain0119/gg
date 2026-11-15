import random
import streamlit as st

# ---------------------------------------------------------
# 1. 페이지 설정 및 포트 마피아 다크 테마 CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="기시 유스케 생존기 | 문스독 빙의 텍스트 게임",
    page_icon="🕶️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e0e12;
        color: #e6e2dc;
    }
    section[data-testid="stSidebar"] {
        background-color: #16161d;
        border-right: 1px solid #2e2024;
    }
    .story-box {
        background-color: #181820;
        border-left: 4px solid #9e2a2b;
        padding: 22px 26px;
        border-radius: 6px;
        line-height: 1.85;
        font-size: 1.05rem;
        margin-bottom: 18px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.45);
    }
    .result-box {
        background-color: #1c1a24;
        border-left: 4px solid #c99a49;
        padding: 20px 24px;
        border-radius: 6px;
        line-height: 1.8;
        font-size: 1.03rem;
        margin-bottom: 16px;
    }
    .ending-box {
        background-color: #1b1215;
        border: 1px solid #9e2a2b;
        padding: 26px 30px;
        border-radius: 8px;
        line-height: 1.85;
        font-size: 1.06rem;
        margin-bottom: 20px;
    }
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
        background-color: #262632;
        color: #e6e2dc;
        border: 1px solid #3a3a4a;
    }
    .badge-warn {
        background-color: #3a1a1d;
        border-color: #9e2a2b;
        color: #ff9c9e;
    }
    .badge-good {
        background-color: #182f24;
        border-color: #388e5c;
        color: #8ce9b0;
    }
    div.stButton > button {
        width: 100%;
        text-align: left;
        background-color: #1e1e28;
        color: #ebe7e0;
        border: 1px solid #38384a;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 0.98rem;
        transition: all 0.15s ease;
    }
    div.stButton > button:hover {
        background-color: #2b1d22;
        border-color: #b53437;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SLOTS = ["오전", "오후", "밤"]


# ---------------------------------------------------------
# 2. 게임 데이터 (고정 스토리 + 랜덤 이벤트 풀 + 엔딩)
# ---------------------------------------------------------
def get_fixed_events():
    return {
        (1, 0): {
            "id": "prologue",
            "title": "DAY 1 오전 — 낯선 천, 한쪽 눈의 어둠",
            "text": (
                "눈을 뜨자 지독한 소독약 냄새와 함께 폐부 깊숙이 묵직한 통증이 스친다. "
                "시야 한쪽은 완전히 어둡고, 얼굴 위에는 얇은 검은 천이 드리워져 있다.\n\n"
                "거울을 볼 새도 없이 당신은 깨닫는다. 이곳은 요코하마. "
                "당신은 포트 마피아 9년 차 말단이자 시한부 생존주의자, **'기시 유스케'**의 몸에 빙의했다.\n\n"
                "그때, 문이 벌컥 열리며 누군가 들어온다. 천 너머로 비친 상대의 얼굴은… "
                "**나카하라 츄야**다?! 아니, 잠깐. 이능력 「검은 집」 때문에 천 너머로 상대가 '가장 믿는 사람'이 보이는 건가, 아니면 진짜 츄야인가?\n\n"
                "\"어이, 기시. 아직도 자빠져 자고 있냐? 모리 보스께서 진료 시간 늦지 말라고 부르시던데.\""
            ),
            "choices": [
                {
                    "label": "1. (반말 유지) \"아, 시끄러워. 알아서 갈 테니까 넌 네 할 일이나 해.\"",
                    "deltas": {"suspicion": -3, "mastery": 5},
                    "set_cloth": True,
                    "result": (
                        "상대는 혀를 차더니 \"여전히 싸가지 없네\"라며 문을 닫고 나갔다. "
                        "아무래도 진짜 츄야가 아니라, 츄야를 가장 신뢰하는 말단 조직원이었던 모양이다. "
                        "일반인 습관대로 존댓말을 쓰지 않은 건 다행이다."
                    ),
                },
                {
                    "label": "2. (일반인 습관) \"아, 죄송합니다! 지금 바로 준비해서 가겠습니다!\"",
                    "deltas": {"suspicion": 22},
                    "set_cloth": True,
                    "result": (
                        "말을 내뱉자마자 조직원이 기겁한 듯 뒷걸음질 친다. "
                        "\"...뭐야, 너 어디 잘못 먹었냐? 기시가 존댓말을 다 하고?\" "
                        "9년 차 말단이 갑자기 공손해지자 공기가 싸늘해졌다. 정체 발각 위험이 올라갔다!"
                    ),
                },
                {
                    "label": "3. 천을 벗어 얼굴을 확인한다. (「검은 집」 발동)",
                    "deltas": {"suspicion": 10, "mastery": 10, "hp": -5},
                    "set_cloth": False,
                    "face": "나카하라 츄야(변신)",
                    "pronoun": "오레(俺)",
                    "result": (
                        "어둠에서 벗어나며 당신이 천을 걷자, 조직원의 얼굴이 사색이 되며 허리를 90도로 꺾는다. "
                        "\"츄, 츄야 님?! 여긴 어쩐 일로...!\" "
                        "당신의 얼굴이 상대가 가장 믿는 인물—나카하라 츄야로 변해버렸다. 능글맞게 넘기긴 했지만 기력이 소모됐다."
                    ),
                },
            ],
        },
        (1, 1): {
            "id": "shredder",
            "title": "DAY 1 오후 — 말단의 책상과 파쇄기",
            "text": (
                "포트 마피아 하부 사무실. 유스케의 책상 위에는 서류 뭉치가 수북이 쌓여 있고, "
                "그 옆에는 유난히 잘 관리된 **문서 파쇄기**가 놓여 있다.\n\n"
                "기억을 더듬어 보니, 유스케는 서류를 받자마자 파쇄기에 갈아버리는 인간이라 9년째 말단 신세를 못 면했다. "
                "주변 조직원들이 힐끔힐끔 당신의 눈치를 살피고 있다."
            ),
            "choices": [
                {
                    "label": "1. 고민 없이 서류 뭉치를 통째로 파쇄기에 처넣는다.",
                    "deltas": {"suspicion": -5, "hp": 3},
                    "result": (
                        "위이이잉—! 시원하게 갈려나가는 서류를 보며 주변 조직원들이 안도의 한숨(?)을 쉰다. "
                        "\"그래, 저래야 기시 유스케지.\" 쓸데없는 업무도 안 하고 의심도 피했다."
                    ),
                },
                {
                    "label": "2. 양심상 이러면 안 될 것 같아 꼼꼼히 분류해서 결재를 올린다.",
                    "deltas": {"suspicion": 20, "hp": -8},
                    "result": (
                        "서류를 내밀자 상급자가 소름 돋는다는 표정으로 당신을 쳐다본다. "
                        "\"기시, 너… 모리 보스한테 암살 지령이라도 받았냐? 왜 갑자기 일을 해?\" "
                        "열심히 일한 죄로 의심만 잔뜩 사고 체력만 빠졌다."
                    ),
                },
                {
                    "label": "3. 서류 절반만 파쇄하고, 나머지는 다른 사람 책상에 슬쩍 떠넘긴다.",
                    "deltas": {"suspicion": 2, "mastery": 5},
                    "result": (
                        "\"어차피 내 몫은 아니잖아?\" 유스케 특유의 이기적인 태도를 흉내 내며 자리를 떴다. "
                        "뒤에서 욕하는 소리가 들렸지만 아무도 이상하게 여기진 않는다."
                    ),
                },
            ],
        },
        (1, 2): {
            "id": "mori_clinic_1",
            "title": "DAY 1 밤 — 모리 오가이의 진료실",
            "text": (
                "보스실 안쪽 간이 진료실. 포트 마피아의 보스 **모리 오가이**가 하얀 가운을 걸친 채 생글생글 웃으며 주사기와 약봉지를 준비하고 있다.\n\n"
                "13살의 유스케를 주워 눈을 치료하고 집에 가둬 키웠던 장본인. 유스케는 모리를 일방적으로 혐오하고, 모리는 그 혐오를 즐긴다. "
                "시한부인 이 몸은 모리의 약 없이는 오래 버티지 못한다.\n\n"
                "\"유스케 군, 오늘도 기특하게 살아 있구나? 컨디션은 어때?\""
            ),
            "choices": [
                {
                    "label": "1. (혐오 티 내며 반말) \"보면 몰라? 모리 씨 얼굴 보니까 수명이 더 줄어드는 기분인데.\"",
                    "deltas": {"meds": 35, "hp": 10, "suspicion": -8},
                    "result": (
                        "모리가 쿡쿡 웃으며 만족스러운 듯 고개를 끄덕인다. "
                        "\"하하, 기운이 넘치는 걸 보니 아직 괜찮겠네. 자, 오늘 치 약이야. 얌전히 받아 가렴.\" "
                        "약물을 확보해 병세가 크게 안정되었다!"
                    ),
                },
                {
                    "label": "2. (위선자 연기) \"어머, 모리 씨도 참~ 걱정해 주는 척하기는. 약이나 내놔.\"",
                    "deltas": {"meds": 28, "hp": 5, "mastery": 6, "suspicion": -3},
                    "result": (
                        "모리가 흥미롭다는 듯 눈을 가늘게 뜬다. "
                        "\"여전히 속이 빤히 보이는 장난을 좋아하네. 그래도 약은 챙겨줄게.\" "
                        "무사히 진료를 마치고 약을 받아냈다."
                    ),
                },
                {
                    "label": "3. (긴장해서 깍듯하게) \"아, 보스님. 신경 써주셔서 감사합니다. 약 잘 먹겠습니다.\"",
                    "deltas": {"meds": 15, "suspicion": 28},
                    "result": (
                        "모리의 미소가 순식간에 차갑게 굳었다가 다시 부드러워진다. "
                        "\"...보스님? 유스케 군, 네가 나한테 그런 말을 쓰다니. 머리를 어딘가 세게 부딪힌 건 아니겠지?\" "
                        "등골이 서늘해지는 시선이 한참 동안 따라붙었다."
                    ),
                },
            ],
        },
        (3, 1): {
            "id": "real_chuuya",
            "title": "DAY 3 오후 — 진짜 나카하라 츄야와의 조우",
            "text": (
                "복도 모퉁이를 도는 순간, 익숙한 오렌지빛 머리카락과 검은 모자가 보인다. "
                "평소엔 천 너머로 온 마피아 조직원들이 다 츄야로 보여서 헷갈렸지만… 이 위압감과 걸음걸이는 **100% 진짜 나카하라 츄야**다!\n\n"
                "츄야가 미간을 찌푸리며 당신을 멈춰 세운다. "
                "\"어이, 기시. 아까부터 복도에서 어슬렁거리면서 뭘 쳐다보는 거야? 기분 나쁘게.\""
            ),
            "choices": [
                {
                    "label": "1. (적당히 짜증 내기) \"하아? 여기 사방에 네 얼굴이 널려 있어서 토 나올 것 같다고.\"",
                    "deltas": {"suspicion": -5, "hp": -5, "mastery": 5},
                    "result": (
                        "\"뭐, 뭐라고 이 자식이...?!\" 츄야가 주먹을 부르르 떨었지만, 이내 '저 녀석 능력 때문이지' 하고 깨달은 듯 혀를 차며 지나갔다. "
                        "유스케답게 불쾌감을 드러낸 덕분에 의심을 피했다."
                    ),
                },
                {
                    "label": "2. \"우와, 진짜 츄야 씨다! 사진이랑 똑같네요!\" (팬심 폭발)",
                    "deltas": {"suspicion": 35, "hp": -25},
                    "flag": "chuuya_warn",
                    "result": (
                        "\"...너 지금 돌았냐?\" 츄야의 이능력이 번쩍이며 당신이 벽에 처박혔다! "
                        "심지어 정체까지 의심받은 최악의 실수였다. 뼈가 부러지지 않은 게 다행이다."
                    ),
                },
                {
                    "label": "3. 천을 살짝 걷어 츄야의 반응을 본다. (위험한 도박)",
                    "deltas": {"hp": -35, "suspicion": 15, "mastery": 8},
                    "set_cloth": False,
                    "face": "츄야가 가장 신뢰하는 인물(혹은 다자이?)",
                    "result": (
                        "천을 걷자마자 츄야의 눈이 커지더니, 즉시 얼굴을 붉히며 발길질을 날렸다! "
                        "\"으악! 네놈, 누구 얼굴을 달고 장난질이야?!\" 누구의 얼굴로 변했는지 알 길은 없지만 죽을 뻔했다."
                    ),
                },
            ],
        },
        (4, 2): {
            "id": "dazai_encounter",
            "title": "DAY 4 밤 — 요코하마 뒷골목, 다자이 오사무",
            "text": (
                "밤바람을 쐬려 항구 근처 골목을 걷던 중, 강물 쪽을 바라보며 서 있는 모래색 코트의 사내와 마주쳤다. **다자이 오사무**다.\n\n"
                "유스케의 어릴 적 유일한 친구이자, 사상이 정반대라 서로 친구라고 생각하지도 않는 가장 위험한 존재. "
                "다자이가 고개를 돌려 천을 쓴 당신을 꿰뚫어 보듯 쳐다본다.\n\n"
                "\"어라? 이 죽지 못해 안달 난 기분 나쁜 기척은 유스케잖아? 오늘따라 공기가 조금 다른걸. 혹시 죽고 싶어졌니?\""
            ),
            "choices": [
                {
                    "label": "1. \"개소리 마, 다자이. 역겹고 의미 없는 삶이라도 죽는 것보단 낫거든.\"",
                    "deltas": {"suspicion": -10, "mastery": 10},
                    "result": (
                        "다자이가 지루하다는 듯 한숨을 내쉰다. "
                        "\"흥, 여전히 꽉 막힌 생존주의자네. 재미없어.\" "
                        "유스케의 핵심 대사를 완벽하게 받아친 덕분에 다자이의 의심을 완전히 따돌렸다!"
                    ),
                },
                {
                    "label": "2. \"솔직히 요즘 마피아 생활 너무 힘들어서 나도 가끔 그럴 때가 있어…\"",
                    "deltas": {"suspicion": 45},
                    "result": (
                        "다자이의 두 눈이 순식간에 서늘한 암흑으로 가라앉는다. "
                        "\"…잠깐. 유스케가 방금 '죽고 싶다' 비슷한 소리를 했나? 너, 안에 들어있는 게 누구지?\" "
                        "절체절명의 위기! 간신히 헛웃음으로 얼버무렸지만 다자이가 당신을 주시하기 시작했다."
                    ),
                },
                {
                    "label": "3. \"그건 그렇고, 츄야 키 얘기나 할까?\" (화제를 돌린다)",
                    "deltas": {"suspicion": 5, "mastery": 5},
                    "result": (
                        "다자이의 입꼬리가 씩 올라간다. "
                        "\"오~ 모처럼 호흡이 맞으려나? 어제 그 꼬맹이가 모자 가게에서 말이야…\" "
                        "잠깐 동안 츄야를 씹으며 위기를 넘겼지만, 다자이가 묘하게 당신을 뜯어본 느낌은 지울 수 없다."
                    ),
                },
            ],
        },
        (6, 1): {
            "id": "teacher_shadow",
            "title": "DAY 6 오후 — 총격전과 '선생님'의 그림자",
            "text": (
                "외부 심부름 중 하필 적대 조직의 습격에 휘말렸다. 폐허가 된 창고 구석에서 총탄이 빗발치는 와중, "
                "쓰러진 잔해 아래에 **어린아이 한 명**이 울며 갇혀 있는 것을 발견했다.\n\n"
                "일반인인 당신의 양심은 아이를 구하라고 소리치지만, 유스케의 기억이 머리를 울린다. "
                "유스케를 키웠던 '선생님'도 똑같이 아이들을 구하다가 죽었다. 그 후 유스케는 자기 목숨만 챙기는 이기적인 인간이 되었다."
            ),
            "choices": [
                {
                    "label": "1. 유스케답게 철저히 외면하고 내 살길만 찾아 도망친다.",
                    "deltas": {"suspicion": -10, "hp": -5, "mastery": 5},
                    "result": (
                        "가슴이 무겁고 죄책감이 밀려오지만, 몸은 유스케의 생존 본능대로 움직여 무사히 현장을 빠져나왔다. "
                        "뒤늦게 보고를 들은 마피아 쪽에선 아무도 당신을 의심하지 않았다."
                    ),
                },
                {
                    "label": "2. 무리해서 아이를 구하고 몰래 빠져나온다. (「검은 집」 활용)",
                    "deltas": {"hp": -22, "meds": -10, "mastery": 15, "suspicion": 12},
                    "set_cloth": False,
                    "face": "아이의 어머니(변신)",
                    "pronoun": "와타시(私)",
                    "result": (
                        "천을 벗어 아이가 가장 믿는 모습으로 변해 아이를 안심시키고 밖으로 끌어냈다. "
                        "허약한 몸에 무리가 가고 각혈이 났지만… 어쩐지 유스케의 마음속 깊은 곳(의외의 정)이 조금은 반응한 기분이 든다."
                    ),
                },
                {
                    "label": "3. \"누가 나 좀 살려줘!\" 미끼로 적의 시선을 돌려 틈을 만든다.",
                    "deltas": {"hp": -12, "suspicion": 5, "mastery": 8},
                    "result": (
                        "위선적인 연기와 소란으로 적들의 주의를 끌어 간신히 아수라장을 빠져나왔다. "
                        "아이도 덩달아 구출된 듯하다. 몸은 좀 다쳤지만 나쁘지 않은 결과다."
                    ),
                },
            ],
        },
        (7, 2): {
            "id": "final_night",
            "title": "DAY 7 밤 — 마지막 진료와 거울 속의 진실",
            "text": (
                "일주일째의 밤. 당신은 무사히 일주일을 버텨내기 직전이다. "
                "모리 오가이의 진료실, 어두운 거울 앞에 앉아 천을 벗자 거울 속에는 우리가 아는 짧은 투톤 머리의 '유스케'가 비친다.\n\n"
                "문득, 그 얼굴조차 진짜 유스케의 얼굴이 아니라는 위화감이 스친다. 어둠의 틈새로 흑발과 흑안, 긴 뒷머리의 잔상이 어른거리는 것 같다.\n\n"
                "그때 모리가 조용히 뒤로 다가와 링거 줄을 점검하며 속삭인다.\n"
                "\"유스케 군. 일주일 동안 꽤 흥미롭게 지켜봤단다. 자, 마지막으로 물어볼까. **너는 살아남을 준비가 되어 있니?**\""
            ),
            "choices": [
                {
                    "label": "1. \"쓸데없는 소리 말고 약이나 놔, 모리 씨. 난 무슨 짓을 해서든 살 거니까.\"",
                    "deltas": {"meds": 25, "suspicion": -5, "mastery": 10},
                    "result": (
                        "모리가 옅게 웃으며 약을 주입한다. "
                        "\"그래, 그 집착이야말로 네가 내 곁에 남아 있는 이유지.\" "
                        "위태로웠던 일주일의 밤이 마침내 지나간다."
                    ),
                },
                {
                    "label": "2. \"모리 씨야말로 나 죽으면 심심할 텐데. 앞으로도 잘 부탁해?\"",
                    "deltas": {"meds": 20, "mastery": 15, "suspicion": -8},
                    "result": (
                        "모리가 작게 박수를 치며 웃는다. "
                        "\"아하하, 이제는 나를 다루는 법까지 터득한 모양이구나! 좋아, 아주 좋아.\" "
                        "모리의 호감을(어긋난 형태로) 완벽히 확보했다."
                    ),
                },
                {
                    "label": "3. 거울 속 진짜 얼굴에 대한 단서를 더듬으며 조용히 입을 다문다.",
                    "deltas": {"meds": 10, "mastery": 18, "suspicion": 8},
                    "result": (
                        "침묵 속에 모리가 의미심장한 미소를 짓고는 주사를 놔준다. "
                        "「검은 집」의 본질과 유스케라는 인간의 비밀에 한 걸음 더 가까워진 채 밤이 깊어간다."
                    ),
                },
            ],
        },
    }


def get_pool_events():
    return [
        {
            "id": "akane_bump",
            "title": "복도의 불시 충돌 — 아카네",
            "text": (
                "천을 쓴 채 복도를 걷고 있는데… 분명 앞이 텅 비어 있었다. "
                "그런데 **쿵!** 하고 누군가와 정면으로 부딪혀 바닥에 나뒹굴었다!\n\n"
                "모리의 집에서 함께 자란 유사 가족 **아카네**다. 아무도 믿지 못하는 아카네의 시선엔 유스케의 머리가 보이지 않고, "
                "천을 쓴 유스케의 눈에도 아카네가 보이지 않기에 늘 일어나는 참사다.\n\n"
                "\"...아파. 기시, 앞 좀 보고 걸어.\" (사실 앞을 봐도 안 보이지만)"
            ),
            "choices": [
                {
                    "label": "1. \"너도 안 보이긴 마찬가지잖아. 조심 좀 해, 아카네.\"",
                    "deltas": {"hp": -4, "suspicion": -6},
                    "result": (
                        "아카네가 조용히 고개를 끄덕이며 먼지를 털고 일어난다. "
                        "서로 별 생각이 없어서인지 오히려 가장 편하고 자연스러운 대화였다."
                    ),
                },
                {
                    "label": "2. \"미안! 많이 다쳤어? 괜찮아?\" (과하게 걱정한다)",
                    "deltas": {"hp": -4, "suspicion": 16},
                    "result": (
                        "아카네가 멍하니 당신을 보다가 고개를 갸웃거린다. "
                        "\"...갑자기 왜 그래? 기분 나쁘게 상냥한 척하지 마.\" "
                        "평소와 다른 다정함에 아카네가 경계심을 세웠다."
                    ),
                },
            ],
        },
        {
            "id": "shohei_lunch",
            "title": "식당의 함정 — 쇼헤이와 점심시간",
            "text": (
                "구내식당에서 마주친 **쇼헤이**. 투톤 머리에 한쪽 눈을 실명했고, 겉과 속이 다르다는 점까지 유스케와 닮은 구석이 많은 인물이다.\n\n"
                "쇼헤이가 한숨을 쉬더니 당신 앞에 김이 모락모락 나는 매운 마늘 카레를 밀어 놓는다. "
                "잠깐—유스케의 프로필에 **'싫어하는 것: 향이 강한 음식'**이라고 적혀 있던 게 번뜩 떠오른다!"
            ),
            "choices": [
                {
                    "label": "1. \"야, 내가 냄새 지독한 거 싫어하는 거 알면서 일부러 이러지?!\" (투덜대며 뺀다)",
                    "deltas": {"suspicion": -6, "hp": 5},
                    "result": (
                        "쇼헤이가 피식 웃으며 쟁반을 가져간다. "
                        "\"여전히 까다롭네. 자, 여기 맹숭맹숭한 죽이나 드시지.\" "
                        "쇼헤이와의 호흡도 맞추고 속이 뒤집히는 것도 막았다!"
                    ),
                },
                {
                    "label": "2. 아까워서 그냥 한 입 크게 떠먹는다.",
                    "deltas": {"hp": -16, "meds": -6, "suspicion": 14},
                    "result": (
                        "강렬한 향신료 냄새가 코를 찌르자마자 구역질이 치밀어 올랐다! "
                        "쇼헤이가 눈을 휘둥그레 뜬다. \"너 진짜 미쳤어? 그걸 왜 먹어?\""
                    ),
                },
            ],
        },
        {
            "id": "chuuya_hallway",
            "title": "사방이 츄야인 지옥",
            "text": (
                "오늘따라 포트 마피아 본부 복도에 사람이 많다. 그런데 천 너머로 보이는 얼굴들이 **전부 다 나카하라 츄야**다.\n\n"
                "마피아 말단들이 가장 믿는 사람이 츄야이기 때문에 벌어지는 「검은 집」의 부작용이다. "
                "어깨가 부딪힌 한 츄야(?)가 당신을 노려보며 말을 건다."
            ),
            "choices": [
                {
                    "label": "1. 눈을 질끈 감고 무시한 채 빠르게 자리를 뜬다.",
                    "deltas": {"suspicion": -2, "hp": -3},
                    "result": (
                        "\"뭐야 저 기분 나쁜 놈은...\" 하는 소리를 뒤로하고 무사히 화장실로 도피했다. "
                        "멘탈이 살짝 깎였지만 안전하다."
                    ),
                },
                {
                    "label": "2. (목소리를 잘 들어보고) 말단 직원 같으니 뻔뻔하게 심부름을 시킨다.",
                    "deltas": {"mastery": 8, "suspicion": 3},
                    "result": (
                        "목소리를 구분해 진짜 츄야가 아님을 간파하고, 내 몫의 잡일을 떠넘겼다! "
                        "이기적인 유스케다운 처세술이었다."
                    ),
                },
            ],
        },
        {
            "id": "mirror_truth",
            "title": "거울 앞의 고독한 밤",
            "text": (
                "아무도 없는 숙소. 당신은 얼굴을 덮은 답답한 천을 벗고 세면대 거울 앞에 섰다.\n\n"
                "거울이나 아무도 없을 때 어둠에서 벗어나면, 다음 능력을 쓸 때까지 유스케 본연의(것으로 알려진) 얼굴로 고정된다. "
                "거울 속 22세의 얼굴을 보며 숨을 고른다. 문득 이능력의 작동 원리가 조금 더 손에 잡히는 듯하다."
            ),
            "choices": [
                {
                    "label": "1. 거울을 보며 유스케의 비웃는 표정과 '보쿠' 말투를 연습한다.",
                    "deltas": {"suspicion": -8, "mastery": 10},
                    "set_cloth": False,
                    "face": "유스케(위장된 본얼굴)",
                    "pronoun": "보쿠(僕)",
                    "result": (
                        "\"죽는 것보다야 낫지~\" 비뚤어진 미소와 1인칭 '보쿠'를 입에 붙이자 위화감이 줄어들었다. "
                        "잠시 천을 벗고 숨을 돌렸으니 다시 쓸 준비를 하자."
                    ),
                },
                {
                    "label": "2. 가만히 눈을 감고 체력을 회복하며 휴식을 취한다.",
                    "deltas": {"hp": 15, "meds": -3},
                    "set_cloth": True,
                    "result": (
                        "짧지만 꿀 같은 휴식을 취해 체력이 어느 정도 회복되었다. "
                        "내일을 버틸 힘이 조금 생겼다."
                    ),
                },
            ],
        },
        {
            "id": "cloth_slip_pronoun",
            "title": "돌발 상황 — 천이 벗겨졌다!",
            "text": (
                "문서에 발이 걸려 넘어지는 바람에 머리의 천이 훌러덩 벗겨지고 말았다! "
                "하필 앞에 서 있던 중견 간부 한 명이 당신과 정면으로 눈이 마주쳤다.\n\n"
                "상대가 화들짝 놀라며 외친다. \"아, **코요 님**?! 여긴 어쩐 일로...\"\n"
                "큰일이다. 당신은 지금 오자키 코요의 얼굴로 변해버린 듯하다! 유스케는 변신한 외형에 따라 1인칭을 바꿔 연기하곤 했다."
            ),
            "choices": [
                {
                    "label": "1. 우아하게 미소 지으며 '와타시(私)' 1인칭으로 속삭이고 유유히 사라진다.",
                    "deltas": {"mastery": 14, "suspicion": -4},
                    "set_cloth": False,
                    "face": "오자키 코요(변신)",
                    "pronoun": "와타시(私)",
                    "result": (
                        "\"훗, 신경 쓰지 말게. 잠깐 바람을 쐬러 나왔을 뿐이니.\" "
                        "완벽한 연기력에 간부가 깍듯이 고개를 숙였다! 모퉁이를 돌자마자 천을 다시 뒤집어썼다."
                    ),
                },
                {
                    "label": "2. 당황해서 '보쿠(僕)'라고 말하며 허둥지둥 천을 주워 쓴다.",
                    "deltas": {"suspicion": 22, "hp": -5},
                    "set_cloth": True,
                    "result": (
                        "\"어, 어라? 코요 님이 왜 보쿠라고…?\" 간부가 기겁하며 얼굴을 붉히다 이상함을 눈치챘다! "
                        "겨우 도망쳤지만 소문이 흉흉하게 퍼질 것 같다."
                    ),
                },
            ],
        },
        {
            "id": "mafia_debt_bluff",
            "title": "전투력 0의 협박 임무",
            "text": (
                "상납금을 미룬 하청업자를 압박하라는 말단 심부름을 받았다. "
                "문제는 유스케의 전투 능력이 **거의 제로(0)**에 가깝다는 것. 덩치 큰 업자가 쇠파이프를 들고 버티고 있다."
            ),
            "choices": [
                {
                    "label": "1. \"내 뒤엔 포트 마피아 보스랑 '그분'이 있는데, 목숨 아까우면 내놓지?\"",
                    "deltas": {"mastery": 8, "suspicion": -3},
                    "result": (
                        "천을 쓴 기괴한 행색과 태연한 협박에 겁을 먹은 업자가 돈을 순순히 내놓았다. "
                        "폭력 없이 살아남는 것도 생존주의자의 기술이다."
                    ),
                },
                {
                    "label": "2. \"죄송한데, 저도 살려고 이러는 거라...\" 사정해 본다.",
                    "deltas": {"hp": -20, "suspicion": 12},
                    "result": (
                        "약점을 잡힌 업자가 쇠파이프를 휘둘렀다! 간신히 도망쳤지만 크게 다쳤고 마피아 체면도 구겼다."
                    ),
                },
            ],
        },
        {
            "id": "cough_attack",
            "title": "한계를 알리는 기침",
            "text": (
                "계단을 오르던 중 갑자기 폐가 찢어질 듯한 기침이 터져 나온다. "
                "손수건에 붉은 핏방울이 번진다. 유스케의 시한부 몸이 슬슬 한계를 드러내고 있다."
            ),
            "choices": [
                {
                    "label": "1. 비상용 진통제를 삼키고 구석에서 숨을 고른다.",
                    "deltas": {"hp": -8, "meds": 12},
                    "result": (
                        "쓴 약을 삼키자 당장의 발작은 가라앉았다. 역시 모리의 약 없이는 버티기 힘든 몸이다."
                    ),
                },
                {
                    "label": "2. 아무 일 없는 척 버티며 임무지로 향한다.",
                    "deltas": {"hp": -18, "meds": -8, "suspicion": -4},
                    "result": (
                        "무리는 했지만 주변에 약한 모습을 보이지 않았다. 다만 몸 상태가 눈에 띄게 나빠졌다."
                    ),
                },
            ],
        },
        {
            "id": "mori_extra_meds",
            "title": "보스실에서의 은밀한 거래",
            "text": (
                "모리 오가이가 간식을 먹으며 당신을 불렀다. 책상 위에는 고급 영양제와 추가 약병이 놓여 있다.\n"
                "\"유스케 군, 오늘따라 안색이 안 좋아 보이는걸? 내게 어리광이라도 부려보면 약을 더 줄 수도 있는데~?\""
            ),
            "choices": [
                {
                    "label": "1. \"징그러운 소리 집어치워, 모리 씨. 줄 거면 빨리 내놓고 꺼지라 그래.\"",
                    "deltas": {"meds": 24, "hp": 8, "suspicion": -6},
                    "result": (
                        "모리가 껄껄 웃으며 약병을 던져주었다. 역시 모리에겐 혐오를 퍼붓는 게 제일 잘 먹힌다."
                    ),
                },
                {
                    "label": "2. 자존심을 버리고 \"모리 씨, 부탁이야. 약 좀 더 줘.\" 라고 말한다.",
                    "deltas": {"meds": 28, "suspicion": 18},
                    "result": (
                        "약은 두둑이 챙겼지만, 모리가 묘한 눈빛으로 당신을 관찰하기 시작했다. "
                        "\"네가 그런 순한 소리를 하다니… 비가 오려나?\""
                    ),
                },
            ],
        },
        {
            "id": "hypocrite_tease",
            "title": "양치기 소년의 연기",
            "text": (
                "신입 조직원이 잔뜩 긴장한 채 서류를 나르고 있다. "
                "원래 유스케는 상냥한 척하며 남을 놀려먹는 걸 좋아하는 위선자지만, 다들 속지 않아서 '양치기 소년' 취급을 받는다."
            ),
            "choices": [
                {
                    "label": "1. \"어머~ 힘들어 보이네? 내가 들어줄까?\" 하고 말한 뒤 바닥에 떨어뜨린다.",
                    "deltas": {"suspicion": -8, "mastery": 4},
                    "result": (
                        "\"역시 기시 선배는 최악이야!\" 신입이 울먹이며 도망갔다. "
                        "양심은 찔리지만 완벽한 유스케 연기였다."
                    ),
                },
                {
                    "label": "2. 진심으로 서류를 들어주며 격려한다.",
                    "deltas": {"suspicion": 18, "hp": -4},
                    "result": (
                        "신입이 오히려 함정인 줄 알고 비명을 지르며 도망갔다. "
                        "\"기시 선배가 착하게 굴어! 뭔가 꿍꿍이가 있어!\" 소문만 이상해졌다."
                    ),
                },
            ],
        },
        {
            "id": "confinement_dream",
            "title": "감금 시절의 기억",
            "text": (
                "쪽잠을 자던 중 유스케의 오래된 악몽이 덮친다. "
                "어릴 적 모리의 집에 갇혀 약을 먹으며 지내던 답답한 방. 붉은 피와 선생님의 마지막 목소리가 귓가를 맴돈다."
            ),
            "choices": [
                {
                    "label": "1. \"...난 살아있어. 죽은 건 그 사람이지, 내가 아니야.\" 현실을 자각한다.",
                    "deltas": {"hp": 5, "mastery": 8},
                    "result": (
                        "식의 땀을 닦고 일어났다. 유스케의 지독한 생존 집착을 조금 더 이해하게 된 기분이다."
                    ),
                },
                {
                    "label": "2. 악몽에 짓눌려 식은땀을 흘리며 밤을 새운다.",
                    "deltas": {"hp": -12, "meds": -6},
                    "result": (
                        "수면을 전혀 취하지 못해 몸이 천근만근이다."
                    ),
                },
            ],
        },
        {
            "id": "akane_tea",
            "title": "아카네와의 조용한 티타임",
            "text": (
                "옥상 구석에서 아카네가 캔 커피를 마시고 있다. 아카네는 당신을 믿어서가 아니라, 별 생각이 없어서 우호적이다. "
                "마피아 안에서 유일하게 긴장을 풀 수 있는 시간일지도 모른다."
            ),
            "choices": [
                {
                    "label": "1. 옆에 조용히 앉아 아무 말 없이 바람을 쐰다.",
                    "deltas": {"hp": 14, "suspicion": -5},
                    "result": (
                        "아무도 서로를 캐묻지 않는 고요한 시간. 지친 몸과 멘탈이 조금 회복되었다."
                    ),
                },
                {
                    "label": "2. \"아카네, 요즘 나 좀 이상해 보이지 않아?\" 슬쩍 떠본다.",
                    "deltas": {"suspicion": 10, "hp": 5},
                    "result": (
                        "아카네가 캔을 내려놓으며 말했다. \"원래부터 이상했잖아. 갑자기 왜 물어?\" "
                        "다행히 크게 의심하진 않았지만 괜히 긁어 부스럼을 만들 뻔했다."
                    ),
                },
            ],
        },
        {
            "id": "shohei_banter",
            "title": "쇼헤이의 날카로운 눈",
            "text": (
                "서류 창고에서 마주친 쇼헤이가 한쪽 눈을 가늘게 뜨며 당신을 훑어본다.\n"
                "\"야, 너 요 며칠 사리 분별이 좀 빨라진 것 같다? 멍 때리는 시간도 늘었고. 설마 큰 병이라도 도졌냐?\""
            ),
            "choices": [
                {
                    "label": "1. \"내가 언제부터 바보였다고 그래? 쇼헤이 너야말로 주름 늘었네.\"",
                    "deltas": {"suspicion": -6, "mastery": 5},
                    "result": (
                        "쇼헤이가 질렸다는 듯 한숨을 푹 쉰다. \"아 예, 그러시겠죠.\" 가벼운 말장난으로 위기를 넘겼다."
                    ),
                },
                {
                    "label": "2. \"응, 사실 요즘 좀 어지럽긴 해.\" 솔직히 털어놓는다.",
                    "deltas": {"suspicion": 8, "hp": 8},
                    "result": (
                        "쇼헤이가 잠시 멈칫하더니 진통제 한 알을 던져준다. \"관리 좀 해라. 모리 씨한테 또 끌려가기 싫으면.\""
                    ),
                },
            ],
        },
        {
            "id": "ability_experiment",
            "title": "「검은 집」 연습하기",
            "text": (
                "적적한 오후, 어둠 속에서 천 너머로 사물을 보는 감각에 집중해 본다. "
                "이 몸의 무기는 싸움 실력이 아니라 오직 이 기묘한 이능력뿐이다."
            ),
            "choices": [
                {
                    "label": "1. 천을 통해 지나가는 사람들의 실루엣과 반응 속도를 익힌다.",
                    "deltas": {"mastery": 14, "hp": -5},
                    "result": (
                        "시야가 한쪽뿐인 상태에서도 거리 감각을 꽤 익혔다. 이능력 제어력이 눈에 띄게 올랐다!"
                    ),
                },
                {
                    "label": "2. 무리하지 말고 오늘은 그냥 낮잠이나 잔다.",
                    "deltas": {"hp": 12, "suspicion": -2},
                    "result": (
                        "마피아 9년 차 말단답게 땡땡이를 치며 체력을 아꼈다."
                    ),
                },
            ],
        },
        {
            "id": "rainy_yokohama",
            "title": "비 오는 요코하마의 갈림길",
            "text": (
                "비가 쏟아지는 골목길, 자살 기도자처럼 보이는 남자가 다리 난간 위에서 위태롭게 서 있다. "
                "일반인의 시선으론 구해야 할 사람이고, 유스케의 신조는 '타살은 기회, 자살은 권리 포기! 역겨워도 살아가라'다."
            ),
            "choices": [
                {
                    "label": "1. \"야, 뛰어내릴 거면 남 안 보이는 데서 해! 죽는 것보다 사는 게 낫다고!\" (독설 후 끌어내림)",
                    "deltas": {"hp": -8, "suspicion": -5, "mastery": 8},
                    "result": (
                        "역설적이게도 유스케다운 험한 말로 사람을 살렸다. 비에 좀 젖었지만 기분은 나쁘지 않다."
                    ),
                },
                {
                    "label": "2. 남의 권리 포기까지 간섭할 틈이 없다며 그냥 지나친다.",
                    "deltas": {"suspicion": -3, "hp": 2},
                    "result": (
                        "냉정하게 발걸음을 돌렸다. 이 세계에서 오래 살려면 마음을 닫는 법도 배워야 한다."
                    ),
                },
            ],
        },
        {
            "id": "mori_errand_paper",
            "title": "모리의 이상한 심부름",
            "text": (
                "모리 보스가 밀봉된 편지 한 통을 건네며 무장탐정사 관할 경계선의 우체통에 넣고 오라고 한다. "
                "괜히 탐정사 인물과 마주치면 끝장인데…"
            ),
            "choices": [
                {
                    "label": "1. 천을 깊게 눌러쓰고 그림자처럼 움직여 우편물만 넣고 빠진다.",
                    "deltas": {"mastery": 8, "hp": -6},
                    "result": (
                        "누구와도 마주치지 않고 무사히 심부름을 완수했다!"
                    ),
                },
                {
                    "label": "2. 귀찮아서 길가의 부랑자에게 돈을 주고 대신 넣게 시킨다.",
                    "deltas": {"suspicion": 10, "hp": 2},
                    "result": (
                        "편지는 들어간 듯하지만, 나중에 모리가 이 사실을 알면 흥미로워할지 화낼지 모를 일이다."
                    ),
                },
            ],
        },
    ]


ENDINGS = {
    "ending_true": {
        "title": "👑 [진 엔딩] 검은 집의 주인 — 완벽한 생존자",
        "text": (
            "일주일이 지났다. 당신은 모리의 의심도, 다자이의 예리한 시선도, 츄야의 분노도 모두 피해 냈다.\n\n"
            "뿐만 아니라 「검은 집」의 감각을 완전히 손에 익혀, 이제는 천 너머의 왜곡된 얼굴들 속에서도 "
            "누가 적이고 누가 아군인지 정확히 꿰뚫어 본다.\n\n"
            "거울 앞, 잠시 스쳐 간 흑발 흑안의 진짜 얼굴을 떠올리며 당신은 유스케 특유의 비뚤어진 미소를 짓는다.\n"
            "**\"역겹고 의미 없는 삶이라도… 이 정도면 제법 살 만하잖아?\"**"
        ),
    },
    "ending_survive": {
        "title": "🕶️ [생존 엔딩] 살아가는 것만으로도 수고했어!",
        "text": (
            "아슬아슬하고 엉망진창이었지만, 어쨌든 당신은 포트 마피아에서 일주일을 버텨냈다!\n\n"
            "가끔 아카네와 부딪히고, 쇼헤이에게 잔소리를 듣고, 모리의 약을 받아 마시며 "
            "여전히 9년 차 말단으로 파쇄기 앞을 지키는 나날.\n\n"
            "언제 정체가 들킬지 모르는 살얼음판이지만, 적어도 오늘 당신은 살아 있다. "
            "유스케의 말처럼, 죽어버리는 것보다 살아가는 것이 더 나으니까."
        ),
    },
    "ending_caught": {
        "title": "💀 [배드 엔딩 1] 양치기 소년의 가면이 벗겨지다",
        "text": (
            "위화감이 한계치를 넘어버렸다.\n\n"
            "어느 날 밤, 당신의 숙소 문이 열리고 모리 오가이—혹은 다자이 오사무가 서늘한 눈빛으로 당신을 내려다본다.\n"
            "**\"유스케는 그런 표정을 짓지 않아. 자, 네 몸 안에 들어앉은 낯선 손님과 이야기를 좀 해볼까?\"**\n\n"
            "포트 마피아의 지하 심문실로 끌려가는 것으로 당신의 짧은 빙의 생존기는 막을 내렸다."
        ),
    },
    "ending_hp": {
        "title": "🩸 [배드 엔딩 2] 부서진 유리 몸",
        "text": (
            "원래부터 허약했던 유스케의 신체가 누적된 부상과 무리를 견디지 못하고 무너졌다.\n\n"
            "어두운 복도 한구석, 천이 벗겨진 채 쓰러진 당신의 귓가로 멀어지는 발소리가 들린다. "
            "포트 마피아의 말단은 그렇게 조용히 생을 마감했다."
        ),
    },
    "ending_meds": {
        "title": "⏳ [배드 엔딩 3] 시한부의 끝",
        "text": (
            "모리의 진료와 약물 관리를 소홀히 한 대가가 찾아왔다.\n\n"
            "폐가 타는 듯한 고통과 함께 시야가 붉게 물든다. "
            "그토록 살기를 갈망했던 유스케의 몸에서, 정작 약 하나 제때 챙기지 못해 숨이 멎어가고 있다."
        ),
    },
}


# ---------------------------------------------------------
# 3. 상태 초기화 및 턴 진행 로직
# ---------------------------------------------------------
def clamp(val, low=0, high=100):
    return max(low, min(high, val))


def init_game():
    st.session_state.phase = "title"  # title | playing | result | ending
    st.session_state.day = 1
    st.session_state.slot = 0  # 0: 오전, 1: 오후, 2: 밤
    st.session_state.hp = 75
    st.session_state.meds = 70
    st.session_state.suspicion = 10
    st.session_state.mastery = 15
    st.session_state.cloth_on = True
    st.session_state.current_face = "천 착용 중 (시야 왜곡)"
    st.session_state.pronoun = "보쿠(僕)"
    st.session_state.used_pool = []
    st.session_state.logs = []
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


def check_bad_ending():
    if st.session_state.suspicion >= 100:
        return "ending_caught"
    if st.session_state.hp <= 0:
        return "ending_hp"
    if st.session_state.meds <= 0:
        return "ending_meds"
    return None


def handle_choice(choice_idx):
    event = st.session_state.current_event
    choice = event["choices"][choice_idx]
    deltas = choice.get("deltas", {})

    st.session_state.hp = clamp(st.session_state.hp + deltas.get("hp", 0))
    st.session_state.meds = clamp(st.session_state.meds + deltas.get("meds", 0))
    st.session_state.suspicion = clamp(
        st.session_state.suspicion + deltas.get("suspicion", 0)
    )
    st.session_state.mastery = clamp(
        st.session_state.mastery + deltas.get("mastery", 0)
    )

    if "set_cloth" in choice:
        st.session_state.cloth_on = choice["set_cloth"]
        if choice["set_cloth"]:
            st.session_state.current_face = "천 착용 중 (시야 왜곡)"
            st.session_state.pronoun = "보쿠(僕)"
    if "face" in choice:
        st.session_state.current_face = choice["face"]
    if "pronoun" in choice:
        st.session_state.pronoun = choice["pronoun"]

    # 변화량 배지 생성
    label_map = {
        "hp": "체력",
        "meds": "병세 안정",
        "suspicion": "위화감",
        "mastery": "이능력 숙련",
    }
    delta_texts = []
    for k, v in deltas.items():
        if v != 0:
            sign = "+" if v > 0 else ""
            delta_texts.append((k, f"{label_map[k]} {sign}{v}"))

    st.session_state.logs.insert(
        0,
        f"[DAY {st.session_state.day} {SLOTS[st.session_state.slot]}] {event['title']} → {choice['label']}",
    )

    bad = check_bad_ending()
    if bad:
        st.session_state.ending_key = bad
        st.session_state.last_result = {
            "text": choice["result"],
            "deltas": delta_texts,
        }
        st.session_state.phase = "ending"
    else:
        st.session_state.last_result = {
            "text": choice["result"],
            "deltas": delta_texts,
        }
        st.session_state.phase = "result"


def next_turn():
    st.session_state.slot += 1
    if st.session_state.slot >= 3:
        st.session_state.slot = 0
        st.session_state.day += 1

        # 하루가 지날 때마다 시한부 병세 자연 감소
        if st.session_state.day <= 7:
            st.session_state.meds = clamp(st.session_state.meds - 18)
            if st.session_state.meds <= 20:
                st.session_state.hp = clamp(st.session_state.hp - 10)

    bad = check_bad_ending()
    if bad:
        st.session_state.ending_key = bad
        st.session_state.phase = "ending"
        return

    if st.session_state.day > 7:
        if (
            st.session_state.suspicion <= 30
            and st.session_state.mastery >= 55
            and st.session_state.hp >= 40
        ):
            st.session_state.ending_key = "ending_true"
        else:
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
# 4. 사이드바 (기시 유스케 상태창)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🕶️ 기시 유스케 (貴志祐介)")
    st.caption("포트 마피아 9년 차 말단 | 22세 | 시한부")
    st.divider()

    st.markdown(
        f"**📅 생존 일정:** `DAY {min(st.session_state.day, 7)} / 7` ({SLOTS[st.session_state.slot]})"
    )
    st.markdown(f"**🎭 현재 외형:** `{st.session_state.current_face}`")
    st.markdown(f"**🗣️ 권장 1인칭:** `{st.session_state.pronoun}`")

    st.write("")
    st.markdown(f"**❤️ 체력 (HP): {st.session_state.hp} / 100**")
    st.progress(st.session_state.hp / 100)

    st.markdown(f"**💊 병세 안정도 (약효): {st.session_state.meds} / 100**")
    st.progress(st.session_state.meds / 100)

    st.markdown(f"**⚠️ 정체 위화감: {st.session_state.suspicion} / 100**")
    st.progress(st.session_state.suspicion / 100)

    st.markdown(f"**🔮 「검은 집」 숙련도: {st.session_state.mastery} / 100**")
    st.progress(st.session_state.mastery / 100)

    st.divider()
    with st.expander("📖 생존 수칙 메모", expanded=False):
        st.markdown(
            "- **말투:** 보스(모리) 포함 누구에게나 **반말**.\n"
            "- **업무:** 서류는 파쇄기행. 성실하면 의심받음.\n"
            "- **체질:** 향 강한 음식 금지. 시한부라 약 필수.\n"
            "- **이능력:** 천을 벗으면 상대가 가장 믿는 자로 변신."
        )

    st.button("🔄 처음부터 다시 시작", on_click=init_game, key="reset_btn")


# ---------------------------------------------------------
# 5. 메인 화면 렌더링
# ---------------------------------------------------------
st.title("🔪 기시 유스케 빙의 생존기")
st.caption("문호 스트레이 독스 기반 텍스트 서바이벌 | 7일간 정체를 들키지 않고 살아남아라")

# [1] 타이틀 화면
if st.session_state.phase == "title":
    st.markdown(
        """
        <div class="story-box">
        <strong>"타살은 기회, ■■은 권리 포기! 역겹고 의미 없는 삶이라도 살아가도록 해."</strong><br><br>
        눈을 떠보니 당신은 요코하마 포트 마피아 소속의 시한부 말단, <strong>기시 유스케</strong>의 몸에 들어와 있습니다.<br>
        전투력은 0에 가깝고, 사방이 적이며, 보스에게도 반말을 찍찍 내뱉어야 정체를 안 들킵니다.<br><br>
        과연 당신은 <strong>7일 동안</strong> 시한부 몸을 건사하고, 다자이와 모리, 츄야 사이에서 무사히 살아남을 수 있을까요?
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.button("▶ 눈을 뜬다 (게임 시작)", on_click=start_game, key="start_btn")

# [2] 이벤트 선택 화면
elif st.session_state.phase == "playing":
    ev = st.session_state.current_event
    st.subheader(ev["title"])
    formatted_text = ev["text"].replace("\n", "<br>")
    st.markdown(
        f'<div class="story-box">{formatted_text}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("**어떻게 행동할까?**")
    for idx, ch in enumerate(ev["choices"]):
        st.button(
            ch["label"],
            on_click=handle_choice,
            args=(idx,),
            key=f"choice_{st.session_state.day}_{st.session_state.slot}_{idx}",
        )

# [3] 행동 결과 화면
elif st.session_state.phase == "result":
    res = st.session_state.last_result
    badges_html = ""
    for k, txt in res["deltas"]:
        is_bad = (k == "suspicion" and "+" in txt) or (
            k in ("hp", "meds") and "-" in txt
        )
        cls = "badge badge-warn" if is_bad else "badge badge-good"
        badges_html += f'<span class="{cls}">{txt}</span>'

    formatted_res = res["text"].replace("\n", "<br>")
    st.markdown(
        f'<div class="result-box">{formatted_res}<br><br>{badges_html}</div>',
        unsafe_allow_html=True,
    )
    st.button("다음 일정으로 ▶", on_click=next_turn, key="next_btn")

# [4] 엔딩 화면
elif st.session_state.phase == "ending":
    if st.session_state.last_result:
        st.info(st.session_state.last_result["text"])

    end = ENDINGS[st.session_state.ending_key]
    formatted_end = end["text"].replace("\n", "<br>")
    st.markdown(
        f"""
        <div class="ending-box">
        <h3>{end['title']}</h3>
        <hr style="border-color: #4a2427;">
        {formatted_end}
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("생존 일수", f"{min(st.session_state.day, 7)}일")
    col2.metric("최종 체력", f"{st.session_state.hp}")
    col3.metric("위화감", f"{st.session_state.suspicion}%")
    col4.metric("「검은 집」 숙련", f"{st.session_state.mastery}%")

    st.button("🔄 다시 도전하기", on_click=start_game, key="retry_btn")

# 최근 진행 로그
if st.session_state.logs:
    with st.expander("📜 최근 행동 기록", expanded=False):
        for log in st.session_state.logs[:10]:
            st.text(log)
