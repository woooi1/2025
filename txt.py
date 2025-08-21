import streamlit as st

st.set_page_config(page_title="운동 & 스트레칭 웹앱", layout="wide")

# --- 데이터 ---
pre_stretches = [
    {"name": "12분 전신 스트레칭", "video": "https://www.youtube.com/embed/itJE4neqDJw?autoplay=1&mute=1"},
    {"name": "15분 전신 스트레칭 (DAY7)", "video": "https://www.youtube.com/embed/g_tea8ZNk5A?autoplay=1&mute=1"}
]

workouts = {
    "초급": {
        "승모근": [{"name": "덤벨 숄더 슈러그", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "어깨": [{"name": "덤벨 숄더 프레스", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "팔": [{"name": "덤벨 컬", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "등": [{"name": "벤트오버 로우", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "배": [{"name": "플랭크", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "허리": [{"name": "백 익스텐션", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "허벅지": [{"name": "스쿼트", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/75pA0MaLvy0?autoplay=1&mute=1"}]
    }
}

post_stretches = [
    {"name": "허리 스트레칭 루틴", "video": "https://www.youtube.com/embed/FI51zRzgIe4?autoplay=1&mute=1"},
    {"name": "20분 전신 스트레칭", "video": "https://www.youtube.com/embed/DYGfwPppgO4?autoplay=1&mute=1"}
]

# --- UI ---
st.title("🏋️ 전신/부위별 운동 & 스트레칭 웹앱")

# 난이도 선택
level = st.radio("난이도를 선택하세요", list(workouts.keys()))

# 부위 선택 (전체 가능)
muscle_options = list(workouts[level].keys())
muscle = st.multiselect("부위를 선택하세요 (전체 선택 가능)", muscle_options, default=muscle_options)

# --- 운동 전 스트레칭 ---
st.markdown("---")
st.header("🧘 운동 전 스트레칭 (자동재생)")
for s in pre_stretches:
    st.subheader(s["name"])
    st.markdown(f'<iframe width="100%" height="315" src="{s["video"]}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)

# --- 운동 루틴 ---
st.markdown("---")
st.header(f"{level} 루틴 - 선택 부위: {', '.join(muscle)}")
for m in muscle:
    st.subheader(m)
    for ex in workouts[level][m]:
        st.write(f"▶ {ex['name']}")
        st.markdown(f'<iframe width="100%" height="315" src="{ex["video"]}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)

# --- 운동 후 스트레칭 ---
st.markdown("---")
st.header("🧘 운동 후 스트레칭 (자동재생)")
for s in post_stretches:
    st.subheader(s["name"])
    st.markdown(f'<iframe width="100%" height="315" src="{s["video"]}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)
