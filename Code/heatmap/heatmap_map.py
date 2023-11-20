import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("address_coordinates.csv") 
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
duke_coords = (35.9993, -78.9382)
m = folium.Map(location=duke_coords, zoom_start=14)

heat_data = [[point.xy[1][0], point.xy[0][0], time] for point, time in zip(gdf.geometry, gdf.time)]
HeatMap(heat_data).add_to(m)
m.save("heatmap_map.html")