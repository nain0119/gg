
import json
import random
import streamlit as st

st.set_page_config(
    page_title="BLACK HOUSE — 기시 유스케",
    page_icon="🌑",
    layout="wide",
)

# ==========================================
# BLACK HOUSE — YUSUKE KISHI
# Streamlit RPG
# ==========================================

INITIAL_STATE = {
    "day": 1,
    "slot": 0,
    "hp": 65,
    "mind": 80,
    "ability": 90,
    "reputation": 25,
    "work": 15,
    "survival": 100,
    "money": 3000,
    "relations": {
        "모리 오가이": -85,
        "다자이 오사무": -35,
        "나카하라 츄야": -70,
        "아카네": 25,
        "쇼헤이": 25,
    },
    "flags": {
        "dazai_talks": 0,
        "mori_deal": False,
        "intro_seen": False,
    },
    "log": ["DAY 01 — 요코하마의 아침이 시작되었다."],
    "ending": None,
}

STAT_NAMES = {
    "hp": "체력",
    "mind": "정신력",
    "ability": "이능력 숙련도",
    "reputation": "평판",
    "work": "업무 성실도",
    "survival": "생존 의지",
}

TIME_NAMES = [
    "09:00 AM",
    "12:00 PM",
    "03:00 PM",
    "06:00 PM",
    "09:00 PM",
]

PHASES = [
    "MORNING",
    "NOON",
    "AFTERNOON",
    "EVENING",
    "NIGHT",
]


# ==========================================
# GAME FUNCTIONS
# ==========================================

def init_game():
    st.session_state.game = json.loads(
        json.dumps(INITIAL_STATE)
    )

    # 이전 이벤트도 초기화
    for key in list(st.session_state.keys()):
        if str(key).startswith("event_"):
            del st.session_state[key]


def add_log(message):
    g = st.session_state.game

    g["log"].insert(
        0,
        f'DAY {g["day"]:02d} — {message}'
    )

    g["log"] = g["log"][:30]


def change(stat, amount):
    g = st.session_state.game

    g[stat] = max(
        0,
        min(100, g[stat] + amount)
    )


def change_relation(name, amount):
    g = st.session_state.game

    g["relations"][name] = max(
        -100,
        min(100, g["relations"][name] + amount)
    )


def finish_ending(title, text):
    st.session_state.game["ending"] = {
        "title": title,
        "text": text,
    }


def check_ending():
    g = st.session_state.game

    if g["hp"] <= 0:
        finish_ending(
            "ENDING 01 — 몸이 먼저 한계를 맞았다",
            "살아남겠다는 의지만으로 모든 것을 해결할 수는 없었다. "
            "유스케는 당분간 모든 일정을 내려놓게 되었다."
        )

    elif (
        g["flags"]["mori_deal"]
        and g["reputation"] >= 75
        and g["day"] >= 5
    ):
        finish_ending(
            "ENDING 02 — 쓸모 있는 말단",
            "승진을 바라지 않았던 유스케에게 모리는 새로운 역할을 제안했다. "
            "그 제안이 선물인지 족쇄인지는 아직 알 수 없다."
        )

    elif (
        g["flags"]["dazai_talks"] >= 3
        and g["day"] >= 6
    ):
        finish_ending(
            "ENDING 03 — 오래된 악우",
            "몇 번의 대화 끝에 두 사람은 예전처럼 서로를 이해하지 못한 채 헤어졌다. "
            "달라진 것은 없지만, 그것으로 충분했다."
        )

    elif g["day"] >= 10:
        finish_ending(
            "ENDING 04 — 내일도 살아간다",
            "특별한 결론은 없었다. 유스케는 여전히 포트 마피아의 말단 조직원이고, "
            "내일도 눈을 뜰 것이다. 적어도 지금은."
        )


def advance():
    g = st.session_state.game

    g["slot"] += 1

    if g["slot"] >= 5:
        g["slot"] = 0
        g["day"] += 1

        change("hp", -5)
        change("mind", -3)

        add_log("하루가 끝났다. 피로가 쌓였다.")

    check_ending()


def do_action(label, effect, log_message):
    effect()

    add_log(log_message)
    advance()

    st.rerun()


# ==========================================
# EVENTS
# ==========================================

