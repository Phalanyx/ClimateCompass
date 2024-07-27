import requests

# Define the query parameters
url = "https://api.reliefweb.int/v1/disasters"

# Define the query parameters
params = {
    'appname': 'YOUR_APP_NAME',  # Replace with your application name or domain
    'filter[field]': 'date',
    'filter[value][from]': '2011-01-01T00:00:00+00:00',
    'filter[value][to]': '2024-12-31T23:59:59+00:00',
    'filter[operator]': 'and',
    'filter[field]': 'country',
    'filter[value]': 'Afghanistan'
}

response = requests.get(url, params=params)
data = response.json()

# Print the result



counter = 0
results = {}

for i in range(0, len(data['data'])):
    if ('Pandemic' not in data['data'][i]['fields']['name']):
        results['event' + str(i)] = data['data'][i]['fields']['name']
        counter += 1


print(results)
print('\n')
print(counter)
print('\n')