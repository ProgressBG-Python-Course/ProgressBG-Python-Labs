# ---------------------------------- Task 1 ---------------------------------- #
### Description:
#  Ask the user for their name, age, and favorite color. Store this information
#  into variables and print a greeting in the console, for example:
#  "Hello, my name is Alice, I am 30 years old, and my favorite color is black."
#  Use f-strings and the variables to construct the message.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# user_color = input("Enter your favorite color: ")
# print(f"Hello, my name is {user_name}, I am {user_age} year old, and my favorite color is {user_color}.")

### Expected output (example):
# Enter your name: Alice
# Enter your age: 30
# Enter your favorite color: black
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.

# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Ask the user for their birth year and the current year.
#  Calculate their age using these inputs, then print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
# user_year = int(input("Enter your birth year: "))
# current_year = int(input("Enter the current year: "))
# user_age = current_year - user_year
# print(f"You are {user_age} years old.")

### Expected output (example):
# Enter your birth year: 1995
# Enter the current year: 2025
# You are 30 years old.

# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Ask the user to enter a large numeric amount (e.g., 1234567.89).
#  Format this number to be displayed as a USD currency with two decimal places and
#  commas for thousands separators. Example: "$1,234,567.89".
#  Use an f-string to format and print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
# user_amount = float(input("Enter an amount:"))

# print(f"${user_amount:,.2f}")  # Форматиране на числото като USD валута с два знака след десетичната точка и запетаи за разделители на хилядите


### Expected output (example):
# Enter an amount: 1234567.89
# $1,234,567.89

# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Ask the user for the names and prices of three different shopping items.
#  Create a simple receipt format. Use f-strings to format each item name
#  aligned to the left and its price aligned to the right.
#  Each line for an item should be 30 characters wide.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
name_item1="milk"
price_item1=1.99
name_item2="bread"
price_item2=2.34
name_item3="eggs"
price_item3=3.59


print()
title = "Shopping Items:" # заглавие на бележката
print(f"{title:^30}") # Центрира името на бележката в поле от 30 символа
# Форматира имената на стоките и цените им в рамките на 30 символа (20 за името и 10 за цената)
print(f"{name_item1:<30} {price_item1:>10.2f}")
print(f"{name_item2:<30} {price_item3:>10.2f}")
print(f"{name_item3:<30} {price_item3:>10.2f}")

### Expected output (example):
# Enter name of item 1: Milk
# Enter price of item 1: 1.99
# Enter name of item 2: Bread
# Enter price of item 2: 2.49
# Enter name of item 3: Eggs
# Enter price of item 3: 3.59
#
#           Shopping Items:
# Milk                          1.99
# Bread                         2.49
# Eggs                          3.59

# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Ask the user for the current temperature in Celsius.
#  Convert this temperature to Fahrenheit using the formula: $F = (C \times 9/5) + 32$.
#  Print both the Celsius and Fahrenheit temperatures, formatted to one decimal place,
#  using an f-string.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
# temperature_celsius = float(input("Enter temperature in Celsius: "))
# temperature_fahrenheit = (temperature_celsius * 9/5) + 32
# # конвертиране на температурата от Целзий в Фаренхайт
# print(f"{temperature_celsius:.1f}°C is equal to {temperature_fahrenheit:.1f}°F")


### Expected output (example):
# Enter temperature in Celsius: 25
# 25.0°C is equal to 77.0°F