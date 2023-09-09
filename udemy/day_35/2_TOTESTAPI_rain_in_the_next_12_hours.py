import requests

API_KEY = "616c0c4adeae4dae56393cad2bc90fb4"
ONE_CALL_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
LAT = 40.645020
LON = 17.516430

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(ONE_CALL_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]

# list_codes = []
for i in range(12):
    current_id = int(hourly_data[i]["weather"][0]["id"])
    if current_id < 700:
        print("Take an Umbrella")
        break
