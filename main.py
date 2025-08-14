import streamlit as st

# ----------------------------
# MBTI별 직업 추천 데이터
# ----------------------------
mbti_jobs = {
    "INTJ": ["🧠 데이터 사이언티스트", "📊 전략 컨설턴트", "🔬 연구원"],
    "INFJ": ["💬 심리상담사", "📖 작가", "🎓 교육 전문가"],
    "ENTP": ["💡 기업가", "📣 마케팅 디렉터", "🎤 방송인"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "🛍 판매 전문가"],
    "ISTP": ["🔧 엔지니어", "🏎 레이싱 드라이버", "🛠 장인"],
    "ENFP": ["🎨 크리에이티브 디렉터", "🌍 여행 작가", "🎬 영화감독"],
}

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(page_title="💖 MBTI 진로 추천", page_icon="🌟", layout="centered")

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
        background-color: rgba(255, 255, 255, 0.8);
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
    <h1 style='text-align: center; font-size: 60px; color: #ff66b3;'>
        🌈💖 MBTI 기반 ✨진로 추천 파티✨ 💖🌈
    </h1>
    <p style='text-align: center; font-size: 20px; color: #444;'>
        당신의 MBTI를 선택하면 🎯 반짝이는 미래 직업을 추천해드려요!  
        <br>💎 눈뽕 주의! 이 세상에서 제일 화려한 진로 추천 페이지 💎
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
            🌟 {selected_mbti} 🌟 유형 추천 직업
        </h2>
    """, unsafe_allow_html=True)

    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"""
            <div style='
                background-color: rgba(255, 240, 245, 0.9);
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
            경험을 통해 나만의 길을 찾아가세요 🌟
        </p>
    """, unsafe_allow_html=True)

# ----------------------------
# 하단 푸터
# ----------------------------
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 16px; color: #555;'>
        🪞 만든 사람: <b>최최 이</b> ✨  
        🌸 세상에서 제일 반짝이는 진로 추천 페이지 🌸
    </p>
""", unsafe_allow_html=True)