EVENTS = [
    {
        "title": "파쇄기 앞의 서류",
        "location": "PORT MAFIA OFFICE",
        "text": (
            "책상 위에 결재 서류가 놓여 있다. "
            "읽기도 전에 파쇄기가 눈에 들어온다.\n\n"
            "누가 봐도 귀찮은 일이다."
        ),
        "choices": [
            (
                "서류를 처리한다",
                lambda: (
                    change("work", 8),
                    change("mind", -5),
                    change("reputation", 2),
                ),
                "드물게 서류를 처리했다.",
            ),
            (
                "적당히 훑어보고 미룬다",
                lambda: (
                    change("work", -2),
                    change("mind", 2),
                ),
                "서류를 내일로 미뤘다.",
            ),
            (
                "파쇄기에 넣는다",
                lambda: (
                    change("work", -8),
                    change("reputation", -4),
                ),
                "서류가 파쇄되었다.",
            ),
        ],
    },
    {
        "title": "오래된 친구",
        "location": "HEADQUARTERS HALLWAY",
        "text": (
            "복도 모퉁이에서 다자이와 마주쳤다. "
            "그는 먼저 말을 걸어온다.\n\n"
            "“어라, 유스케. 아직도 여기 있었구나?”"
        ),
        "choices": [
            (
                "“너야말로 한가한가 봐.”",
                lambda: (
                    change_relation("다자이 오사무", 2),
                    st.session_state.game["flags"].update(
                        dazai_talks=st.session_state.game["flags"]["dazai_talks"] + 1
                    ),
                    change("mind", 2),
                ),
                "다자이와 말씨름을 했다.",
            ),
            (
                "대꾸하지 않고 지나간다",
                lambda: change_relation("다자이 오사무", -1),
                "다자이를 지나쳤다.",
            ),
            (
                "츄야를 놀릴 계획을 제안한다",
                lambda: (
                    change_relation("다자이 오사무", 4),
                    st.session_state.game["flags"].update(
                        dazai_talks=st.session_state.game["flags"]["dazai_talks"] + 1
                    ),
                ),
                "다자이와 잠깐 손을 잡았다.",
            ),
        ],
    },
    {
        "title": "불쾌한 모자",
        "location": "HEADQUARTERS HALLWAY",
        "text": (
            "복도 끝에서 츄야가 걸어온다. "
            "다자이와 함께 있던 흔적을 본 모양인지 표정이 썩 좋지 않다.\n\n"
            "“야, 너. 또 무슨 수작이야?”"
        ),
        "choices": [
            (
                "“별일 없는데? 예민하네.”",
                lambda: (
                    change_relation("나카하라 츄야", -3),
                    change("mind", 2),
                ),
                "츄야의 신경을 긁었다.",
            ),
            (
                "못 들은 척 지나간다",
                lambda: change_relation("나카하라 츄야", -1),
                "츄야를 무시했다.",
            ),
            (
                "다자이에게 떠넘긴다",
                lambda: (
                    change_relation("나카하라 츄야", -2),
                    change_relation("다자이 오사무", 1),
                ),
                "다자이를 끌어들였다.",
            ),
        ],
    },
    {
        "title": "보스의 호출",
        "location": "MORI'S OFFICE",
        "text": (
            "모리의 집무실로 오라는 연락이 왔다. "
            "이유는 적혀 있지 않다.\n\n"
            "모리는 늘 그렇듯 무슨 생각인지 알기 어렵다."
        ),
        "choices": [
            (
                "일단 찾아간다",
                lambda: (
                    change_relation("모리 오가이", -1),
                    change("reputation", 2),
                    st.session_state.game["flags"].update(
                        mori_deal=True
                    ),
                ),
                "모리의 집무실에 다녀왔다.",
            ),
            (
                "몸이 좋지 않다고 거절한다",
                lambda: (
                    change("hp", 4),
                    change_relation("모리 오가이", -2),
                ),
                "모리의 호출을 거절했다.",
            ),
            (
                "아카네에게 먼저 물어본다",
                lambda: (
                    change_relation("아카네", 2),
                    change("mind", 2),
                ),
                "아카네에게 상황을 물었다.",
            ),
        ],
    },
    {
        "title": "예상 밖의 휴식",
        "location": "PORT MAFIA LOUNGE",
        "text": (
            "오늘은 드물게 급한 일이 없다. "
            "창밖으로 요코하마의 거리가 보인다.\n\n"
            "이대로 잠깐 쉬어도 아무도 모를 것 같다."
        ),
        "choices": [
            (
                "조용히 쉰다",
                lambda: (
                    change("hp", 8),
                    change("mind", 7),
                ),
                "잠시 휴식을 취했다.",
            ),
            (
                "쇼헤이를 찾아간다",
                lambda: (
                    change_relation("쇼헤이", 3),
                    change("mind", 3),
                ),
                "쇼헤이와 시간을 보냈다.",
            ),
            (
                "이능력 감각을 점검한다",
                lambda: (
                    change("ability", 2),
                    change("mind", -2),
                ),
                "이능력을 점검했다.",
            ),
        ],
    },
]


