import requests
from bs4 import BeautifulSoup
import smtplib
import ssl

my_email = "joshuapellaa@gmail.com"
password = "hemykxrowgfbltyf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}
link = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/" \
       "ref=sr_1_1_sspa?crid=34BP3ERF7LSDC"
response = requests.get(url=link, headers=headers)
content = response.text
soup = BeautifulSoup(content, "lxml")
price = soup.find(name="span", class_="a-offscreen").get_text().split("$")[1]
if float(price) < 100:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="coolpellajosh@gmail.com",
                            msg=f"Subject: Instant pot now below $100!!!\n\n{link}")
