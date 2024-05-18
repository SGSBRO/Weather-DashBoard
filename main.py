import pandas as pd
import streamlit as st
import json
import requests

resp = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&current=temperature_2m,is_day,precipitation,rain,weather_code,wind_speed_10m,wind_direction_10m&hourly=temperature_2m&daily=weather_code,uv_index_max,rain_sum,precipitation_hours&timezone=Asia%2FSingapore")
value = resp.json()


st.title("Weather Dashboard")
st.subheader("Asia/Colombo") 
st.image(f"https://flagcdn.com/80x60/{'lk'}.png")
st.sidebar.write("Latitude: ",value['latitude'],)
st.sidebar.write("Longitude",value['longitude'])
option = st.sidebar.selectbox("test", ("weather_code","uv_index_max", "rain_sum","precipitation_hours"))
st.sidebar.date_input("Dates")

day_night = value['current']['is_day']
# def test()
#     if day_night == 1:
#         st.metric("Day/Night", "Day")
    


col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", value['current']['temperature_2m'])
with col2:
    st.metric("Wind Speed", value['current']['wind_speed_10m'])
with col3:
    if day_night == 1:
        st.metric("Day/Night", "Day")
    else:
        st.metric("Day/Night", "Night")


weather = pd.DataFrame(value ["daily"]["weather_code"], value ["daily"]["time"])
UV_index = pd.DataFrame(value ["daily"]["uv_index_max"], value ["daily"]["time"])
Rain = pd.DataFrame(value ["daily"]["rain_sum"], value ["daily"]["time"])
Precipitation = pd.DataFrame(value ["daily"]["precipitation_hours"], value ["daily"]["time"])

if option == "weather_code":
    st.line_chart(weather)
elif option == "uv_index_max":
    st.line_chart(UV_index)
elif option == "rain_sum":
    st.line_chart(Rain)
else:
    st.line_chart(Precipitation)


st.video("https://www.youtube.com/watch?v=-ZQsFgINBwQ")