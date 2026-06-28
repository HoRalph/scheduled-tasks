import smtplib
import datetime as dt
import random
import csv
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

birthdays = []
with open("birthdays.csv", "r") as file:
    data = csv.DictReader(file)
    for line in data:
        birthdays.append(line)


now = dt.datetime.now()
letter_templates = os.listdir("./letter_templates")


for birthday in birthdays:
    if int(birthday["month"]) == now.month and int(birthday["day"]) == now.day:
        letter = random.choice(letter_templates)
        letter_lines = []
        letter_string =""
        with open(f"./letter_templates/{letter}") as letter_template:
            for line in letter_template:
                line = line.replace("[NAME]", birthday["name"])
                letter_string += line
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=birthday["email"], msg=f"Subject: Happy Birthday {birthday["name"]}! \n\n {letter_string}")