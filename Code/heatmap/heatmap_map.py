import pandas as pd
import folium
from folium.plugins import HeatMap

# retrieves necessary columns from coordinate dataset outputted by coordinate_api.py
df = pd.read_csv("address_coordinates.csv") 
df = df[["time", "latitude", "longitude"]]

# centers folium map in the middle of Duke University
duke_center = (36.0014, -78.9382)
m = folium.Map(location=duke_center, zoom_start=14)

# uses list comprehension to reorder columns to generate heatmap
heat_data = [[lat, lng, time] for time, lat, lng in df.values.tolist()]
HeatMap(heat_data).add_to(m)
m.save("heatmap_map.html")