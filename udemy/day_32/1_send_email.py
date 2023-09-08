import smtplib

my_email = "rockdesires@gmail.com"
to_address = "rocco.caliandro@toptal.com"
password = "rwzuaeheaajizvma"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs=to_address,
                        msg="Subject:Hello from Python\n\nThis is the body of my email")
