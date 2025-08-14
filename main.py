import streamlit as st

# ----------------------------
# MBTI 직업 추천 기본 데이터
# ----------------------------
mbti_jobs = {
    # 간단한 예시만 살짝...
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "연구원"],
    "INFJ": ["심리상담사", "작가", "교육 전문가"],
    "ENTP": ["기업가", "마케팅 디렉터", "방송인"],
    "ESFP": ["배우", "이벤트 플래너", "판매 전문가"],
    # 나머지는 자유롭게 확장 가능!
}

st.set_page_config(page_title="🌟 피크민 진로 추천", page_icon="🍃", layout="centered")

# ----------------------------
# 반짝 피크민 배경 (GIF) + CSS 설정
# ----------------------------
st.markdown("""
    <style>
    body {
        background-image: url("https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
    }
    .pikmin-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 상단 아트피크민 이미지 중심 배치
# ----------------------------
st.markdown(
    '<img src="https://drawsocute.com/wp-content/uploads/2023/08/Pikmin-drawing.png" class="pikmin-img"/>',
    unsafe_allow_html=True
)

st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #009933;'>
        🍃💖 피크민 터치 진로 추천 💖🍃
    </h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>
        피크민처럼 귀엽고 반짝이는 직업 추천 🎈<br>
        MBTI를 골라서 당신에게 딱 맞는 길을 찾아봐요~  
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# MBTI 선택
# ----------------------------
selected_mbti = st.selectbox("✨ MBTI 유형을 골라주세요!", list(mbti_jobs.keys()))

# ----------------------------
# 결과 출력
# ----------------------------
if selected_mbti:
    st.markdown(f"""
        <h2 style='text-align: center; font-size: 32px; color: #006600;'>
            당신의 유형: {selected_mbti}
        </h2>
    """, unsafe_allow_html=True)

    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"""
            <div style='
                background-color: #e6ffe6;
                padding: 12px;
                margin: 8px 0;
                border-radius: 12px;
                text-align: center;
                font-size: 22px;
                color: #004d00;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            '>
                🍀 {job}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; font-size: 16px; color: #333;'>
            피크민처럼 무리의 힘을 믿고, 다양한 경험으로  
            당신만의 길을 찾아가세요! 🌟
        </p>
    """, unsafe_allow_html=True)

# ----------------------------
# 푸터
# ----------------------------
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 14px; color: #666;'>
        © 피크민 진로 추천 프로젝트<br>
        Designed with love and cuteness by you! 🍃❤️
    </p>
""", unsafe_allow_html=True)
