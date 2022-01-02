# import smtplib
#
# my_email = "jpascoato@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="")
#
#     connection.sendmail(from_addr=my_email, to_addrs="fzerbinatti@gmail.com",
#                         msg="Subject:Hello\n\n This is the body of my email")

import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month

# Start at zero
day_of_week = now.weekday()

print(now)
print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=1981, month=11, day=10)


print(date_of_birth.weekday())

