import base64
import streamlit as st

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="🤍 하얀피크민의 왕 · 지배자",
    page_icon="🤍",
    layout="centered"
)

# ----------------------------
# 사이드바: 배경 이미지 설정
# ----------------------------
with st.sidebar:
    st.header("🤍 배경 설정 (하얀피크민)")
    bg_url = st.text_input("하얀 피크민 GIF/이미지 URL", value="")
    bg_file = st.file_uploader("직접 업로드 (GIF/JPG/PNG)", type=["gif", "jpg", "jpeg", "png"])
    st.caption("URL 또는 업로드 중 하나만 사용하세요. 없으면 기본 반짝이 배경이 적용됩니다 ✨")

# 업로드된 파일을 base64로 변환
bg_style = ""
if bg_file is not None:
    bdata = bg_file.read()
    b64 = base64.b64encode(bdata).decode()
    mime = "image/gif" if bg_file.type == "image/gif" else ("image/png" if "png" in bg_file.type else "image/jpeg")
    bg_style = f"background-image: url('data:{mime};base64,{b64}');"
elif bg_url.strip():
    bg_style = f"background-image: url('{bg_url.strip()}');"
else:
    # 기본 반짝이 그라디언트 (이미지 없이 CSS 애니메이션만)
    bg_style = """
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,0.9), rgba(255,255,255,0.4) 40%, transparent 60%),
        radial-gradient(circle at 80% 30%, rgba(255,255,255,0.85), rgba(255,255,255,0.35) 45%, transparent 65%),
        linear-gradient(135deg, #ffffff 0%, #f7f7ff 40%, #eef2ff 100%);
    """

