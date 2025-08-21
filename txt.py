import streamlit as st
import random

st.set_page_config(page_title="홈트 루틴 & 스트레칭", layout="wide")

# --- 동기부여 문구 ---
motivational_quotes = [
    "오늘도 한 걸음, 더 강해지는 나 💪",
    "포기하지 마세요, 작은 움직임이 큰 변화를 만듭니다!",
    "운동은 몸과 마음 모두를 단단하게 합니다.",
    "땀은 배신하지 않는다, 오늘도 시작해요!",
    "지금 시작하면 1시간 후 더 나은 내가 있어요."
]

quote_today = random.choice(motivational_quotes)

# --- 세션 상태 초기화 ---
if "show_workout" not in st.session_state:
    st.session_state.show_workout = False

# --- 표지 화면 ---
if not st.session_state.show_workout:
    st.markdown(
        f"""
        <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 80vh;'>
            <h1 style='color: #ff4b4b; font-size: 60px;'>🏋️‍♀️ 홈트 루틴 & 스트레칭</h1>
            <h3 style='color: #2a2a2a; font-size: 28px; text-align: center; margin-top: 20px;'>{quote_today}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 운동 시작 버튼 (중앙 하단, 크게)
    if st.button("운동 시작 💪"):
        st.session_state.show_workout = True

    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            width: 300px;
            height: 80px;
            font-size: 30px;
            background-color: #ff4b4b;
            color: white;
            border-radius: 20px;
            position: fixed;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 운동 루틴 화면 ---
if st.session_state.show_workout:
    st.title("🏋️‍♀️ 오늘의 루틴")

    # --- 데이터 ---
    pre_stretch = {"name": "전신 스트레칭 (운동 전)", "video": "https://www.youtube.com/embed/ahbAnkN4KJ0"}
    post_stretch = {"name": "전신 스트레칭 (운동 후)", "video": "https://www.youtube.com/embed/xW3JI2eI7nM"}

    exercise_videos = {
        "전신": [
            {"name": "귀찮은 날, 전신 폭파", "video": "https://www.youtube.com/embed/F-Jd4kI6rdM"},
        ],
        "상체": [
            {"name": "상체 전체 폭파", "video": "https://www.youtube.com/embed/54tTYO-vU2E"},
        ],
        "하체": [
            {"name": "하체 전체 폭파", "video": "https://www.youtube.com/embed/NDsjmxTROEo"},
        ]
    }

    # 운동 부위 선택
    muscle = st.multiselect("운동 부위 선택", ["전신", "상체", "하체"], default=["전신"])

    # --- 운동 전 스트레칭 ---
    st.markdown("---")
    st.header("🧘 운동 전 스트레칭")
    st.subheader(pre_stretch["name"])
    st.video(f"{pre_stretch['video']}?autoplay=1")

    # --- 운동 루틴 ---
    st.markdown("---")
    st.header("루틴 - 선택 부위: " + ", ".join(muscle))
    for m in muscle:
        st.subheader(f"{m} 운동")
        exercise = random.choice(exercise_videos[m])
        st.write(f"▶ {exercise['name']}")
        st.video(f"{exercise['video']}?autoplay=1")

    # --- 운동 후 스트레칭 ---
    st.markdown("---")
    st.header("🧘 운동 후 스트레칭")
    st.subheader(post_stretch["name"])
    st.video(f"{post_stretch['video']}?autoplay=1")
