import json
import networkx as nx
import geopy.distance
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from train_graph import G

font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'  # Adjust path as needed
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()


# Load and process station data
with open('sorted_stations.json', 'r', encoding='utf-8') as file:
    all_stations = json.load(file)

def is_transfer_station(station):
    for station_info in all_stations:
        if station_info["역이름"] == station:
            return len(station_info["호선"]) > 1
    return False

# Define a heuristic function for A*
def heuristic(u, v):
    # You can improve this heuristic based on your specific requirements
    return 0

def get_station_lines(station):
    """Return the lines associated with a station."""
    for station_info in all_stations:
        if station_info["역이름"] == station:
            return station_info["호선"]
    return []

# Calculate the shortest path using A*
shortest_path = nx.astar_path(G, "강동", "삼성", heuristic)
print("Shortest path from 강동 to 삼성 using A*:", shortest_path)

# Print actual transfer stations in the path with debugging
for i in range(1, len(shortest_path) - 1):  # 첫 번째와 마지막 역은 제외
    prev_station = shortest_path[i - 1]
    current_station = shortest_path[i]
    next_station = shortest_path[i + 1]

    prev_lines = set(get_station_lines(prev_station))
    current_lines = set(get_station_lines(current_station))
    next_lines = set(get_station_lines(next_station))

    print(f"Previous: {prev_station}, Current: {current_station}, Next: {next_station}")
    # 환승역 판정 조건 수정
    if (not prev_lines & next_lines) and (prev_lines & current_lines) and (current_lines & next_lines):
        print(f"Transfer station: {current_station}")

"""""
for i in range(1, len(shortest_path) - 1):  # Exclude the first and last stations
    current_station = shortest_path[i]
    next_station = shortest_path[i + 1]

    current_lines = set(get_station_lines(current_station))
    next_lines = set(get_station_lines(next_station))

    # Debugging prints
    print(f"Current: {current_station}, Lines: {current_lines}")
    print(f"Next: {next_station}, Lines: {next_lines}")

    # A transfer is required if the current station's lines don't intersect with either the previous or the next station's lines
    if not (current_lines & next_lines):
        print(f"Transfer station: {current_station}")
"""




