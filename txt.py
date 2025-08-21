import streamlit as st

# 운동 루틴 데이터
routines = {
    "초급": [
        "스쿼트 10회 × 3세트",
        "푸시업(무릎) 8회 × 3세트",
        "플랭크 20초 × 3세트",
        "런지 10회 × 2세트"
    ],
    "중급": [
        "스쿼트 15회 × 4세트",
        "푸시업 12회 × 4세트",
        "플랭크 40초 × 3세트",
        "버피 10회 × 3세트",
        "런지 12회 × 3세트"
    ],
    "고급": [
        "점프 스쿼트 20회 × 4세트",
        "푸시업(딥) 15회 × 4세트",
        "플랭크 60초 × 4세트",
        "버피 15회 × 4세트",
        "풀업 8회 × 3세트"
    ]
}

# 제목
st.title("🏋️ 전신 운동 루틴 웹앱")
st.subheader("난이도를 선택하면 루틴이 나와요")

# 난이도 선택
level = st.radio("난이도를 선택하세요", list(routines.keys()))

# 선택된 루틴 표시
st.markdown("---")
st.header(f"{level} 루틴")
for idx, ex in enumerate(routines[level], 1):
    st.write(f"{idx}. {ex}")
