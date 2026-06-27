import os
import smtplib
import datetime as dt
import random
my_email = "rho416341@gmail.com"
password = "tqnqrmxmjesqgvpw"
'''
connection = smtplib.SMTP("smtp.gmail.com", port = 587)
connection.starttls()
connection.login(user= my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="ralph.ho94@gmail.com",msg = "Hello")
connection.close()
'''

with open("quotes.txt") as file:
    all_quotes = file.readlines()


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 0:
    selected_quote = random.choice(all_quotes)
    print(selected_quote)
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ralph.ho94@gmail.com",msg = f"subject: Quote of the day \n\n {selected_quote}")

