class FlightData:

    def __init__(self,
                 flight_id,
                 dest_airport_code,
                 dest_airport_city,
                 flight_price,
                 flight_currency,
                 local_departure,
                 local_arrival,
                 duration_min,
                 # company,
                 dep_airport_code="LON",
                 dep_airport_city="London"):
        self.dep_airport_code = dep_airport_code
        self.dep_airport_city = dep_airport_city
        self.destination_airport_code = dest_airport_code
        self.destination_airport_city = dest_airport_city
        self.flight_price = flight_price
        self.flight_currency = flight_currency
        self.local_departure = local_departure
        self.local_arrival = local_arrival
        self.duration_min = duration_min
        # self.company = company


