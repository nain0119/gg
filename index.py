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
st.markdown('<div class="eyebrow">PORT MAFIA  /  PERSONAL RECORD</div>', unsafe_allow_html=True)
st.title("기시 유스케 생존 기록")
st.markdown('<div class="subnote">요코하마 · 7일간의 생존 보고서</div>', unsafe_allow_html=True)

if st.session_state.phase == "title":
    intro_text = (
        "**「타살은 기회, ■■은 권리 포기! 역겹고 의미 없는 삶이라도 살아가도록 해.」**\n\n"
        "당신은 문호 스트레이 독스의 자캐 **기시 유스케**의 몸에 빙의했습니다.\n"
        "앞으로 7일. 체력을 관리하고, 정체를 들키지 않은 채 살아남으세요."
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
