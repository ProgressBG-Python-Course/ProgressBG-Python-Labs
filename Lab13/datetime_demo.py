# print("Current time:", time.time())


# current_datetime = datetime.now()
# print(f"Current Date and Time: {current_datetime}")

# print(f"Year: {current_datetime.year}")
# print(f"Month: {current_datetime.month}")
# print(f"Day: {current_datetime.day}")


# user_birthday_string = input("Enter your birthday (DD.MM.YYYY): ")  # e.g., 17.10.1999

# # user_birthday = datetime(year=1999, month=10, day=17, hour=12, minute=30, second=45)
# user_birthday = datetime.strptime(user_birthday_string, "%d.%m.%Y")
# print(f"user birth year: {user_birthday.year}")


# from datetime import datetime

# current_date = datetime.now().date()


# one_week_ahead = current_date + timedelta(weeks=1)
# hundred_days_before = current_date - timedelta(days=100)

# print("One week from today:", one_week_ahead)
# print("100 days before today:", hundred_days_before)

# OUTPUT:
# One week from today: 2023-10-24
# 100 days before today: 2023-07-09


# -------------------------- Working with timezones -------------------------- #
from datetime import datetime
from zoneinfo import ZoneInfo

user_birthday_string = "17.10.1999"
user_birthday = datetime.strptime(user_birthday_string, "%d.%m.%Y")

print(
    f"User's birthday in Kolkata: {user_birthday.astimezone(ZoneInfo('Asia/Kolkata'))}"
)
print(f"User's birthday in Paris: {user_birthday.astimezone(ZoneInfo('Europe/Paris'))}")
