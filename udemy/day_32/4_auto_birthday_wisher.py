import random
import smtplib
import datetime as dt

MY_EMAIL = "rockdesires@gmail.com"
MY_PSW = "rwzuaeheaajizvma"

now = dt.datetime.now()
month = int(now.month)
day = int(now.day)

today_birthdays = []

with open("birthdays.csv") as birthdays_file:
    data = birthdays_file.readlines()
    for line in data:
        line = line.strip()
        if not (line.startswith("name") or line == ""):
            file_month = int(line.split(',')[3])
            file_day = int(line.split(',')[4])

            if file_month == month and file_day == day:
                today_birthdays.append({
                    "name": line.split(',')[0],
                    "email": line.split(',')[1]
                })


for birthday in today_birthdays:
    random_num = random.randint(1, 3)

    with open(file="letter_templates/letter_" + str(random_num) + ".txt") as template:
        text = template.read().replace("[NAME]", birthday["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PSW)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday["email"],
                            msg="Subject:Happy Birthday!\n\n" + text)
