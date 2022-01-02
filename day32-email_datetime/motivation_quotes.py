import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "jpascoato@gmail.com"
MY_PASSWORD = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:

    with open("quotes.txt", "r") as data:
        quotes = data.readlines()

    random_quote = choice(quotes).strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jpascoato@gmail.com",
            msg=f"Subject:Monday Motivation\n\n {random_quote}")
