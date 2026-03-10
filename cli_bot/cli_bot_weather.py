import os

import requests
from dotenv import load_dotenv

load_dotenv()

user_input = input("Введите город, что бы узнать температуру воздуха: ")

API_KEY = os.getenv("API_KEY")

url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={user_input}'

response = requests.post(url)

if response.status_code == 200:
    date = response.json()
    print(f"Город: {date['location']['name']}")
    print(f"Cтрана: {date['location']['country']}")
    print(f"Температура по Цельсию: {date['current']['temp_c']}")
    print(f"Температура по Фаренгейту: {date['current']['temp_f']}")
else:
    print(f'Error:{response.status_code}')
