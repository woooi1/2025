import streamlit as st

st.set_page_config(page_title="운동 & 스트레칭 웹앱", layout="wide")

# --- 데이터 ---
pre_stretches = [
    {"name": "목 스트레칭", "video": "https://www.youtube.com/embed/2L2lnxIcNmo"},
    {"name": "어깨 스트레칭", "video": "https://www.youtube.com/embed/1dy0NfBf5co"},
]

workouts = {
    "초급": {
        "승모근": [{"name": "덤벨 숄더 슈러그", "video": "https://www.youtube.com/embed/2z8JmcrW-As"}],
        "어깨": [{"name": "덤벨 숄더 프레스", "video": "https://www.youtube.com/embed/qEwKCR5JCog"}],
        "팔": [{"name": "덤벨 컬", "video": "https://www.youtube.com/embed/ykJmrZ5v0Oo"}],
        "등": [{"name": "벤트오버 로우", "video": "https://www.youtube.com/embed/vT2GjY_Umpw"}],
        "배": [{"name": "플랭크", "video": "https://www.youtube.com/embed/pSHjTRCQxIw"}],
        "허리": [{"name": "백 익스텐션", "video": "https://www.youtube.com/embed/Phq1_pnU8wY"}],
        "허벅지": [{"name": "스쿼트", "video": "https://www.youtube.com/embed/YaXPRqUwItQ"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/YU4_Ds6g8pA"}]
    },
    "중급": {
        "승모근": [{"name": "덤벨 숄더 슈러그", "video": "https://www.youtube.com/embed/2z8JmcrW-As"}],
        "어깨": [{"name": "푸시 프레스", "video": "https://www.youtube.com/embed/qEwKCR5JCog"}],
        "팔": [{"name": "바벨 컬", "video": "https://www.youtube.com/embed/ykJmrZ5v0Oo"}],
        "등": [{"name": "풀업", "video": "https://www.youtube.com/embed/eGo4IYlbE5g"}],
        "배": [{"name": "사이드 플랭크", "video": "https://www.youtube.com/embed/K2VljzCC16g"}],
        "허리": [{"name": "데드리프트", "video": "https://www.youtube.com/embed/ytGaGIn3SjE"}],
        "허벅지": [{"name": "점프 스쿼트", "video": "https://www.youtube.com/embed/aclHkVaku9U"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/YU4_Ds6g8pA"}]
    },
    "고급": {
        "승모근": [{"name": "바벨 슈러그", "video": "https://www.youtube.com/embed/2z8JmcrW-As"}],
        "어깨": [{"name": "아놀드 프레스", "video": "https://www.youtube.com/embed/qEwKCR5JCog"}],
        "팔": [{"name": "클로즈 그립 푸시업", "video": "https://www.youtube.com/embed/IODxDxX7oi4"}],
        "등": [{"name": "풀업", "video": "https://www.youtube.com/embed/eGo4IYlbE5g"}],
        "배": [{"name": "드래곤 플래그", "video": "https://www.youtube.com/embed/6v5RzZ3Rpu0"}],
        "허리": [{"name": "백 익스텐션", "video": "https://www.youtube.com/embed/Phq1_pnU8wY"}],
        "허벅지": [{"name": "바벨 스쿼트", "video": "https://www.youtube.com/embed/2-LAMcpzODU"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/YU4_Ds6g8pA"}]
    }
}

post_stretches = [
    {"name": "허리 스트레칭", "video": "https://www.youtube.com/embed/_gL8EYsg3_0"},
    {"name": "햄스트링 스트레칭", "video": "https://www.youtube.com/embed/yYasr1enKHc"}
]

# --- UI ---
st.title("🏋️ 전신/부위별 운동 & 스트레칭 웹앱")

# 난이도 선택
level = st.radio("난이도를 선택하세요", list(workouts.keys()))

# 부위 선택
muscle_options = list(workouts[level].keys())
muscle = st.multiselect("부위를 선택하세요 (전체 선택 가능)", muscle_options, default=muscle_options)

# --- 운동 전 스트레칭 ---
st.markdown("---")
st.header("🧘 운동 전 스트레칭")
for s in pre_stretches:
    st.subheader(s["name"])
    st.video(s["video"])

# --- 운동 루틴 ---
st.markdown("---")
st.header(f"{level} 루틴 - 선택 부위: {', '.join(muscle)}")
for m in muscle:
    st.subheader(m)
    for ex in workouts[level][m]:
        st.write(f"▶ {ex['name']}")
        st.video(ex["video"])

# --- 운동 후 스트레칭 ---
st.markdown("---")
st.header("🧘 운동 후 스트레칭")
for s in post_stretches:
    st.subheader(s["name"])
    st.video(s["video"])
