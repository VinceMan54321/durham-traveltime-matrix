# durham-traveltime-matrix
The main goal of this project/repo was to apply the Helsinki Region Travel Time Matrix as described in a paper by Tenkanen to analyze door-to-door travel times for areas near Duke University. This is for our CS 333 tech demo for Duke University.

Our overall methodology is as follows:
1 - form a location dataset
2 - develop a baseline routing matrix
3 - incorporate door-to-door adjustments
4 - develop heat-map visualizations
5 - evaluate results with real-time testing

## Heatmap Visualizations
The heatmap visualization-related code is all in the heatmap directory. Here is what each file does. Also make sure to install any libraries using pip install if you wish to run this code locally.

Code
heatmap_grid.py - generates a heatmap based on a 6x10 grid that can be overlaid over Duke's map
coordinate_api.py - uses Google Maps' Geocoding API to generate coordinates and outputs address_coordinates.csv
heatmap_map.py - uses folium library to create heatmap_map.html, which is the primary heatmap visualization
heatmap_map.html - shows heatmap circles for each location in the data on a real-world map

Datasets
Location_Dataset.csv - initial dataset containing location info
HeatMapModified.csv - copy of HeatMap.csv that contains travel times but with address column removed
address_coordinates.csv - output of coordinate_api.py, contains locations and coordinates