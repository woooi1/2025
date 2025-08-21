import streamlit as st
import random

st.set_page_config(page_title="몸을 가꾸는 멋진 나", layout="wide")

# --- 배경 이미지 ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1554284111-50f03e444ae7?auto=format&fit=crop&w=1740&q=80');
        background-size: cover;
        background-position: center;
    }
    .card {
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 동기부여 문구 ---
motivational_quotes = [
    "오늘도 한 걸음, 더 강해지는 나 💪",
    "포기하지 마세요, 작은 움직임이 큰 변화를 만듭니다!",
    "운동은 몸과 마음 모두를 단단하게 합니다.",
    "땀은 배신하지 않는다, 오늘도 시작해요!",
    "지금 시작하면 1시간 후 더 나은 내가 있어요."
]
quote_today = random.choice(motivational_quotes)

st.markdown(
    f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ff4b4b;">🏋️‍♀️ 홈트 루틴 & 스트레칭</h1>
        <h3 style="color:#2a2a2a; margin-top: 10px;">{quote_today}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 데이터 ---
pre_stretch = {"name": "전신 스트레칭 (운동 전)", "video": "https://www.youtube.com/embed/ahbAnkN4KJ0"}
post_stretch = {"name": "전신 스트레칭 (운동 후)", "video": "https://www.youtube.com/embed/xW3JI2eI7nM"}

exercise_videos = {
    "전신": [{"name": "귀찮은 날, 전신 폭파", "video": "https://www.youtube.com/embed/F-Jd4kI6rdM"}],
    "상체": [{"name": "상체 전체 폭파", "video": "https://www.youtube.com/embed/54tTYO-vU2E"}],
    "하체": [{"name": "하체 전체 폭파", "video": "https://www.youtube.com/embed/NDsjmxTROEo"}]
}

# --- 운동 부위 선택 ---
muscle = st.multiselect("운동 부위 선택", ["전신", "상체", "하체"], default=["전신"])

# --- 운동 전 스트레칭 ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🧘 운동 전 스트레칭")
st.subheader(pre_stretch["name"])
st.video(f"{pre_stretch['video']}?autoplay=1")
st.markdown('</div>', unsafe_allow_html=True)

# --- 운동 루틴 ---
st.markdown("---")
st.header("루틴 - 선택 부위: " + ", ".join(muscle))
for m in muscle:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"{m} 운동")
    exercise = random.choice(exercise_videos[m])
    st.write(f"▶ {exercise['name']}")
    st.video(f"{exercise['video']}?autoplay=1")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 운동 후 스트레칭 ---
st.markdown("---")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🧘 운동 후 스트레칭")
st.subheader(post_stretch["name"])
st.video(f"{post_stretch['video']}?autoplay=1")
st.markdown('</div>', unsafe_allow_html=True)

# --- 출처 ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>
        출처: 전신/상체/하체 운동 - 땅끄부부 | 운동 전 스트레칭 - SOMPIT | 운동 후 스트레칭 - 다노
    </div>
    """,
    unsafe_allow_html=True
)
