import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

URL = "https://www.amazon.in/gp/product/B0DBHVFW5L/ref=ox_sc_saved_title_4?smid="
http_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
}
response = requests.get(URL, headers=http_headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
product_name = " ".join(
    soup.find(
        name="span", class_="a-size-large product-title-word-break", id="productTitle"
    )
    .getText()
    .split()
)

if price < 30000.00:
    with smtplib.SMTP("smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Alert: Amazon Price Tracker\n\n{product_name}\nis now ${price}.\n\n{URL}",
        )
