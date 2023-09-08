import random
import pandas
import smtplib
import datetime as dt

now = dt.datetime.now()
week = now.weekday()
week_day = now.strftime('%A')

data_dict = [{
    "author": "XXX",
    "quote": "CC"
}]

if week == 0:
    data_frame = pandas.read_csv("quotes.txt")
    data_dict = data_frame.to_dict(orient="split")["data"]

    data_dict = [string[0] for string in data_dict]
    data_dict = [{"author": string.replace("'", "").split("-")[1].strip(),
                  "quote": string.replace("'", "").split("-")[0].strip()}
                 for string in data_dict]

    random_quote = random.choice(data_dict)
    print(random_quote)

    my_email = "rockdesires@gmail.com"
    to_address = "rock_y@libero.it"
    password = "rwzuaeheaajizvma"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address,
                            msg=f"Subject:{week_day}'s quote\n\n"
                                f"A quote from: {random_quote['author']}\n"
                                f"{random_quote['quote']}")
