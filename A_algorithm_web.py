import streamlit as st
import json
import networkx as nx
import geopy.distance
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from train_graph import G

# Load and process station data
with open('sorted_stations.json', 'r', encoding='utf-8') as file:
    all_stations = json.load(file)

# Graph loading (assuming G is already created and saved)

def is_transfer_station(station):
    for station_info in all_stations:
        if station_info["역이름"] == station:
            return len(station_info["호선"]) > 1
    return False

def heuristic(u, v):
    return 0

def get_station_lines(station):
    for station_info in all_stations:
        if station_info["역이름"] == station:
            return station_info["호선"]
    return []

st.title("지하철 경로 탐색")

# Select boxes for source and destination
source = st.selectbox("출발역을 선택하세요", list(G.nodes))
destination = st.selectbox("도착역을 선택하세요", list(G.nodes))

if st.button("경로 찾기"):
    try:
        shortest_path = nx.astar_path(G, source, destination, heuristic)
        st.write("Shortest path:", shortest_path)

        transfer_stations = []
        for i in range(1, len(shortest_path) - 1):
            prev_station = shortest_path[i - 1]
            current_station = shortest_path[i]
            next_station = shortest_path[i + 1]

            prev_lines = set(get_station_lines(prev_station))
            current_lines = set(get_station_lines(current_station))
            next_lines = set(get_station_lines(next_station))

            if (not prev_lines & next_lines) and (prev_lines & current_lines) and (current_lines & next_lines):
                transfer_stations.append(current_station)

        st.write("환승역:", transfer_stations)
    except nx.NetworkXNoPath:
        st.error("경로를 찾을 수 없습니다.")

# Optional: Display the graph (might need adjustments for large graphs)
# plt.figure(figsize=(10, 10))
# nx.draw(G, with_labels=True, font_weight='bold')
# st.pyplot(plt)

