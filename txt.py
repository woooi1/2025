import streamlit as st
import random

st.set_page_config(page_title="홈트 루틴 & 스트레칭", layout="wide")

# --- 데이터 ---
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

# --- UI ---
st.title("🏋️‍♀️ 홈트 루틴 & 스트레칭 웹앱")

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
