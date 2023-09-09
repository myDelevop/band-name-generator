import requests
from datetime import datetime

LATITUDE = 40.645020
LONGITUDE = 17.516430

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)

print(time_now.hour)
