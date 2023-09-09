import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 40.645020  # Your latitude
MY_LONG = 17.516430  # Your longitude


def is_position_close_iss(iss_lat, iss_long):
    print("ISS LAT: " + str(iss_lat))
    print("ISS LNG: " + str(iss_long))
    print("MY LAT: " + str(MY_LAT))
    print("MY LNG: " + str(MY_LONG))

    is_close = True
    abs_latitude = abs(MY_LAT - iss_lat)
    abs_longitude = abs(MY_LONG - iss_long)

    print("Latitude Distance: " + str(abs_latitude))
    print("Longitude Distance: " + str(abs_longitude))

    if (abs_latitude < -5 or abs_latitude > 5
            or abs_longitude < -5 or abs_longitude > 5):
        is_close = False

    print("is_close: " + str(is_close))

    return is_close


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    print("Sunrise: " + str(sunrise))
    print("Sunset: " + str(sunset))
    print("Time hour: " + str(time_now.hour))

    iis_close = is_position_close_iss(iss_latitude, iss_longitude)
    is_dark = not(sunrise < time_now.hour < sunset)

    print("ISS close: " + str(iis_close) + "\n is dark: " + str(is_dark))

    if iis_close and is_dark:
        print("Sending email...")
        my_email = "rockdesires@gmail.com"
        to_address = "rocco.caliandro@toptal.com"
        password = "rwzuaeheaajizvma"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(from_addr=my_email,
                                to_addrs=to_address,
                                msg="Subject:ISS Position\n\nHey! Look at the sky"
                                    "you can see the ISS 😀")
        print("... email sent!")

    time.sleep(60)
