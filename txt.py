import streamlit as st
import pandas as pd
import datetime

st.title("근육별 스트레칭 & 운동 가이드💪")

# 샘플 운동 데이터 (텍스트, 이미지, 영상 URL)
exercise_data = {
    "어깨": {
        "초급": [("어깨 돌리기 10회", "shoulder1.jpg", "https://youtu.be/shoulder1"), 
                 ("밴드 스트레칭 5분", "shoulder2.jpg", "https://youtu.be/shoulder2")],
        "중급": [("덤벨 숄더 프레스 10회", "shoulder3.jpg", "https://youtu.be/shoulder3"), 
                 ("푸시업 10회", "shoulder4.jpg", "https://youtu.be/shoulder4")],
        "고급": [("풀업 5회", "shoulder5.jpg", "https://youtu.be/shoulder5"), 
                 ("어깨 서킷 15분", "shoulder6.jpg", "https://youtu.be/shoulder6")]
    },
    "허리": {
        "초급": [("무릎 당기기 10회", "back1.jpg", "https://youtu.be/back1"), 
                 ("고양이-소 자세 5분", "back2.jpg", "https://youtu.be/back2")],
        "중급": [("브릿지 10회", "back3.jpg", "https://youtu.be/back3"), 
                 ("플랭크 30초 x3", "back4.jpg", "https://youtu.be/back4")],
        "고급": [("데드리프트 10회", "back5.jpg", "https://youtu.be/back5"), 
                 ("백 익스텐션 15회", "back6.jpg", "https://youtu.be/back6")]
    },
    "다리": {
        "초급": [("종아리 스트레칭 5분", "leg1.jpg", "https://youtu.be/leg1"), 
                 ("스쿼트 10회", "leg2.jpg", "https://youtu.be/leg2")],
        "중급": [("런지 10회", "leg3.jpg", "https://youtu.be/leg3"), 
                 ("레그 익스텐션 15회", "leg4.jpg", "https://youtu.be/leg4")],
        "고급": [("점프 스쿼트 10회", "leg5.jpg", "https://youtu.be/leg5"), 
                 ("힙 쓰러스트 15회", "leg6.jpg", "https://youtu.be/leg6")]
    }
}

# 세션 상태 초기화
if "log" not in st.session_state:
    st.session_state["log"] = []

# 부위 & 난이도 선택
muscle = st.selectbox("부위를 선택하세요", list(exercise_data.keys()))
level = st.radio("난이도를 선택하세요", ["초급", "중급", "고급"])

st.subheader(f"{muscle} - {level} 추천 운동/스트레칭")

# 체크박스 형태로 운동 표시
for ex, img, video in exercise_data[muscle][level]:
    completed = st.checkbox(ex, key=ex)
    st.image(img, width=300)
    st.video(video)
    if completed:
        today = datetime.date.today()
        # 이미 기록에 없으면 추가
        if not any(log['날짜']==today and log['운동']==ex for log in st.session_state["log"]):
            st.session_state["log"].append({"날짜": today, "운동": ex})
            st.success(f"✅ '{ex}' 기록 완료!")

# 주간 운동 시각화
if st.session_state["log"]:
    df = pd.DataFrame(st.session_state["log"])
    weekly_count = df.groupby(["날짜"]).count()
    st.subheader("주간 운동 횟수")
    st.line_chart(weekly_count["운동"])
import streamlit as st
import requests
import datetime

API_KEY = "YOUR_API_KEY"  # OpenWeatherMap API Key 입력
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