# ----------------------------
# 전역 스타일: 하얀피크민 왕국 ✨
# ----------------------------
st.markdown(f"""
<style>
/* 배경 */
.stApp {{
    {bg_style}
    background-size: cover;
    background-attachment: fixed;
    backdrop-filter: blur(0.0px);
}}

/* 반투명 카드 느낌 */
.block-container {{
    background: rgba(255,255,255,0.82);
    border-radius: 24px;
    padding: 28px 24px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.08);
}}

/* 반짝이 파티클 */
@keyframes float {{
  0% {{ transform: translateY(0) translateX(0) scale(1); opacity: .9; }}
  50% {{ transform: translateY(-20px) translateX(10px) scale(1.05); opacity: 1; }}
  100% {{ transform: translateY(0) translateX(0) scale(1); opacity: .9; }}
}}
.sparkle {{
  position: fixed; z-index: 0; pointer-events: none; opacity: .8;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,.12));
  animation: float 4s ease-in-out infinite;
  font-size: 22px;
}}

/* 추천 카드 */
.pill {{
  background: rgba(255,255,255,0.92);
  border: 2px solid #f1f5ff;
  border-radius: 18px;
  padding: 14px 16px;
  margin: 8px 0;
  font-size: 20px;
  color: #2b2b2b;
  box-shadow: 0 6px 20px rgba(0,0,0,0.06);
}}
.pill:hover {{ transform: translateY(-2px); transition: .15s ease; }}

/* 제목 폰트 효과 */
h1.title {{
  text-align: center;
  font-size: 56px;
  color: #111;
  background: linear-gradient(90deg, #111, #666);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 1px;
}}
h2.subtitle {{
  text-align: center; color: #444; font-size: 22px; margin-top: -8px;
}}

/* 왕관 배지 */
.badge {{
  display: inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,.9);
  border: 1.5px solid #eaeaea;
  font-size: 14px; color: #555;
  box-shadow: 0 4px 12px rgba(0,0,0,.06);
}}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# 상단 헤더
# ----------------------------
st.markdown("<div style='text-align:center' class='badge'>🤍 하얀피크민 왕국 · White Pikmin Dominion</div>", unsafe_allow_html=True)
st.markdown("<h1 class='title'>👑 하얀피크민의 왕 · 하얀피크민의 지배자 👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>독(毒)에 강하고 빠른 그대여, 하얀 꽃을 머리에 이고 길을 열지어다 🌸</h2>", unsafe_allow_html=True)

# 떠다니는 이모지(하얀피크민 느낌)
for i, (top, left, emoji) in enumerate([
    ("12%", "8%", "🤍"),
    ("20%", "82%", "🌸"),
    ("72%", "6%", "🤍"),
    ("85%", "80%", "🌟"),
    ("40%", "90%", "🌸"),
    ("60%", "12%", "🤍"),
]):
    st.markdown(f"""
    <div class='sparkle' style='top:{top}; left:{left}; animation-delay:{i*0.6}s;'>{emoji}</div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# MBTI 16 유형 & 직업 추천 (하얀피크민 버전 라벨)
# ----------------------------
mbti_jobs = {
    "INTJ": ["독성 데이터 분석가 🤍🧪", "전략 설계자 🧠", "AI 연구원 🔬"],
    "INTP": ["알고리즘 아키텍트 🧩", "리서치 프로그래머 💻", "지식 시스템 설계자 📚"],
    "ENTJ": ["프로덕트 오너 🏰", "조직 전략가 📈", "벤처 빌더 🚀"],
    "ENTP": ["혁신가 ⚡", "크리에이티브 플래너 🎨", "테크 에반젤리스트 📣"],
    "INFJ": ["상담 심리사 💬", "교육 디자이너 🎓", "커뮤니티 빌더 🕊"],
    "INFP": ["콘텐츠 크리에이터 ✍️", "브랜드 스토리텔러 📖", "사회 혁신가 🌱"],
    "ENFJ": ["에듀 리더 👩‍🏫", "조직 코치 🧭", "인재 개발자 💞"],
    "ENFP": ["캠페인 메이커 🎉", "여행·문화 기획자 🌍", "크리에이티브 디렉터 🎬"],
    "ISTJ": ["회계·재무 전문가 🧾", "품질 관리자 🧱", "공공행정 사무관 🏛"],
    "ISFJ": ["간호·보건 전문가 🏥", "사회복지사 🤝", "아동교육 교사 🧸"],
    "ESTJ": ["운영 매니저 🗂", "생산·공정 관리자 🏭", "프로젝트 매니저 🧱"],
    "ESFJ": ["고객경험 매니저 💝", "이벤트 디렉터 🎈", "의료코디네이터 🩺"],
    "ISTP": ["정밀 엔지니어 🔧", "현장 솔버 🛠", "보안·포렌식 분석가 🕵️"],
    "ISFP": ["UX/UI 디자이너 🖌", "뮤지션/사운드메이커 🎶", "플로리스트 🌸"],
    "ESTP": ["세일즈 스페셜리스트 🏆", "스포츠 코치 🏃", "응급 구조(현장) 요원 🚑"],
    "ESFP": ["퍼포머/배우 🎭", "이벤트 플래너 🎊", "리테일 크리에이터 🛍"],
}

# ----------------------------
# 선택 UI
# ----------------------------
col1, col2 = st.columns([1,1])
with col1:
    mbti = st.selectbox("🔮 당신의 MBTI를 고르세요", list(mbti_jobs.keys()), index=0)
with col2:
    vibe = st.select_slider("✨ 왕의 오라", options=["순백", "은은", "반짝", "광휘"], value="반짝")

if vibe in ["반짝", "광휘"]:
    st.balloons()

st.markdown(f"""
<div style="text-align:center; margin-top:10px;">
  <span class="badge">하얀피크민 권능: 독 저항·민첩 부스트 · 은밀 탐사</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# 결과 출력
# ----------------------------
st.markdown(
    f"<h3 style='text-align:center; font-size:30px;'>👑 {mbti} · 하얀피크민의 가호가 내린 추천 직업 👑</h3>",
    unsafe_allow_html=True
)

for job in mbti_jobs[mbti]:
    st.markdown(f"<div class='pill'>🤍🌸 {job}</div>", unsafe_allow_html=True)

st.info("💡 MBTI는 길잡이일 뿐! 진짜 진로는 경험·관심·역량의 합으로 결정돼요. 하얀피크민처럼 빠르고 똑똑하게 탐험해봐요 ✨")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size:14px; color:#666;'>© 하얀피크민의 왕국 · Designed with love 🤍</div>",
    unsafe_allow_html=True
)
