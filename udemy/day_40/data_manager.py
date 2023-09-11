import os
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/550056cfdf9916e403de58f74910dc55/flightDeals/"
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN_2")


class DataManager:
    def __init__(self):
        self.generic_data = {}

    def get_generic_data(self, entity):
        header = {
            "Authorization": SHEETY_BEARER_TOKEN,
            "Content-Type": "application/json"
        }

        response = requests.get(url=SHEETY_PRICES_ENDPOINT+entity, headers=header)
        data = response.json()
        self.generic_data = data[entity]
        return self.generic_data

    def update_destination_codes(self):
        for city in self.generic_data:
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
