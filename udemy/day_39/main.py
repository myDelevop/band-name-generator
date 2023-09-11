from notification_manager import NotificationManager
from flight_search import FlightSearch
import data_manager


dm = data_manager.DataManager()
sheet_data = dm.read_spreadsheet()
dm.print_last_call()
flight_search = FlightSearch()

index = 0
for row in sheet_data:
    if row["iataCode"] == '':
        iata_code = flight_search.get_destination_code(row["city"])
        sheet_data[index]["iataCode"] = iata_code
        dm.update_iata_code(row["id"], iata_code)
        index += 1

output_data = {
    "city": "",
    "flight_data": ""
}


for row in sheet_data:
    cheapest_flight = flight_search.search_cheapest_direct_flight("LON", row["iataCode"])
    if cheapest_flight.flight_price < row["lowestPrice"]:
        notification_manager = NotificationManager(
            price=cheapest_flight.flight_price,
            departure_city=cheapest_flight.dep_airport_city,
            departure_iata=cheapest_flight.dep_airport_code,
            arrival_city=cheapest_flight.destination_airport_city,
            arrival_iata=cheapest_flight.destination_airport_code,
            outbound_date=cheapest_flight.local_arrival,
            inbound_date=cheapest_flight.local_departure)
        notification_manager.send_sms()

