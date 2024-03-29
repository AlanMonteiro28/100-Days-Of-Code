import smtplib
import datetime as dt
import pandas as pd
from random import randint

MY_EMAIL = "YOUR GMAIL ACCOUNT"
MY_PASSWORD = "YOUR PASSWORD"

# birthday csv
data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
# date
now = dt.datetime.now()
today = now.day
this_month = now.month

# logic
for person in birthday_dict:
    if person["day"] == today and person["month"] == this_month:
        name = person["name"]
        with open(f"letter_templates/letter_{randint(1,3)}.txt", mode="r") as letter_file:
            message = letter_file.read().replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday!\n\n"
                                    f"{message}")
