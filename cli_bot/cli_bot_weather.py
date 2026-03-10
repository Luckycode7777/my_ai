import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()

user_input = input("Введите город, что бы узнать температуру воздуха: ")

API_KEY = os.getenv("API_KEY")


url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={user_input}'

response = requests.post(url)

if response.status_code == 200:
    date = response.json()
    dat = json.dumps(date)
    print(f"Bot: температура по цельсию: {date['location']['country']}")
    print(f"---: температура по цельсию: {date['current']['temp_c']}")
    print(f"---: температура по фаренгейту: {date['current']['temp_f']}")
else:
    print(f'Error:{response.status_code}')
