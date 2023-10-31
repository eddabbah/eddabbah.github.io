import requests
from ast import literal_eval
import json
url="https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&hourly=temperature_2m&start_date=2023-10-30&end_date=2023-11-03"
response=requests.get(url).content.decode('utf-8')
mydic=literal_eval(response)
print(mydic["hourly"]["temperature_2m"])
