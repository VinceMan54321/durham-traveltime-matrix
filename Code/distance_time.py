import googlemaps
import pandas as pd
from datetime import datetime

df = pd.read_csv('location_dataset.csv')

def get_distance_and_time(api_key, origin_address, destination_address):
    gmaps = googlemaps.Client(key=api_key)

    # Geocode the addresses to get latitude and longitude
    origin_location = gmaps.geocode(origin_address)[0]['geometry']['location']
    destination_location = gmaps.geocode(destination_address)[0]['geometry']['location']

    # Get the distance matrix
    result = gmaps.distance_matrix(
        origins=(origin_location['lat'], origin_location['lng']),
        destinations=(destination_location['lat'], destination_location['lng']),
        mode="transit",
        departure_time=datetime.now()
    )

    # Extract the distance from the result
    distance = result['rows'][0]['elements'][0]['distance']['text']
    duration = result['rows'][0]['elements'][0]['duration']['text']

    return distance, duration

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
api_key = 'AIzaSyDdOtd4C4C32UcKZihI70BSf8bcdzQYqXs'
api_key2 = 'AIzaSyDZZXA299PDImjwzm65wfx4rrDnUsa-T9Q'
origin_address = '1328 Campus Drive, Durham, NC 27705'  # Googleplex
destination_address = '1312 Campus Drive, Durham, NC 27705'  # Apple Campus

distance, duration = get_distance_and_time(api_key, origin_address, destination_address)