def show_event():
    g = st.session_state.game

    key = f'event_{g["day"]}_{g["slot"]}'

    if key not in st.session_state:
        st.session_state[key] = random.choice(EVENTS)

    event = st.session_state[key]

    st.subheader(event["title"])
    st.write(event["text"])
    st.caption(event["location"])

    for index, choice in enumerate(event["choices"]):
        label, effect, message = choice

        if st.button(
            label,
            key=f'{key}_choice_{index}',
            use_container_width=True,
        ):
            do_action(label, effect, message)


# ==========================================
# MORNING
# ==========================================

def show_morning():
    g = st.session_state.game

    if (
        g["day"] == 1
        and g["slot"] == 0
        and not g["flags"]["intro_seen"]
    ):
        st.session_state.game["flags"]["intro_seen"] = True

        st.subheader("오늘도 살아 있네.")

        st.write(
            "눈을 뜨자 휴대전화가 울렸다. "
            "발신자는 모리 씨다. 아침부터 기분이 썩 좋지 않다.\n\n"
            "책상 위에는 어제 처리하지 않은 서류가 쌓여 있다. "
            "오늘도 평범하고 귀찮은 하루가 될 것 같다."
        )

        st.caption("PORT MAFIA HEADQUARTERS")

        if st.button("모리의 전화를 받는다", use_container_width=True):
            change_relation("모리 오가이", -2)
            add_log("모리의 호출을 받았다.")

            st.session_state.game["flags"]["mori_call"] = True
            st.session_state.game["slot"] = 1

            st.rerun()

        if st.button("무시하고 다시 눕는다", use_container_width=True):
            change("hp", 3)
            change("work", -2)

            add_log("모리의 전화를 무시했다.")
            advance()

            st.rerun()

        if st.button("문자부터 확인한다", use_container_width=True):
            change("mind", 2)

            add_log("호출 내용을 문자로 확인했다.")
            advance()

            st.rerun()

        return

    if g["slot"] == 0:
        st.subheader("새로운 아침")

        st.write(
            "어제의 피로가 완전히 가시지는 않았다. "
            "오늘 하루를 어떻게 보낼까?"
        )

        st.caption("YOKOHAMA")

        if st.button("포트 마피아 본부로 출근한다", use_container_width=True):
            do_action(
                "출근",
                lambda: (
                    change("work", 5),
                    change("reputation", 1),
                ),
                "본부에 출근했다.",
            )

        if st.button("병원에서 상태를 확인한다", use_container_width=True):
            do_action(
                "진료",
                lambda: (
                    change("hp", 12),
                    st.session_state.game.update(
                        money=max(
                            0,
                            st.session_state.game["money"] - 500
                        )
                    ),
                ),
                "진료를 받고 컨디션을 조금 회복했다.",
            )

        if st.button("밖으로 나가 산책한다", use_container_width=True):
            do_action(
                "산책",
                lambda: change("mind", 8),
                "요코하마 거리를 걸었다.",
            )

        if st.button("아카네에게 연락한다", use_container_width=True):
            do_action(
                "연락",
                lambda: (
                    change_relation("아카네", 3),
                    change("mind", 4),
                ),
                "아카네와 짧게 연락했다.",
            )

        return

    show_event()


# ==========================================
# INITIALIZE
# ==========================================

if "game" not in st.session_state:
    init_game()

g = st.session_state.game


