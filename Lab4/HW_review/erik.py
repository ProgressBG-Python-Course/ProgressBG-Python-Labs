
# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here

# number = float(input("Enter a number: "))

# if number==0:
#     print("Zero")
# elif number>0:
#     print("Positive")
# else:
#     print("Negative")


### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here

# year = int(input("Enter a year: "))

# if year%4==0:
#     print(f"{year} is a leap year")
#     if year%400==0:
#         print(f"{year} is a leap year")
#     elif year%100==0:
#         print(f"{year} is not a leap year")
# else:
#     print(f"{year} is not a leap year")

### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here

# header = "Fahrenheit/Celsius Converter"
# option_1 = "1 => Convert to Fahrenheit"
# option_2 = "2 => Convert to Celsius"

# print("")
# print(f"{11*'*'}{header:^31}{11*'*'}")
# print(f"# {option_1:<50}"'#')
# print(f"# {option_2:<50}"'#')
# print(f"{"*" * 53}")
# print("")

# user_choice = int(input("Enter your choice [1/2]: "))

# if user_choice == 1:
#     temperature_entered_in_celsius = float(input("Enter temperature in C:"))
#     temperature_converted_to_fahrenheit = temperature_entered_in_celsius * (9/5) + 32
#     print(f"{temperature_entered_in_celsius}C = {temperature_converted_to_fahrenheit}F")
# elif user_choice == 2:
#     temperature_entered_in_fahrenheit = float(input("Enter temperature in F:"))
#     temperature_converted_to_celsius = (temperature_entered_in_fahrenheit - 32 ) * 5/9
#     print(f"{temperature_entered_in_fahrenheit}F = {temperature_converted_to_celsius}C")
# else:
#     print("You have to choose between 1 or 2")


### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Underweight (Severe thinness)   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

### Your code here

user_height_in_meters = float(input("Enter your height in meters: "))
user_weight_in_kilograms = float(input("Enter your weight in kilograms: "))
category = (
    " Underweight (Severe thinness)",
    "Underweight (Moderate thinness)",
    "Underweight (Mild thinness)",
    "Normal range",
    "Overweight (Pre-obese)",
    "Obese (Class I)",
    "Obese (Class II)",
    "Obese (Class III)"
)

bmi = user_weight_in_kilograms / (user_height_in_meters * user_height_in_meters)

if bmi <=16.0:
    print(f"Your BMI = {bmi:.2f}, Category: {category[0]}")
elif bmi >=16.0 and bmi<17:
    print(f"Your BMI = {bmi:.2f}, Category: {category[1]}")
elif bmi >=17.0 and bmi<18.5:
    print(f"Your BMI = {bmi:.2f}, Category: {category[2]}")
elif bmi >=18.5 and bmi<24.9:
    print(f"Your BMI = {bmi:.2f}, Category: {category[3]}")
elif bmi >=25.0 and bmi<30:
    print(f"Your BMI = {bmi:.2f}, Category: {category[4]}")
elif bmi >=30.0 and bmi<35:
    print(f"Your BMI = {bmi:.2f}, Category: {category[5]}")
elif bmi >=35.0 and bmi<40:
    print(f"Your BMI = {bmi:.2f}, Category: {category[6]}")
else:
    print(f"Your BMI = {bmi:.2f}, Category: {category[7]}")

### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)