# import time

# now = time.time()
# print("number of seconds since the Unix epoch: ", now)


# start = time.time()
# for i in range(1_000_000):
#     i**2

# end = time.time()
# print(f"Time taken: {end - start} ")


# from datetime import datetime
# import datetime

# current_datetime = datetime.datetime.now()
# print(f"Current Date and Time: {current_datetime}")

# # OUTPUT:
# # Current Date and Time: 2023-10-17 11:54:04.585473

# from datetime import datetime

# now = datetime.now()

# print(now.year)
# print(now.month)


# now = datetime.now()
# print(now)
# print(now.strftime("%d.%m.%y, %H:%M"))  # 24.03.25


# birth_date = input("Enter birht date: ")
# birth_date = "01.02.1990"
# birth_date_obj = datetime.strptime(birth_date, "%d.%m.%Y")

# now = datetime.now()
# print(now.year - birth_date_obj.year)


# from datetime import timedelta

# what day name will be 10 days after now
# now = datetime.now()
# delta_10_days = timedelta(days=10)
# print((now + delta_10_days).day)


# ------------------------------- zoneinfo demo ------------------------------ #
# from datetime import datetime
# from zoneinfo import ZoneInfo


# # current_paris = datetime.now(ZoneInfo("Europe/Paris"))
# # print(current_paris)

# # now = datetime.now()
# # print(now)  # show time in Paris

# ### Convert
# # Create a timezone-aware datetime object
# sofia_now = datetime.now(ZoneInfo("Europe/Sofia"))

# # Convert to another Time
# kolkata_now = sofia_now.astimezone(ZoneInfo("Asia/Kolkata"))

# print("Current datetime in Sofia", sofia_now.strftime("%d.%m.%Y, %H:%M"))
# print("Current datetime in Kolkata", kolkata_now.strftime("%d.%m.%Y, %H:%M"))

# # Current datetime in Sofia 11.02.2024, 22:28
# # Current datetime in Kolkata 12.02.2024, 01:58


# ---------------------------------- Example --------------------------------- #
from datetime import datetime
from zoneinfo import ZoneInfo

def get_weekday_name(date, lang):
    """Returns the name of the day of the week for a given date in a specified language.

    :param date: A datetime object.
    :param lang: A string indicating the language ('bg' for Bulgarian, 'en' for English).
    :return: A string representing the name of the weekday.
    """
    weekday_names_mapping = {
        'bg': ["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
        'en': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    }

    weekday_name = weekday_names_mapping[lang][date.weekday()]
    return weekday_name

# Now using timezone-aware datetime
now = datetime.now(ZoneInfo("Europe/Sofia"))

print('Днес е', get_weekday_name(now, "bg"))
print('Today is', get_weekday_name(now, "en"))

# Днес е сряда
# Today is Wednesday
