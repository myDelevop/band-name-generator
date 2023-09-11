from data_manager import DataManager
import os
from twilio.rest import Client


TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

TWILIO_VIRTUAL_NUMBER = os.environ.get("NUMBER_FROM")
TWILIO_VERIFIED_NUMBER = os.environ.get("NUMBER_TO")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


def send_emails():
    data_manager = DataManager()
    sheet_data = data_manager.get_generic_data("users")
    print(sheet_data)


