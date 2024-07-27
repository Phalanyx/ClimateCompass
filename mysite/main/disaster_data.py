import requests
import json
import datetime
from decouple import config

type = "FLOOD"
key = config('KEY')
new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
&feed=kontur-public&types={type}
&severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..&limit=20&sortOrder=ASC&episodeFilterType=ANY"""
response = requests.get(new_req).json()
print(response)


def get_disaster_data(type, key, date):
    new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
    &feed=kontur-public&types={type}
    &severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..&limit=20&sortOrder=ASC&episodeFilterType=ANY"""
    response = requests.get(new_req).json()
    return response