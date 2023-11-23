import streamlit as st
import folium
from streamlit_folium import folium_static
import json

# 호선별 색상 정의
line_colors = {
    "01호선": "blue",
    "02호선": "green",
    "03호선": "orange",
    "04호선": "skyblue",
    "05호선": "purple",
    "06호선": "brown",
    "07호선": "yellow",
    "08호선": "pink",
    "09호선": "red"
}

# JSON 파일 불러오기
with open('sorted_stations.json', 'r', encoding='utf-8') as file:
    stations = json.load(file)

# 서울 지도 생성
map = folium.Map(location=[37.554648, 126.972559], zoom_start=12)

# 각 지하철역의 위치에 마커 추가
for station in stations:
    lat = station['좌표'].get('Latitude')
    lon = station['좌표'].get('Longitude')
    lines = station.get('호선', [])
    
    # 호선별로 색상 지정
    color = "gray"  # 기본 색상
    for line in lines:
        if line in line_colors:
            color = line_colors[line]
            break  # 첫 번째 일치하는 호선의 색상을 사용

    if lat is not None and lon is not None:
        folium.CircleMarker([lat, lon], radius=3, color=color, fill=True, popup=station['역이름']).add_to(map)

# Streamlit에서 지도 표시
st.title('서울 지하철역 위치')
folium_static(map)
