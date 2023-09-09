import requests

API_KEY = "616c0c4adeae4dae56393cad2bc90fb4"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
ONE_CALL_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall?"
LAT = 40.645020
LON = 17.516430

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}


response_1 = requests.get(WEATHER_ENDPOINT, params=parameters)
response_1.raise_for_status()
print(response_1.json())


# hourly forecast for the next 24 hours
response_2 = requests.get(ONE_CALL_ENDPOINT, params=parameters)
response_2.raise_for_status()
http_code = response_2.status_code
data = response_2.json()
print(http_code)

