import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="전체 근육 운동 가이드", layout="wide")
st.title("💪 전체 근육 운동 가이드")

# 운동 데이터: (운동명, 이미지URL, 영상URL, 난이도 팁, 마무리 스트레칭)
exercise_data = {
    "승모근": {
        "초급":[("어깨 으쓱하기 10회","https://i.imgur.com/UYiroysl.jpg","https://www.youtube.com/watch?v=IODxDxX7oi4","승모근 긴장 완화","팔 스트레칭 1분")],
        "중급":[("덤벨 슈러그 10회","https://i.imgur.com/5tj6S7Ol.jpg","https://www.youtube.com/watch?v=8VmA3Tbti2A","승모근 강화","팔 스트레칭 1분")],
        "고급":[("바벨 슈러그 15회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=7sJ1JkK1rS0","고강도 승모근 운동","팔 스트레칭 1분")],
    },
    "어깨": {
        "초급":[("어깨 돌리기 10회","https://i.imgur.com/5tj6S7Ol.jpg","https://www.youtube.com/watch?v=B-aVuyhvLHU","어깨 근육 풀기","어깨 스트레칭 1분")],
        "중급":[("덤벨 숄더 프레스 10회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=B-aVuyhvLHU","어깨 근력 향상","어깨 스트레칭 1분")],
        "고급":[("푸시프레스 12회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=eGo4IYlbE5g","상체 근력 강화","어깨 스트레칭 1분")],
    },
    "팔": {
        "초급":[("푸시업 10회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=IODxDxX7oi4","팔 근력 강화","팔 스트레칭 1분")],
        "중급":[("덤벨 컬 12회","https://i.imgur.com/UYiroysl.jpg","https://www.youtube.com/watch?v=ykJmrZ5v0Oo","이두 근육 강화","팔 스트레칭 1분")],
        "고급":[("친업 8회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=eGo4IYlbE5g","팔+등 복합 강화","팔 스트레칭 1분")],
    },
    "등": {
        "초급":[("고양이-소 자세 5분","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=kqnua4rHVVA","척추 유연성 향상","등 스트레칭 1분")],
        "중급":[("덤벨 로우 12회","https://i.imgur.com/5tj6S7Ol.jpg","https://www.youtube.com/watch?v=pYcpY20QaE8","등 근력 강화","등 스트레칭 1분")],
        "고급":[("바벨 로우 12회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=2yjwXTZQDDI","고강도 등 근육 운동","등 스트레칭 1분")],
    },
    "배": {
        "초급":[("크런치 10회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=7vAQ4sU6F34","복근 강화","복부 스트레칭 1분")],
        "중급":[("레그레이즈 12회","https://i.imgur.com/UYiroysl.jpg","https://www.youtube.com/watch?v=JB2oyawG9KI","하복근 강화","복부 스트레칭 1분")],
        "고급":[("바이시클 크런치 15회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=9FGilxCbdz8","복근 집중 강화","복부 스트레칭 1분")],
    },
    "허리": {
        "초급":[("무릎 당기기 10회","https://i.imgur.com/5tj6S7Ol.jpg","https://www.youtube.com/watch?v=4pKly2JojMw","허리 긴장 완화","허리 스트레칭 1분")],
        "중급":[("브릿지 10회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=8bbE64NuDTU","허리 근력 강화","허리 스트레칭 1분")],
        "고급":[("데드리프트 10회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=op9kVnSso6Q","허리+하체 강화","허리 스트레칭 1분")],
    },
    "허벅지": {
        "초급":[("스쿼트 10회","https://i.imgur.com/UYiroysl.jpg","https://www.youtube.com/watch?v=aclHkVaku9U","허벅지 근력 강화","허벅지 스트레칭 1분")],
        "중급":[("런지 12회","https://i.imgur.com/5tj6S7Ol.jpg","https://www.youtube.com/watch?v=QOVaHwm-Q6U","허벅지 근력 향상","허벅지 스트레칭 1분")],
        "고급":[("점프 스쿼트 15회","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=CVaEhXotL7M","고강도 하체 운동","허벅지 스트레칭 1분")],
    },
    "종아리": {
        "초급":[("종아리 스트레칭 5분","https://i.imgur.com/VKX4l4nl.jpg","https://www.youtube.com/watch?v=YMmgqO8Jo-k","종아리 긴장 완화","종아리 스트레칭 1분")],
        "중급":[("카프 레이즈 12회","https://i.imgur.com/UYiroysl.jpg","https://www.youtube.com/watch?v=YMmgqO8Jo-k","종아리 근력 강화","종아리 스트레칭 1분")],
        "고급":[("점프 카프 레이즈 15회","https://i.imgur.com/3GvwNBMl.jpg","https://www.youtube.com/watch?v=YMmgqO8Jo-k","고강도 종아리 운동","종아리 스트레칭 1분")],
    },
}

# 세션 상태 초기화
if "log" not in st.session_state:
    st.session_state["log"] = []

# 난이도 선택
level = st.radio("난이도를 선택하세요", ["초급","중급","고급"])
st.subheader(f"{level} 전체 근육 운동")

# 모든 부위 운동 표시
for muscle, exercises in exercise_data.items():
    st.markdown(f"### {muscle}")
    for ex, img, video, tip, stretch in exercises[level]:
        completed = st.checkbox(f"{ex} - {tip} (마무리: {stretch})", key=f"{muscle}_{ex}")
        st.image(img, width=300)
        st.video(video)
        if completed:
            today = datetime.date.today()
            if not any(log['날짜']==today and log['운동']==ex for log in st.session_state["log"]):
                st.session_state["log"].append({"날짜": today, "운동": ex})
                st.success(f"✅ '{ex}' 기록 완료!")

# 주간 운동 시각화
if st.session_state["log"]:
    df = pd.DataFrame(st.session_state["log"])
    weekly_count = df.groupby(["날짜"]).count()
    st.subheader("주간 운동 횟수")
    st.line_chart(weekly_count["운동"])

