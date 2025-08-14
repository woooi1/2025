import streamlit as st

# ----------------------------
# MBTI별 직업 추천 데이터 (고양이 버전)
# ----------------------------
mbti_jobs = {
    "INTJ": ["🐱📊 데이터 사이언티스트", "🐾 전략 컨설턴트", "🐈🔬 연구원"],
    "INTP": ["🐱💻 프로그래머", "🐾 인공지능 연구원", "🐈🔍 분석가"],
    "ENTJ": ["🐱💼 CEO", "🐾 프로젝트 매니저", "🐈 전략 기획가"],
    "ENTP": ["🐱💡 기업가", "🐾 마케팅 디렉터", "🐈 방송인"],
    "INFJ": ["🐱💬 심리상담사", "🐾 작가", "🐈 교육 전문가"],
    "INFP": ["🐱🎨 예술가", "🐾 시인", "🐈 사회운동가"],
    "ENFJ": ["🐱🎓 교육가", "🐾 상담사", "🐈 리더십 코치"],
    "ENFP": ["🐱🎬 영화감독", "🐾 여행 작가", "🐈 크리에이티브 디렉터"],
    "ISTJ": ["🐱📚 행정 공무원", "🐾 회계사", "🐈 법률 전문가"],
    "ISFJ": ["🐱🏥 간호사", "🐾 사회복지사", "🐈 보육교사"],
    "ESTJ": ["🐱📈 경영 관리자", "🐾 운영 책임자", "🐈 군 간부"],
    "ESFJ": ["🐱💝 고객 서비스 전문가", "🐾 간호사", "🐈 이벤트 기획자"],
    "ISTP": ["🐱🔧 엔지니어", "🐾 레이싱 드라이버", "🐈 장인"],
    "ISFP": ["🐱🎶 음악가", "🐾 디자이너", "🐈 플로리스트"],
    "ESTP": ["🐱🏆 운동선수", "🐾 영업 전문가", "🐈 응급 구조원"],
    "ESFP": ["🐱🎭 배우", "🐾 이벤트 플래너", "🐈 판매 전문가"],
}

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(page_title="🐱💖 MBTI 고양이 진로 추천", page_icon="🐱", layout="centered")

# ----------------------------
# 반짝이 배경 CSS
# ----------------------------
st.markdown("""
    <style>
    body {
        background-image: url("https://i.gifer.com/yy3.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 상단 타이틀
# ----------------------------
st.markdown("""
    <h1 style='text-align: center; font-size: 55px; color: #ff66cc;'>
        🌸🐱 MBTI 기반 고양이 진로 추천 🌸
    </h1>
    <p style='text-align: center; font-size: 20px; color: #444;'>
        당신의 MBTI를 선택하면 😺 딱 맞는 직업을 귀여운 고양이와 함께 추천해드려요!  
        <br>💖 이 세상에서 제일 귀여운 고양이 진로 추천 페이지 💖
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# MBTI 선택
# ----------------------------
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("✨ 당신의 MBTI를 골라주세요! ✨", mbti_list, index=0)

# ----------------------------
# 결과 출력
# ----------------------------
if selected_mbti:
    st.markdown(f"""
        <h2 style='color: #ff3399; font-size: 40px; text-align: center;'>
            🐾 {selected_mbti} 🐾 유형 추천 직업
        </h2>
    """, unsafe_allow_html=True)

    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"""
            <div style='
                background-color: rgba(255, 240, 250, 0.9);
                padding: 15px;
                margin: 10px;
                border-radius: 15px;
                text-align: center;
                font-size: 24px;
                color: #cc0066;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {job}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; font-size: 18px; color: #555;'>
            💡 MBTI는 참고용이에요! <br>
            세상에서 제일 귀여운 고양이처럼 🐱 자유롭게 진로를 탐험하세요 🌟
        </p>
    """, unsafe_allow_html=True)

# ----------------------------
# 하단 푸터
# ----------------------------
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 16px; color: #555;'>
        🐱 만든 사람: <b>최최 이</b> 🌸  
        🌟 세상에서 제일 귀여운 고양이 진로 추천 페이지 🌟
    </p>
""", unsafe_allow_html=True)
