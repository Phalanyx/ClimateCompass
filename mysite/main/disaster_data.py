import requests
import json
import datetime
from decouple import config
import math
def get_square_bounding_box(center_lat, center_lon, side_length):
    """
    Calculate the corners of a square bounding box given its center and side length.
    
    Parameters:
    center_lat (float): Latitude of the center point.
    center_lon (float): Longitude of the center point.
    side_length (float): Side length of the square in degrees.
    
    Returns:
    tuple: A tuple containing four values:
           (min_longitude, min_latitude, max_longitude, max_latitude)
    """
    half_side = side_length / 2
    
    min_lat = center_lat - half_side
    max_lat = center_lat + half_side
    min_lon = center_lon - half_side
    max_lon = center_lon + half_side
    
    return min_lon, min_lat, max_lon, max_lat

# Example usage:
center_latitude = 15.1666665 

center_longitude = 47.2500001  # Example center longitude
side_length = 1.0  # Example side length in degrees

bounding_box = get_square_bounding_box(center_latitude, center_longitude, side_length)
print(f"The bounding box is: {bounding_box}")

def get_disaster_data(type, key, date, lat, lon):
    min_lon, min_lat, max_lon, max_lat = get_square_bounding_box(lat, lon, 1.0)
    new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
    &feed=kontur-public&types={type}
    &severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..
    &bbox={min_lon}&bbox={min_lat}&bbox={max_lon}&bbox={max_lat}
    &limit=20&sortOrder=ASC&episodeFilterType=ANY"""
    response = requests.get(new_req).json()
    return response

def get_polygons(response):
    try:
        val = response['features'][1]['geometry']['coordinates']
    except:
        print("Error: No polygons found")
    return val

def get_active_hazard(response):
    pass

type = "FLOOD"
key = config('KEY')

#response = requests.get(new_req).json()
#for x in response:
#    print(x)

#print(response["type"]) 

