import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "itsviv0@proton.me"
MY_PASSWORD = "6:zEuc5B5Upt;'C"

random_num = random.randint(1, 3)
random_letter = f"letter_{random_num}.txt"

now = dt.datetime.now()
month_day = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
birthday_person = birthdays_dict[month_day]

if month_day in birthdays_dict:
    with open(f"./letter_templates/{random_letter}", "r") as file:
        letter_data = file.read()

    letter_data = letter_data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{letter_data}",
        )

else:
    print("No birthdays today.")
