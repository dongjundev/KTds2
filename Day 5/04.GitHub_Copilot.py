import streamlit as st
import random

st.title("숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.result = ""

guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1, key="guess_input")

if st.button("제출"):
    st.session_state.tries += 1
    if guess < st.session_state.number:
        st.session_state.result = "더 큰 숫자입니다."
    elif guess > st.session_state.number:
        st.session_state.result = "더 작은 숫자입니다."
    else:
        st.session_state.result = f"정답입니다! 시도 횟수: {st.session_state.tries}번"
        # 게임을 다시 시작할 수 있도록 숫자 초기화
        st.session_state.number = random.randint(1, 100)
        st.session_state.tries = 0

if "result" in st.session_state:
    st.write(st.session_state.result)