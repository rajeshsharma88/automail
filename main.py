import smtplib
import datetime as dt
import random

MY_EMAIL = "rcssharma70@gmail.com"
MY_PASSWORD = "Rajesh@123"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}")





# my_email = "rcssharma70@gmail.com"
# password = "Rajesh@123"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="imrajesh88@yahoo.com",
#                         msg="Subject:Hello\n\n This is a test email for this account")



