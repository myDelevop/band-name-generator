import math
from datetime import datetime, timedelta
from flight_data import FlightData
import requests
import os


class FlightSearch:

    def __init__(self):
        self.FLIGHT_SEARCH_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.FLIGHT_SEARCH_FLIGHTS_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.FLIGHT_SEARCH_API_KEY = os.environ.get("FLIGHT_SEARCH_API_KEY")
        self.header_params = {
            "accept": "application/json",
            "apikey": self.FLIGHT_SEARCH_API_KEY
        }

    def get_destination_code(self, city):

        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=self.FLIGHT_SEARCH_LOCATION_ENDPOINT,
                                params=params,
                                headers=self.header_params)
        response.raise_for_status()
        response_json = response.json()
        return response_json["locations"]["name" == city]["code"]

    def search_cheapest_direct_flight(self, iata_departure, iata_destination):
        tomorrow = (datetime.now() + timedelta(1))
        six_months = tomorrow + timedelta(6 * 30)

        date_from = tomorrow.strftime("%d/%m/%Y")
        date_to = six_months.strftime("%d/%m/%Y")

        params = {
            "fly_from": iata_departure,
            "fly_to": iata_destination,
            "date_from": date_from,
            "date_to": date_to,
            "max_stopovers": "0",  # direct flights,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1
        }
        response = requests.get(url=self.FLIGHT_SEARCH_FLIGHTS_ENDPOINT,
                                params=params,
                                headers=self.header_params)
        response.raise_for_status()
        response_json = response.json()["data"]

        min_price = math.inf
        min_id = ""
        min_flight = {}
        for flight in response_json:
            price = flight["conversion"]["GBP"]
            if price < min_price:
                min_price = price
                min_id = flight["id"]
                min_flight = flight

        response = {
            "min_price": min_price,
            "currency": "GBP",
            "min_flight_id": min_id,
            "cheapest_flight": min_flight
        }

        utc_departure = self.convert_date(response["cheapest_flight"]["utc_departure"])
        utc_arrival = self.convert_date(response["cheapest_flight"]["utc_arrival"])

        duration_min = (utc_arrival - utc_departure).min

        flight_data = FlightData(
            flight_id=response["min_flight_id"],
            dest_airport_code=response["cheapest_flight"]["cityCodeTo"],
            dest_airport_city=response["cheapest_flight"]["cityTo"],
            flight_price=response["min_price"],
            flight_currency=response["currency"],
            local_departure=response["cheapest_flight"]["local_departure"],
            local_arrival=response["cheapest_flight"]["local_arrival"],
            duration_min=duration_min,
            dep_airport_code=response["cheapest_flight"]["cityFrom"],
            dep_airport_city=response["cheapest_flight"]["cityCodeFrom"])

        return flight_data

    def convert_date(self, date_time):
        date = date_time.split("T")[0]
        time = date_time.split("T")[1][0:5]
        date_string = date + " " + time

        return datetime.strptime(date_string, "%Y-%m-%d %H:%M")

