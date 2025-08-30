import streamlit as st

st.set_page_config(page_title="운동하자!", layout="wide")

# --- 명언 출력 ---
quotes = [
    "오늘 땀 한 방울이 내일의 변화를 만든다.",
    "포기하지 마라, 시작이 반이다.",
    "운동은 최고의 투자다.",
    "작은 습관이 큰 변화를 만든다."
]
import random
st.markdown(
    f"<h2 style='text-align: center; color: #ff4b4b;'>{random.choice(quotes)}</h2>",
    unsafe_allow_html=True
)

st.write("---")

# --- 운동 부위 선택 ---
part = st.radio("운동할 부위를 선택하세요:", ["전신", "상체", "하체"])

# --- 운동 시작 버튼 ---
if st.button("운동 시작!"):
    st.subheader("🔥 운동 전 스트레칭")
    st.video("https://www.youtube.com/embed/WoNCIBVLbgw")  # 예시 스트레칭 영상

    st.subheader(f"💪 {part} 운동 영상")
    if part == "전신":
        st.video("https://www.youtube.com/embed/UItWltVZZmE")  # 전신 운동 예시
        st.video("https://www.youtube.com/embed/ml6cT4AZdqI")
    elif part == "상체":
        st.video("https://www.youtube.com/embed/ykJmrZ5v0Oo")  # 팔
        st.video("https://www.youtube.com/embed/eGo4IYlbE5g")  # 어깨
    elif part == "하체":
        st.video("https://www.youtube.com/embed/2vSJM8QoBvw")  # 하체
        st.video("https://www.youtube.com/embed/IoY2kdU9jE4")  # 스쿼트

    st.subheader("🧘 운동 후 스트레칭")
    st.video("https://www.youtube.com/embed/qHJhR7wS4Vw")  # 예시 스트레칭 영상
