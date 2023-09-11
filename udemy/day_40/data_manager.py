import os
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/550056cfdf9916e403de58f74910dc55/flightDeals/prices"
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN_2")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": SHEETY_BEARER_TOKEN,
            "Content-Type": "application/json"
        }

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
