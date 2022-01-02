import smtplib
import datetime as dt
import pandas
from random import randint

MY_EMAIL = "jpascoato@gmail.com"
MY_PASSWORD = ""

data = pandas.read_csv("birthdays.csv")
person_data = pandas.DataFrame.to_dict(data, orient="records")

date = dt.datetime.now()
day = date.day
month = date.month

for person in person_data:
    if person["month"] == month and person["day"] == day:
        random_letter_path = f"letter_{randint(1,3)}.txt"

        with open(f"letter_templates/{random_letter_path}", "r") as data:
            letter = data.read()
            email = letter.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday\n\n {email}")
