import requests
import json
import datetime
from decouple import config
import math
def get_square_bounding_box(center_lat, center_lon ):
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

    
    min_lat = center_lat - 5
    max_lat = center_lat + 5
    min_lon = center_lon - 5
    max_lon = center_lon + 5
    
    return min_lon, min_lat, max_lon, max_lat

# Example usage:
center_latitude = 15.1666665 

center_longitude = 47.2500001  # Example center longitude

bounding_box = get_square_bounding_box(center_latitude, center_longitude)
print(f"The bounding box is: {bounding_box}")

def get_disaster_data(type, date, lat, lon):
    key = config('KEY')
    min_lon, min_lat, max_lon, max_lat = get_square_bounding_box(lat, lon, 1.0)
    new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
    &feed=kontur-public&types={type}
    &severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..
    &bbox={min_lon}&bbox={min_lat}&bbox={max_lon}&bbox={max_lat}
    &limit=20&sortOrder=ASC&episodeFilterType=ANY"""
    response = requests.get(new_req).json()
    return response



def get_active_hazard(lat, lon):
    key = config('KEY')
    min_lon, min_lat, max_lon, max_lat = get_square_bounding_box(lat, lon, 1.0)
    new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
    &feed=kontur-public&types=ALL
    &severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..
    &bbox={min_lon}&bbox={min_lat}&bbox={max_lon}&bbox={max_lat}
    &limit=20&sortOrder=ASC&episodeFilterType=ANY"""
    response = requests.get(new_req).json()
    return response

type = "FLOOD"
key = config('KEY')

#response = requests.get(new_req).json()
#for x in response:
#    print(x)

#print(response["type"]) 

