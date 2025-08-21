import streamlit as st
import random   



# 페이지 설정
st.set_page_config(page_title="운동 & 스트레칭 웹앱", layout="wide")

# 운동 영상 데이터 (한국인 유튜버 영상으로 예시)
exercise_videos = {
    "어깨": [
        {"name": "덤벨 숄더 프레스", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"},
        {"name": "사이드 레터럴 레이즈", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
    ],
    "배": [
        {"name": "플랭크", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"},
        {"name": "사이드 플랭크", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
    ],
    "팔": [
        {"name": "바벨 컬", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"},
        {"name": "덤벨 컬", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
    ],
    "허벅지": [
        {"name": "스쿼트", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"},
        {"name": "런지", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
    ],
    "종아리": [
        {"name": "카프 레이즈", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"},
        {"name": "시티드 카프 레이즈", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
    ],
    "스트레칭": {
        "전신": [
            {"name": "전신 스트레칭", "video": "https://www.youtube.com/watch?v=1vlyd6pG4b4"}
        ]
    }
}

# 난이도별 세트 설정
levels = {
    "초급": {"sets": 2, "time": "20초~30초"},
    "중급": {"sets": 3, "time": "30초~40초"},
    "고급": {"sets": 4, "time": "40초~60초"}
}

# 제목
st.title("홈트 루틴 생성기")

# 선택 옵션
level = st.selectbox("운동 난이도 선택", ["초급", "중급", "고급"])
muscle = st.multiselect("운동 부위 선택", ["어깨", "배", "팔", "허벅지", "종아리"])

# 루틴 생성 버튼
if st.button("루틴 생성하기"):
    st.header(f"{level} 루틴 - 선택 부위: {', '.join(muscle)}")

    # 선택한 부위별 운동 랜덤 추천
    for m in muscle:
        exercise = random.choice(exercise_videos[m])
        st.subheader(f"{m} 운동: {exercise['name']}")
        st.video(exercise["video"])
        st.write(f"세트 수: {levels[level]['sets']}세트, 시간: {levels[level]['time']}")

    # 운동 후 스트레칭 영상
    post_stretch = exercise_videos["스트레칭"]["전신"][0]
    st.subheader("운동 후 스트레칭")
    st.video(post_stretch["video"])

