import streamlit as st

st.set_page_config(page_title="운동 & 스트레칭 웹앱", layout="wide")

# --- 데이터 ---
pre_stretches = [
    {"name": "목 스트레칭", "video": "https://www.youtube.com/embed/kT5ZUhU7qYI"},  
    {"name": "어깨 스트레칭", "video": "https://www.youtube.com/embed/F52zF7ZRzBs"},  
]

workouts = {
    "초급": {
        "승모근": [{"name": "덤벨 숄더 슈러그", "video": "https://www.youtube.com/embed/cn3vNn9vvhA"}],
        "어깨": [{"name": "덤벨 숄더 프레스", "video": "https://www.youtube.com/embed/T8x07Ej7NWI"}],
        "팔": [{"name": "덤벨 컬", "video": "https://www.youtube.com/embed/yE4Jkxy5x2o"}],
        "등": [{"name": "벤트오버 로우", "video": "https://www.youtube.com/embed/Y1H3jYpZP0k"}],
        "배": [{"name": "플랭크", "video": "https://www.youtube.com/embed/M5MdjRR3qjI"}],
        "허리": [{"name": "백 익스텐션", "video": "https://www.youtube.com/embed/d4L6QF5LzEc"}],
        "허벅지": [{"name": "스쿼트", "video": "https://www.youtube.com/embed/nxIY0R5D8U4"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/3DhLMfBHFuM"}]
    },
    "중급": {
        "승모근": [{"name": "덤벨 숄더 슈러그", "video": "https://www.youtube.com/embed/cn3vNn9vvhA"}],
        "어깨": [{"name": "푸시 프레스", "video": "https://www.youtube.com/embed/tYx7b95X2DM"}],
        "팔": [{"name": "바벨 컬", "video": "https://www.youtube.com/embed/0KZDFR6rY4M"}],
        "등": [{"name": "풀업", "video": "https://www.youtube.com/embed/RHzpIduNukE"}],
        "배": [{"name": "사이드 플랭크", "video": "https://www.youtube.com/embed/YPXvabDF_UM"}],
        "허리": [{"name": "데드리프트", "video": "https://www.youtube.com/embed/JqApcH9l3j0"}],
        "허벅지": [{"name": "점프 스쿼트", "video": "https://www.youtube.com/embed/zyzxP_BvjHU"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/3DhLMfBHFuM"}]
    },
    "고급": {
        "승모근": [{"name": "바벨 슈러그", "video": "https://www.youtube.com/embed/cn3vNn9vvhA"}],
        "어깨": [{"name": "아놀드 프레스", "video": "https://www.youtube.com/embed/o-KYwMvmFoI"}],
        "팔": [{"name": "클로즈 그립 푸시업", "video": "https://www.youtube.com/embed/2tKQG9V2BLc"}],
        "등": [{"name": "풀업", "video": "https://www.youtube.com/embed/RHzpIduNukE"}],
        "배": [{"name": "드래곤 플래그", "video": "https://www.youtube.com/embed/LfcJ0R40UJk"}],
        "허리": [{"name": "백 익스텐션", "video": "https://www.youtube.com/embed/d4L6QF5LzEc"}],
        "허벅지": [{"name": "바벨 스쿼트", "video": "https://www.youtube.com/embed/W6j9E5_3fI0"}],
        "종아리": [{"name": "카프 레이즈", "video": "https://www.youtube.com/embed/3DhLMfBHFuM"}]
    }
}

post_stretches = [
    {"name": "허리 스트레칭", "video": "https://www.youtube.com/embed/ENFJtWLw0aU"},  
    {"name": "햄스트링 스트레칭", "video": "https://www.youtube.com/embed/Nc7V5soMgCk"}  
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
