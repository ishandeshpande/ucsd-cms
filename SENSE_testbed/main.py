# importing packages
import networkx as nx
from csv import DictReader
import matplotlib.pyplot as plt
import pandas as pd
import json
import folium


# function to pull location data
def latitude(node_name):
    with open('/Users/ishandeshpande/Downloads/location_data.csv') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            if row['name'] == node_name:
                return row['latitude']


def longitude(node_name):
    with open('/Users/ishandeshpande/Downloads/location_data.csv') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            if row['name'] == node_name:
                return row['longitude']

m = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
m.save("/Users/ishandeshpande/Desktop/map12.html")


# importing files
df = pd.read_csv('/Users/ishandeshpande/Downloads/location_data.csv')
with open('/Users/ishandeshpande/Downloads/sense.json', 'r') as f:
    data = json.load(f)
    data = data["adjacencies"]

    for lines in data:
        node1 = lines["a"]
        node2 = lines["z"]
        folium.Marker([latitude(node1), longitude(node1)], popup="Timberline Lodge", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker([latitude(node2), longitude(node2)], popup="Timberline Lodge", icon=folium.Icon(color="green")).add_to(m)
        folium.PolyLine(locations=[latitude(node1), longitude(node1)], color='darkred', no_clip=True).add_to(animal_map)
        folium.PolyLine(locations=[latitude(node2), longitude(node2)], color='darkorange', no_clip=True).add_to(animal_map)        # mbps = lines["mbps"]
        # if mbps == 10000:
        #     graph.add_edge(node1, node2, color='#f88379', weight=1)
        # if mbps == 20000:
        #     graph.add_edge(node1, node2, color='#f5f5dc', weight=2)
        # if mbps == 100000:
        #     graph.add_edge(node1, node2, color='#e32636', weight=3)
        # else:
        #     graph.add_edge(node1, node2, color='#8b0000', weight=4)
m.save("/Users/ishandeshpande/Desktop/map12.html")



# # drawing graph
# pos = nx.spring_layout(graph)
# edges = graph.edges()
# colors = [graph[u][v]['color'] for u, v in edges]
# weights = [graph[u][v]['weight'] for u, v in edges]
# nx.draw_networkx(graph, pos, font_size=5, node_size=100, edge_color=colors, width=weights, node_color='gray')
# # plt.show()
m