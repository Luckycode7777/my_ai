import json
from pprint import pprint

import requests
import os

user_input = input("Введите город, что бы узнать температуру воздуха: ")
# print("Bot:", user_input)

API_KEY = "1cb416b712284c09a50183350260703"
# location = "Los-Angeles"

url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={user_input}'

response = requests.post(url)

if response.status_code == 200:
    date = response.json()
    dat = json.dumps(date)
    print(f"Bot: температура по цельсию: {date['current']['temp_c']}")
    print(f"Bot: температура по фаренгейту: {date['current']['temp_f']}")
else:
    print(f'Error:{response.status_code}')

