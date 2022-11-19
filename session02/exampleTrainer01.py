import requests
import json
api_key = "XXXXXXXXXXXXXXXXXXXX"
lat = "49.5955"
lon = "17.2518"
url = "http://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
resultado = data["current"]["temp"]
print(resultado)
