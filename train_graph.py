import json
import networkx as nx
import geopy.distance
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'  # Adjust path as needed
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()


with open('sorted_stations.json', 'r', encoding='utf-8') as file:
    all_stations = json.load(file)
 # 그래프 생성
G = nx.Graph()   

#1호선 역 리스트 
line_1_stations=["소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문", "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청", "서울역", "남영", "용산", "노량진", "대방", "신길", "영등포", "신도림", "구로", "가산디지털단지", "독산", "금천구청", "석수", "관악", "안양", "명학", "금정", "군포", "당정", "의왕", "성균관대", "화서", "수원", "세류", "병점", "세마", "오산대", "오산", "진위", "송탄", "서정리", "평택지제", "평택", "성환", "직산", "두정", "천안", "봉명", "쌍용", "아산", "탕정", "배방", "온양온천", "신창"]
line_1_coordinates={station['역이름']:(station['좌표']['Latitude'],station['좌표']['Longitude']) for station in all_stations if station['역이름'] in line_1_stations}
for i in range(len(line_1_stations)-1):
    station1=line_1_stations[i].strip()
    station2=line_1_stations[i+1].strip()
    coord1=line_1_coordinates[station1]
    coord2=line_1_coordinates[station2]
    distance=geopy.distance.distance(coord1,coord2).km
    G.add_edge(station1,station2,weight=distance)
line_1_branch=["구로", "구일", "개봉", "오류동", "온수", "역곡", "소사", "부천", "중동", "송내", "부개", "부평", "백운", "동암", "간석", "주안", "도화", "제물포", "도원", "동인천", "인천"]
for i in range(len(line_1_branch) - 1):
    station1=line_1_branch[i].strip()
    station2=line_1_branch[i + 1].strip()
    coord1=line_1_coordinates.get(station1)
    coord2=line_1_coordinates.get(station2)
    if coord1 and coord2:
        distance=geopy.distance.distance(coord1, coord2).km
        G.add_edge(station1,station2,weight=distance)
G.add_edge("서동탄","병점",weight=1)
G.add_edge("금천구청","광명",weight=1)

#2호선 역 리스트 
line_2_stations=["성수", "건대입구", "구의", "강변", "잠실나루", "잠실","잠실새내", "종합운동장", "삼성", "선릉", "역삼", "강남", "교대", "서초", "방배", "사당", "낙성대", "서울대입구", "봉천", "신림", "신대방", "구로디지털단지", "대림", "신도림", "문래", "영등포구청", "당산", "합정", "홍대입구", "신촌", "이대", "아현", "충정로", "시청", "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리", "한양대", "뚝섬","성수"]
line_2_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_2_stations}
for i in range(len(line_2_stations) - 1):
    station1=line_2_stations[i].strip()
    station2=line_2_stations[i + 1].strip()
    coord1=line_2_coordinates[station1]
    coord2=line_2_coordinates[station2] 
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)
line_2_branch1=["신설동","용두","신답","용답","성수"]
line_2_branch2=["까치산","신정네거리","양천구청","도림천","신도림"]
    #1번째 지선 추가 
for i in range(len(line_2_branch1) - 1):
    station1=line_2_branch1[i].strip()
    station2=line_2_branch1[i + 1].strip()
    coord1=line_2_coordinates.get(station1)
    coord2=line_2_coordinates.get(station2)
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)
    #2번째 지선 추가
for i in range(len(line_2_branch2) - 1):
    station1 = line_2_branch2[i].strip()
    station2 = line_2_branch2[i + 1].strip()
    # 역 간의 좌표 추출 및 거리 계산
    coord1 = line_2_coordinates.get(station1)
    coord2 = line_2_coordinates.get(station2)
    distance = geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1, station2, weight=distance)

#3호선 역 리스트 
line_3_stations=["대화", "주엽", "정발산", "마두", "백석", "대곡", "화정", "원당", "원흥", "삼송", "지축", "구파발", "연신내", "불광", "녹번", "홍제", "무악재", "독립문", "경복궁", "안국", "종로3가", "을지로3가", "충무로", "동대입구", "약수", "금호", "옥수", "압구정", "신사", "잠원", "고속터미널", "교대", "남부터미널", "양재", "매봉", "도곡", "대치", "학여울", "대청", "일원", "수서", "가락시장", "경찰병원", "오금"]
line_3_coordinates={station['역이름']:(station['좌표']['Latitude'],station['좌표']['Longitude']) for station in all_stations if station['역이름'] in line_3_stations}
for i in range(len(line_3_stations)-1):
    station1=line_3_stations[i].strip()
    station2=line_3_stations[i+1].strip()
    coord1=line_3_coordinates[station1]
    coord2=line_3_coordinates[station2]
    distance=geopy.distance.distance(coord1,coord2).km
    G.add_edge(station1,station2,weight=distance)

#4호선 역 리스트
line_4_stations=["당고개", "상계", "노원", "창동", "쌍문", "수유", "미아", "미아사거리", "길음", "성신여대입구", "한성대입구", "혜화", "동대문", "동대문역사문화공원", "충무로", "명동", "회현", "서울역", "숙대입구", "삼각지", "신용산", "이촌", "동작", "총신대입구", "사당", "남태령", "선바위", "경마공원", "대공원", "과천", "정부과천청사", "인덕원", "평촌", "범계", "금정", "산본", "수리산", "대야미", "반월", "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕", "오이도"]
line_4_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_4_stations}
for i in range(len(line_4_stations) - 1):
    station1=line_4_stations[i].strip()
    station2=line_4_stations[i + 1].strip()
    coord1=line_4_coordinates[station1]
    coord2=line_4_coordinates[station2]
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)

