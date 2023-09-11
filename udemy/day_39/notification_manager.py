from twilio.rest import Client
import os


class NotificationManager:

    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

    NUMBER_FROM = os.environ.get("NUMBER_FROM")
    NUMBER_TO = os.environ.get("NUMBER_TO")

    def __init__(self,
                 price,
                 departure_city,
                 departure_iata,
                 arrival_city,
                 arrival_iata,
                 outbound_date,
                 inbound_date):
        self.price = price
        self.departure_city = departure_city,
        self.departure_iata = departure_iata,
        self.arrival_city = arrival_city,
        self.arrival_iata = arrival_iata,
        self.outbound_date = outbound_date,
        self.inbound_date = inbound_date

    def send_sms(self):
        twilio_client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

        string_message = (f"Sent from your Twilio trial account - Low Price Alert!\n"
                          f"Only £{self.price} to fly from {self.departure_city}-{self.departure_iata} "
                          f"to {self.arrival_city}-{self.arrival_iata}, from {self.inbound_date} to "
                          f"{self.outbound_date}.")
        
        sms = twilio_client.messages.create(
            body=string_message,
            from_=self.NUMBER_FROM,
            to=self.NUMBER_TO)

        print("Message Sent. SID: " + sms.sid)
