import requests
import json
import datetime
from decouple import config
d = datetime.datetime.now().isoformat('T')[:-7]
print(d)
type = "FLOOD"
key = config('KEY')
print(key)
new_req = f"""https://apps.kontur.io/events/v1/geojson/events?access_token={key}
&feed=kontur-public&types={type}
&severities=&datetime=2024-07-27T13%3A27%3A26Z%2F..&limit=20&sortOrder=ASC&episodeFilterType=ANY"""
response = requests.get(new_req).json()
print(response)