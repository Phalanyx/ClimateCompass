import requests
import json
import datetime
from decouple import config


def get_disaster_data(type, key, date):
    new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
    &feed=kontur-public&types={type}
    &severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..&limit=20&sortOrder=ASC&episodeFilterType=ANY"""
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
new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
&feed=kontur-public&types={type}
&severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..&limit=20&sortOrder=ASC&episodeFilterType=ANY"""
response = requests.get(new_req).json()
for x in response:
    print(x)

print(response["type"])