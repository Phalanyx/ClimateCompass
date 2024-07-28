import requests
import json
import datetime
from decouple import config
import math
from googleplaces import GooglePlaces
import ssl
import certifi
from geopy.geocoders import Nominatim

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




def get_active_hazard(lat, lon):
    key = config('KEY')
    min_lon, min_lat, max_lon, max_lat = get_square_bounding_box(lon, lat)
    print(min_lon, min_lat, max_lon, max_lat)
    new_req = "https://apps.kontur.io/events/v1/geojson/events?access_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjZDhoWXJtTUxpa1RGTUNaa0NGY1lxOTZPWm9hRE1LajZua2gza18wZ0FRIn0.eyJleHAiOjE3MjIzNTQxMDUsImlhdCI6MTcyMjA5NDkwNSwianRpIjoiOTkyODIyN2MtOGUyOS00MzM0LTgzMTYtNGE0NGUxOWJjMWM1IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hazAxLmtvbnR1ci5pby9yZWFsbXMva29udHVyIiwiYXVkIjpbImV2ZW50LWFwaSIsImFjY291bnQiXSwic3ViIjoiZjpiMzM1ZThiYS0yMWVhLTQzMmUtODViZi1jNzhjNWJlODEzMWU6aHV5bmhhbGJAZ21haWwuY29tIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoia29udHVyX3BsYXRmb3JtIiwic2Vzc2lvbl9zdGF0ZSI6IjMzOGY2NjEyLWYzYTgtNDdhOC04YTBkLTJhNmYyNzk4MWU0ZCIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL3Byb2QtZGlzYXN0ZXItbmluamEua29udHVybGFicy5jb20iLCJodHRwczovL2Rpc2FzdGVyLm5pbmphIiwiaHR0cHM6Ly9hcHBzLmtvbnR1ci5pbyJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsIkVWRU5UQVBJX3JlYWQ6ZmVlZDprb250dXItcHVibGljIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZXZlbnQtYXBpIjp7InJvbGVzIjpbInJlYWQ6ZmVlZDprb250dXItcHVibGljIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiIzMzhmNjYxMi1mM2E4LTQ3YTgtOGEwZC0yYTZmMjc5ODFlNGQiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFsYmVydCBIdXluaCIsInByZWZlcnJlZF91c2VybmFtZSI6Imh1eW5oYWxiQGdtYWlsLmNvbSIsImdpdmVuX25hbWUiOiJBbGJlcnQgSHV5bmgiLCJmYW1pbHlfbmFtZSI6IiIsImVtYWlsIjoiaHV5bmhhbGJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJodXluaGFsYkBnbWFpbC5jb20ifQ.WZA5VxP4PU-jNQ1JCSWmz5dJz0gy0PJJ-GkjwzXGqn0gKGWU99AECar5bJU3_0ltluq9me0JX5yOiLBPpIndujK5OoXidhpXa4bxhbGD3UJKjTSU_3FNuMmH0koXRNfXR3sGhmqXNxowRWKEgZzfksqis2GtlIgIrS9WYJo2wHPJGgUFbIjGZkrJeB_FxUWXi_YxjxRfsPgHerQKIG-3TWub7fD7am3wcaaNZA2JdxCgFZDpM3pCjipHdB63fsjsCWxRrSXZJir8_hbg-vM0gMSs5cqM7gsjsmW2XhGCh1M0LoRZoyYFiaIhYgr0EcjDl7Z6zStPRy5G20yQCkAb-Q&feed=kontur-public&types=FLOOD&severities=&datetime=2024-07-27T00%3A00%3A00Z%2F..&bbox=10&bbox=42&bbox=20&bbox=52&limit=20&sortOrder=ASC&episodeFilterType=LATEST"
    response = requests.get(new_req).json()
    for x in response:
        print(x)

    return response


print(get_active_hazard(15.1666665, 47.2500001))



type = "FLOOD"
key = config('KEY')
#response = requests.get(new_req).json()
#for x in response:
#    print(x)

#print(response["type"]) 


def find_refuge(lat, lon):
    google_places = GooglePlaces("AIzaSyCDC6_hxlug2x1PM_wP9ocUsgaDWXyNAkE")

    query_result = google_places.text_search(
    lat_lng={'lat': lat, 'lng': lon}, 
    query='Homeless Shelter',
    radius=5000
    )
    ret = []
    for place in query_result.places:
        place.get_details()
        name = place.name
        latitude = place.geo_location['lat']
        longitude = place.geo_location['lng']
        ret.append([name, latitude, longitude])
    return ret

def get_news():
    api_key = "7a54072947014d7db0bb2a6ee7da9cf9"

    # Define the endpoint and parameters
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'fire AND Jasper, Canada',
        'apiKey': api_key,
        'pageSize': 5,  # number of articles to retrieve
        'sortBy': 'publishedAt',  # sort articles by published date
        'language': 'en'  # get articles in English
    }
    articles = []
    # Make the request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        articles = response.json().get('articles')
        
        # Print the top articles

        for i, article in enumerate(articles, start=1):
            print(f"Article {i}:")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("-" * 40)
            articles.append(article)
            if (i == 5):
                break

    else:
        print(f"Failed to fetch news articles: {response.status_code}")
    return articles

def addy_to_coords(address):
        # Create an SSL context with the certifi certificate bundle
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Create a custom adapter to use the SSL context
    from geopy.adapters import RequestsAdapter

    class CertifiAdapter(RequestsAdapter):
        def __init__(self, *args, **kwargs):
            kwargs['ssl_context'] = ssl_context
            super().__init__(*args, **kwargs)

    # Initialize the Nominatim geocoder with the custom adapter
    geolocator = Nominatim(user_agent="Geopy Library", adapter_factory=CertifiAdapter)

    # Entering the location name
    getLoc = geolocator.geocode(address)

    if getLoc:
        # Printing address
        print(getLoc.address)
        return [getLoc.longitude, getLoc.latitude]
    else:
        print("Location not found")
        return [15.1666665, 47.2500001]