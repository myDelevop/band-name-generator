import requests
from pprint import pprint
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETY_BEARER_TKN = os.environ.get("SHEETY_BEARER_TOKEN_2")
        self.SHEETY_ENDPOINT = "https://api.sheety.co/550056cfdf9916e403de58f74910dc55/flightDeals/prices"
        self.last_json_get = {}

        self.request_header = {
            "Authorization":  self.SHEETY_BEARER_TKN
        }

    def read_spreadsheet(self):
        response = requests.get(url=self.SHEETY_ENDPOINT,
                                headers=self.request_header)
        response.raise_for_status()
        self.last_json_get = response.json()
        return response.json()["prices"]

    def update_iata_code(self, city_id, iata_code):
        params = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.SHEETY_ENDPOINT}/{city_id}",
                                json=params,
                                headers=self.request_header)
        response.raise_for_status()

    def print_last_call(self):
        pprint(self.last_json_get["prices"])
