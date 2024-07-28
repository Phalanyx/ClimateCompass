import requests


url = "https://api.reliefweb.int/v1/disasters"


params = {
    'appname': 'YOUR_APP_NAME', 
    'filter[field]': 'date',
    'filter[value][from]': '2011-01-01T00:00:00+00:00',
    'filter[value][to]': '2024-12-31T23:59:59+00:00',
    'filter[operator]': 'and',
    'filter[field]': 'country',
    'filter[value]': 'Afghanistan'
}

country = params['filter[value]']
response = requests.get(url, params=params)
data = response.json()





counter = 0
results = {}

for i in range(0, len(data['data'])):
    if ('Pandemic' not in data['data'][i]['fields']['name']):
        results['event' + str(i)] = data['data'][i]['fields']['name']
        counter += 1


if (counter >= 7):
    print("According to the ReliefWeb database for historical natural disaster data, " 
          + country + 
          " is susceptible to natural disasters, due to the increased amount of natural disasters in its history.\n")
else:
    print("According to the ReliefWeb database for historical natural disaster data, " + country + 
          " is NOT susceptible to natural disasters, due to the lack of numerous recent disasters.\n")