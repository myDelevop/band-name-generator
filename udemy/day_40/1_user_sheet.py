import requests
import os
import re

SHEETY_ENDPOINT = "https://api.sheety.co/550056cfdf9916e403de58f74910dc55/flightDeals/users"
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN_2")


print("Welcome to Rocco's Fights Club.")
print("We find the best flights deals and mail you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email = ""
valid_email = False

while valid_email is not True:
    email_tmp = input("What is your email?\n")
    email = input("Type your email again?\n")

    if email_tmp == email and re.fullmatch(regex, email):
        valid_email = True

header = {
    "Authorization": SHEETY_BEARER_TOKEN,
    "Content-Type": "application/json"
}

params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

response = requests.post(url=SHEETY_ENDPOINT, headers=header, json=params)
response.raise_for_status()

if response.status_code == 200:
    print("You're in the club!")
print(response.json())
