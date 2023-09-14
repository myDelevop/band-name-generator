import requests
import os
import smtplib
from bs4 import BeautifulSoup

EMAIL_PROVIDER_TOKEN = os.environ.get("EMAIL_PROVIDER_TOKEN")
EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
AMAZON_PRODUCT_URL = "https://www.amazon.com/Cuisinart-DGB-2-Conical-Single-Serve-Coffeemaker/dp/B09HDFLF2X/ref=sr_1_2_sspa?crid=3HOHQSI2TW8KO&keywords=coffee%2Bmaker&qid=1694696773&sprefix=coff%2Caps%2C215&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
HISTORICAL_MIN = 99.99
# TARGET_PRICE = 108.99
# TARGET_PRICE = 120

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=AMAZON_PRODUCT_URL, headers=headers)


soup = BeautifulSoup(response.content, 'lxml')

product_title = soup.select_one(selector="#productTitle").text.strip()

price = soup.find(class_="a-offscreen")
price = price.text.strip()
price_without_currency = float(price[1:])

print(f"The cost of the price is: ${price_without_currency}, the historical min is: ${HISTORICAL_MIN} "
      f"and your minimum target is ${TARGET_PRICE}")

if price_without_currency < TARGET_PRICE:
    message = (f"Subject:Amazon Price Alert!\n\n"
               f"{product_title} is now on Amazon at ${price_without_currency}\n\n"
               f"Your min target is ${TARGET_PRICE} and the historical min price is ${HISTORICAL_MIN}\n\n"
               f"Buy now here => {AMAZON_PRODUCT_URL}").encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_FROM, password=EMAIL_PROVIDER_TOKEN)

        connection.sendmail(from_addr=EMAIL_FROM,
                            to_addrs=EMAIL_TO,
                            msg=message)
else:
    print("\nProduct still too expensive!")