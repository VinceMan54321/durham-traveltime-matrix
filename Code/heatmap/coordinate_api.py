import csv
import googlemaps
import pandas as pd

# key for Google Maps' Geocoding API, restricted to Vincent's IP address
gmaps = googlemaps.Client(key='AIzaSyBmZwgdt0I2jZrqolnfHZ2zZLOH7GeLwns')

# right merged initial dataset with csv containing travel times
locations = pd.read_csv("Location_Dataset.csv")
times = pd.read_csv("HeatMapModified.csv")
combined = pd.merge(locations, times, on='Name', how='right')
df = combined[["Name", "Address", "Time"]]
data = df.values.tolist()

# created new csv containing coordinates needed for heatmap generation
labels = ["name", "address", "time", "latitude", "longitude"]
with open("address_coordinates.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(labels)

# obtains coordinates using Geocoding API and writes to the new csv
for name, address, time in data:
    result = gmaps.geocode(address)
    lat = result[0]['geometry']['location']['lat']
    lng = result[0]['geometry']['location']['lng']
    with open("address_coordinates.csv", "a", newline="") as output:
        writer = csv.writer(output)
        writer.writerow([name, address, time, lat, lng])
