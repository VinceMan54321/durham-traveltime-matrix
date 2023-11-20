import csv
import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyBmZwgdt0I2jZrqolnfHZ2zZLOH7GeLwns')
df1 = pd.read_csv("Location_Dataset.csv")
df2 = pd.read_csv("HeatMapModified.csv")
merged_df = pd.merge(df1, df2, on='Name', how='right')
df = merged_df[["Name", "Address", "Time"]]
data = df.values.tolist()
labels = ["name", "address", "time", "latitude", "longitude"]
with open("address_coordinates.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(labels)

for name, address, time in data:
    result = gmaps.geocode(address)
    lat = result[0]['geometry']['location']['lat']
    lng = result[0]['geometry']['location']['lng']
    with open("address_coordinates.csv", "a", newline="") as output:
        writer = csv.writer(output)
        writer.writerow([name, address, time, lat, lng])
