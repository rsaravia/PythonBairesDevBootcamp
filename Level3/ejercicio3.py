# Write a Python program that asks the user for their birth date
# and prints the user’s current age in years, months, and days.
# Sample output: You are 25 years, 4 months, and 22 days old
from dateutil.relativedelta import relativedelta
from datetime import datetime

format_string = "%Y-%m-%d"
date_string = input("Give me your birthday (format: YYYY-MM-DD): ")

birthday_tobj = datetime.strptime(date_string, format_string)

today_tojb = datetime.today()

diff = relativedelta(today_tojb, birthday_tobj)

year_data = diff.years
month_data = diff.months
day_data = diff.days
print(f"You are {year_data} years, {month_data} months, and {day_data} days old")