# ==========================================
# DESIGN
# ==========================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(
                circle at 15% 0%,
                #292332 0,
                transparent 34%
            ),
            #111118;
    }

    h1, h2, h3 {
        color: #e5d9eb !important;
    }

    div[data-testid="stMetric"] {
        background: #22212c;
        padding: 12px;
        border: 1px solid #393543;
        border-radius: 10px;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# TITLE
# ==========================================

st.markdown(
    """
    <p style="
        text-align:center;
        letter-spacing:.28em;
        color:#aaa3b2;
        font-size:11px;
    ">
        BUNGO STRAY DOGS · CHARACTER LIFE RPG
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="
        text-align:center;
        letter-spacing:.12em;
    ">
        BLACK HOUSE
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#aaa3b2;
        letter-spacing:.16em;
        font-size:12px;
    ">
        貴志 祐介 — PORT MAFIA / YOKOHAMA
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()


# ==========================================
# MAIN LAYOUT
# ==========================================

left, right = st.columns(
    [1, 2.15],
    gap="large",
)


# ==========================================
# LEFT — STATUS
# ==========================================

with left:
    st.markdown("## 貴志 祐介")
    st.caption("YUSUKE KISHI · 22 · PORT MAFIA")

    st.markdown("### STATUS")

    st.write(
        f'**DAY {g["day"]:02d}** · '
        f'{TIME_NAMES[min(g["slot"], 4)]}'
    )

    if g["hp"] < 30:
        condition = "매우 좋지 않음"
    elif g["hp"] < 60:
        condition = "불안정"
    else:
        condition = "보통"

    st.write(f"상태: {condition}")
    st.write(f'소지금: ¥ {g["money"]:,}')

    st.markdown("### PARAMETERS")

    for key, label in STAT_NAMES.items():
        st.write(f'**{label}** · {g[key]}/100')
        st.progress(g[key] / 100)

    st.markdown("### RELATIONSHIP")

    for name, value in g["relations"].items():
        st.write(f"{name}　**{value:+d}**")


# ==========================================
# RIGHT — STORY
# ==========================================

with right:
    st.markdown(
        f'**PRESENT · YOKOHAMA**　　'
        f'`{PHASES[min(g["slot"], 4)]}`'
    )

    st.markdown(
        """
        <div style="
            background:linear-gradient(
                120deg,
                #252333,
                #3a3040 48%,
                #161720
            );
            border:1px solid #393543;
            border-radius:12px;
            padding:26px 20px;
            margin:10px 0 18px;
        ">
            <div style="
                color:#d7c9df;
                letter-spacing:.2em;
                font-size:11px;
            ">
                PORT MAFIA · YOKOHAMA
            </div>

            <div style="
                color:#e5d9eb;
                font-size:25px;
                margin-top:8px;
            ">
                오늘도 살아 있네.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if g["ending"]:
        st.error(g["ending"]["title"])
        st.write(g["ending"]["text"])

        if st.button(
            "새로운 기록 시작하기",
            use_container_width=True,
        ):
            init_game()
            st.rerun()

    else:
        show_morning()

    st.divider()

    st.markdown("### QUICK ACTIONS")

    c1, c2, c3 = st.columns(3)

    with c1:
        save_data = json.dumps(
            g,
            ensure_ascii=False,
            indent=2,
        )

        st.download_button(
            "저장 파일 받기",
            save_data,
            file_name="black_house_save.json",
            mime="application/json",
            use_container_width=True,
        )

    with c2:
        uploaded = st.file_uploader(
            "불러오기",
            type=["json"],
            label_visibility="collapsed",
        )

        if uploaded is not None:
            try:
                loaded = json.load(uploaded)

                required = {
                    "day",
                    "slot",
                    "hp",
                    "mind",
                    "ability",
                    "reputation",
                    "work",
                    "survival",
                    "money",
                    "relations",
                    "flags",
                    "log",
                    "ending",
                }

                if not required.issubset(loaded.keys()):
                    raise ValueError("잘못된 저장 파일")

                st.session_state.game = loaded

                st.success("저장 데이터를 불러왔어.")
                st.rerun()

            except (
                json.JSONDecodeError,
                KeyError,
                TypeError,
                ValueError,
            ):
                st.error("저장 파일을 읽지 못했어.")

    with c3:
        if st.button("새 게임", use_container_width=True):
            init_game()
            st.rerun()


# ==========================================
# CHRONICLE
# ==========================================

st.divider()

st.markdown("### CHRONICLE / 기록")

for line in g["log"]:
    st.caption(line)


st.caption(
    "UNOFFICIAL FAN-MADE GAME · "
    "NOT AFFILIATED WITH THE ORIGINAL WORK"
)
