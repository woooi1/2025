
import streamlit as st

# MBTI별 직업 추천 데이터 예시
mbti_jobs = {
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "연구원"],
    "INFJ": ["심리상담사", "작가", "교육 전문가"],
    "ENTP": ["기업가", "마케팅 디렉터", "방송인"],
    "ESFP": ["배우", "이벤트 플래너", "판매 전문가"],
    # ... 다른 MBTI도 추가 가능
}

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯")

st.title("MBTI 기반 진로 추천 🎯")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요:", mbti_list)

# 추천 결과
if selected_mbti:
    st.subheader(f"🧩 {selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

# 추가 기능: 결과 설명
st.info("💡 MBTI는 참고용이며, 다양한 경험과 자기 탐색이 진로 선택에 중요합니다.")
