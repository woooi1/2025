import streamlit as st

st.set_page_config(page_title="운동 & 스트레칭 웹앱 (한국 영상)", layout="wide")

# 영상 데이터 (한국 유튜버 영상)
pre_stretch = {"name": "전신 스트레칭 종결판", "video": "https://www.youtube.com/embed/oquaP1cFBqY"}

workouts = {
    "초급": {"하체(스쿼트)": {"name": "스쿼트 누구나 쉽게", "video": "https://www.youtube.com/embed/VEwqIDK2DCM"}},
    "중급": {"하체 라이브": {"name": "하체 운동 라이브 데드-스쿼트", "video": "https://www.youtube.com/embed/RX_xS_qrxYI"}},
    "고급": {"힙 챌린지": {"name": "힙으뜸 스쿼트 100개 챌린지", "video": "https://www.youtube.com/embed/urOSaROmTIk"}}
}

post_stretch = {"name": "매일 10분 전신 스트레칭 체조", "video": "https://www.youtube.com/embed/kB0_xQdt2ow"}

#  UI 구성
st.title("🇰🇷 한국 영상만 모은 운동 & 스트레칭 웹앱")

# --- 운동 전 스트레칭
st.header("① 운동 전 스트레칭")
st.subheader(pre_stretch["name"])
st.video(pre_stretch["video"])

# --- 난이도 선택
st.markdown("---")
level = st.radio("② 난이도를 선택하세요", list(workouts.keys()))

# --- 운동 루틴
st.header(f"③ {level} 루틴")
for part, info in workouts[level].items():
    st.subheader(part)
    st.write(f"▶ {info['name']}")
    st.video(info["video"])

# --- 운동 후 스트레칭
st.markdown("---")
st.header("④ 운동 후 스트레칭")
st.subheader(post_stretch["name"])
st.video(post_stretch["video"])st.header(f"{level} 루틴 - 선택 부위: {', '.join(muscle)}")
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
