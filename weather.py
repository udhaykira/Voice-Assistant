import requests
from template import *

api_key = '443f16372d207f42a6a48c42f96b509d'  # Replace 'your_api_key_here' with your actual API key
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid='+api_key
json_data = requests.get(api_address).json()


def temp():
    temperature = round(json_data["main"]["temp"] - 273, 1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description


