import smtplib
import os

my_email = "rockdesires@gmail.com"
to_address = "rocco.caliandro@toptal.com"
password = os.environ.get("EMAIL_PROVIDER_TOKEN")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs=to_address,
                        msg="Subject:Hello from Python\n\nThis is the body of my email")
