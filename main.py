import requests, smtplib, re
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

example = os.getenv('TOKEN')

URL = "https://appbrewery.github.io/instant_pot/"
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
EMAIL_TO_ADDRESS=os.getenv("EMAIL_TO_ADDRESS")

data = requests.get(url=URL)
soup = BeautifulSoup(data.text, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")
price_string = price_whole.getText() + price_fraction.getText()
price = float(price_string)
print(price)

product_name = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()
new_product_name = re.sub(" {20}", " ", product_name)
new_product_name = re.sub("\r\n", " ", new_product_name)
new_product_name = re.sub(" {3}", " ", new_product_name)
new_product_name = new_product_name.strip()
new_product_name = new_product_name.replace("é", "e")
print(new_product_name)

if price < 100:
    with smtplib.SMTP(f"{SMTP_ADDRESS}", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs=EMAIL_TO_ADDRESS,
                            msg=f"Subject:Amazon Price Alert!\n\n{new_product_name} is now ${price}.\n{URL}")
