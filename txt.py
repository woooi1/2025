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

# --- 웹 표지 ---
st.markdown(
    """
    <div style='text-align: center; padding: 40px; background-color: #f0f8ff; border-radius: 15px;'>
        <h1 style='color: #ff4b4b;'>🏋️‍♀️ 홈트 루틴 & 스트레칭</h1>
        <h3 style='color: #2a2a2a;'>{}</h3>
    </div>
    """.format(quote_today),
    unsafe_allow_html=True
)

st.markdown("---")

# --- 기존 운동 앱 코드 (전신/상체/하체, 운동 전/후 스트레칭) ---
pre_stretch = {"name": "전신 스트레칭 (운동 전)", "video": "https://youtu.be/ahbAnkN4KJ0?si=8bpv4KW5JuSP4oZ1"}
post_stretch = {"name": "전신 스트레칭 (운동 후)", "video": "https://youtu.be/xW3JI2eI7nM?si=6zeKT1a6egU-ox_H"}

exercise_videos = {
    "전신": [
        {"name": "귀찮은 날, 전신 폭파", "video": "https://youtu.be/F-Jd4kI6rdM?si=2kNyTBbgKWKQIWs4"},
    ],
    "상체": [
        {"name": "상체 전체 폭파", "video": "https://youtu.be/54tTYO-vU2E?si=MomGozGJ9UT2K7hP"},
    ],
    "하체": [
        {"name": "하체 전체 폭파", "video": "https://youtu.be/NDsjmxTROEo?si=Hybxtgpxu1QfIBhR"},
    ]
}

# 운동 부위 선택
muscle = st.multiselect("운동 부위 선택", ["전신", "상체", "하체"], default=["전신"])

# 운동 전 스트레칭
st.markdown("---")
st.header("🧘 운동 전 스트레칭")
st.subheader(pre_stretch["name"])
st.video(f"{pre_stretch['video']}?autoplay=1")

# 운동 루틴
st.markdown("---")
st.header("루틴 - 선택 부위: " + ", ".join(muscle))
import random
for m in muscle:
    st.subheader(f"{m} 운동")
    exercise = random.choice(exercise_videos[m])
    st.write(f"▶ {exercise['name']}")
    st.video(f"{exercise['video']}?autoplay=1")

# 운동 후 스트레칭
st.markdown("---")
st.header("🧘 운동 후 스트레칭")
st.subheader(post_stretch["name"])
st.video(f"{post_stretch['video']}?autoplay=1")
