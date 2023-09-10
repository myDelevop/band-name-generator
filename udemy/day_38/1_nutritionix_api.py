import requests
from datetime import datetime

NUTRITIONIX_USERNAME = "mawafi3528"
NUTRITIONIX_PASSWORD = "MV9iic!in%A"
NUTRITIONIX_APPLICATION_ID = "d888e201"
NUTRITIONIX_APPLICATION_KEY = "1a9d7a45b664e6719c10b073db79a331"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/550056cfdf9916e403de58f74910dc55/myWorkouts/workouts"

nutritionix_header = {
    "x-app-id": NUTRITIONIX_APPLICATION_ID,
    "x-app-key": NUTRITIONIX_APPLICATION_KEY,
    "x-remote-user-id": "0"
}

query = input("Tell me which exercise you did: ")

nutritionix_parameters = {
    "query": query,
    "gender": "female",
    "weight_kg": "67",
    "height_cm": "167",
    "age": "26"
}

response = requests.post(url=NUTRITIONIX_ENDPOINT,
                         json=nutritionix_parameters,
                         headers=nutritionix_header)
response.raise_for_status()
response_json = response.json()

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")


for exercise in response_json["exercises"]:
    parameters = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["nf_calories"],
            "calories": exercise["duration_min"]
        }
    }
    requests.post(SHEETY_ENDPOINT, json=parameters)
