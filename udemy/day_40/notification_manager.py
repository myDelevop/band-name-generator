from data_manager import DataManager
import os
import smtplib
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

TWILIO_VIRTUAL_NUMBER = os.environ.get("NUMBER_FROM")
TWILIO_VERIFIED_NUMBER = os.environ.get("NUMBER_TO")

EMAIL_PROVIDER_TOKEN = os.environ.get("EMAIL_PROVIDER_TOKEN")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.my_email = "rockdesires@gmail.com"

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message):
        # message.replace("£", "&#36;")
        # message.replace("£", "&#x24;")
        # message.replace("£", "&dollar;")
        data_manager = DataManager()
        sheet_data = data_manager.get_generic_data("users")

        message = (f"Subject:New Low Price Flight! Look at this Occasion "
                   f"for a flight\n\n{message}").encode("utf-8")

        for obj in sheet_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=EMAIL_PROVIDER_TOKEN)

                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=obj["email"],
                                    msg=message)