#5호선 역 리스트
line_5_stations=["방화", "개화산", "김포공항", "송정", "마곡", "발산", "우장산", "화곡", "까치산", "신정", "목동", "오목교", "양평", "영등포구청", "영등포시장", "신길", "여의도", "여의나루", "마포", "공덕", "애오개", "충정로", "서대문", "광화문", "종로3가", "을지로4가", "동대문역사문화공원", "청구", "신금호", "행당", "왕십리", "마장", "답십리", "장한평", "군자", "아차산", "광나루", "천호", "강동", "길동", "굽은다리", "명일", "고덕", "상일동", "강일", "미사", "하남풍산", "하남시청", "하남검단산"]
line_5_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_5_stations}
for i in range(len(line_5_stations) - 1):
    station1=line_5_stations[i].strip()
    station2=line_5_stations[i + 1].strip()
    coord1=line_5_coordinates[station1]
    coord2=line_5_coordinates[station2]
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)
line_5_branch=["강동", "둔촌동", "올림픽공원", "방이", "오금", "개롱", "거여", "마천"]
for i in range(len(line_5_branch) - 1):
    station1=line_5_branch[i].strip()
    station2=line_5_branch[i + 1].strip()
    coord1=line_5_coordinates.get(station1)
    coord2=line_5_coordinates.get(station2)
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)

#6호선 역 리스트
line_6_stations=["신내", "봉화산", "화랑대", "태릉입구", "석계", "돌곶이", "상월곡", "월곡", "고려대", "안암", "보문", "창신", "동묘앞", "신당", "청구", "약수", "버티고개", "한강진", "이태원", "녹사평", "삼각지", "효창공원앞", "공덕", "대흥", "광흥창", "상수", "합정", "망원", "마포구청", "월드컵경기장", "디지털미디어시티", "증산", "새절", "응암", "역촌", "불광", "독바위", "연신내", "구산", "응암"]
line_6_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_6_stations}
for i in range(len(line_6_stations) - 1):
    station1=line_6_stations[i].strip()
    station2=line_6_stations[i + 1].strip()
    coord1=line_6_coordinates[station1]
    coord2=line_6_coordinates[station2]
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)

#7호선 역 리스트
line_7_stations=["장암", "도봉산", "수락산", "마들", "노원", "중계", "하계", "공릉", "태릉입구", "먹골", "중화", "상봉", "면목", "사가정", "용마산", "중곡", "군자", "어린이대공원", "건대입구", "뚝섬유원지", "청담", "강남구청", "학동", "논현", "반포", "고속터미널", "내방", "총신대입구", "남성", "숭실대입구", "사당", "장승배기", "신대방삼거리", "보라매", "신풍", "대림", "남구로", "가산디지털단지", "철산", "광명사거리", "천왕", "온수", "까치울", "부천종합운동장", "춘의", "신중동", "부천시청", "상동", "삼산체육관", "굴포천", "부평구청", "산곡", "석남"]
line_7_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_7_stations}
for i in range(len(line_7_stations) - 1):
    station1=line_7_stations[i].strip()
    station2=line_7_stations[i + 1].strip()
    coord1=line_7_coordinates[station1]
    coord2=line_7_coordinates[station2]
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)

# 8호선 역 리스트
line_8_stations = ["암사", "천호", "강동구청", "몽촌토성", "잠실", "석촌", "송파", "가락시장", "문정", "장지", "복정", "산성", "남한산성입구", "단대오거리", "신흥", "수진", "모란"]
# 8호선 역의 좌표만 추출
stations_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_8_stations}
# 8호선 역들을 노드로 추가하고 간선(연결) 생성
for i in range(len(line_8_stations) - 1):
    station1 = line_8_stations[i]
    station2 = line_8_stations[i + 1]
    # 역 간의 거리 계산
    coord1 = stations_coordinates[station1]
    coord2 = stations_coordinates[station2]
    distance = geopy.distance.distance(coord1, coord2).km
    # 노드 추가 및 가중치를 거리로 설정하여 간선 추가
    G.add_edge(station1, station2, weight=distance)

# 9호선 역 리스트
line_9_stations=["개화", "김포공항", "공항시장", "신방화", "마곡나루", "양천향교", "가양", "증미", "등촌", "염창", "신목동", "선유도", "당산", "국회의사당", "여의도", "샛강", "노량진", "노들", "흑석", "동작", "구반포", "신반포", "고속터미널", "신논현", "언주", "선정릉", "삼성중앙", "봉은사", "종합운동장", "삼전", "석촌고분", "석촌", "송파나루", "한성백제", "올림픽공원", "둔촌오륜", "중앙보훈병원"]
line_9_coordinates = {station["역이름"]: (station["좌표"]["Latitude"], station["좌표"]["Longitude"]) for station in all_stations if station["역이름"] in line_9_stations}
for i in range(len(line_9_stations) - 1):
    station1=line_9_stations[i].strip()
    station2=line_9_stations[i + 1].strip()
    coord1=line_9_coordinates[station1]
    coord2=line_9_coordinates[station2]
    distance=geopy.distance.distance(coord1, coord2).km
    G.add_edge(station1,station2,weight=distance)


# Format edge weights to two decimal places
for u, v, d in G.edges(data=True):
    d['weight'] = round(d['weight'], 2)

# Graph layout
pos = nx.spring_layout(G, k=0.15, iterations=20)  # Adjust layout parameters for better appearance

# Draw the graph
plt.figure(figsize=(12, 12))  # Increase figure size for better visibility
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700, alpha=0.8)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_family=font_prop.get_name(), font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Display the graph
plt.axis('off')
plt.tight_layout()
plt.show()
