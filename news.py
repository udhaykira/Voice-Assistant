import requests
from template import *

api_address = "http://newsapi.org/v2/top-headlines?country=us&apikey="+key
json_data = requests.get(api_address).json()

def news():
    news_list = []  # Renamed to avoid conflict with the built-in list type
    for i in range(3):
        news_list.append("Number "+ str(i+1 )+": " + json_data["articles"][i]["title"]+".")
    return news_list


