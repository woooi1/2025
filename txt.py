import streamlit as st
import requests
import datetime

API_KEY = "YOUR_API_KEY"  # OpenWeatherMap API Key 입력
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 옷차림 추천 함수
def recommend_outfit(temp, weather, style="casual"):
    if temp >= 28:
        outfit = "반팔, 반바지"
    elif 20 <= temp < 28:
        outfit = "얇은 긴팔, 청바지"
    elif 10 <= temp < 20:
        outfit = "자켓, 니트"
    elif 0 <= temp < 10:
        outfit = "코트, 머플러"
    else:
        outfit = "두꺼운 패딩, 장갑"

    if "rain" in weather.lower():
        outfit += " + 우산"
    if "snow" in weather.lower():
        outfit += " + 방수 신발"

    # 스타일 옵션 반영
    if style == "formal":
        outfit += " (포멀 버전: 셔츠 + 슬랙스)"
    elif style == "sporty":
        outfit += " (스포티 버전: 트레이닝복)"

    return outfit


st.title("오늘의 날씨 기반 옷차림 추천🧥")
city = st.text_input("도시명을 입력하세요", "Seoul")
style = st.radio("스타일을 선택하세요", ["casual", "formal", "sporty"])

if st.button("오늘 날씨 확인"):
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "kr"}
    res = requests.get(BASE_URL, params=params)

    if res.status_code == 200:
        data = res.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        st.metric("현재 기온", f"{temp}°C")
        st.write("날씨:", weather)

        outfit = recommend_outfit(temp, weather, style)
        st.success(f"{date} 기준 추천 옷차림: {outfit}")
    else:
        st.error("도시명을 다시 확인해주세요.")

