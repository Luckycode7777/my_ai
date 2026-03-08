from pprint import pprint

import requests
import os

API_KEY = "1cb416b712284c09a50183350260703"
location = "Los-Angeles"

url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}'

response = requests.post(url)

if response.status_code == 200:
    date = response.json()
    pprint(date)
else:
    print(f'Error:{response.status_code}')

