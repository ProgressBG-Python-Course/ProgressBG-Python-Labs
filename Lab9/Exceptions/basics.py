# # not an exception, parse error
# # print("hi)

# # error, but it is run time => exception
# print(x)


# ------------------------- Basic Exception HAndling ------------------------- #
# try:
#     # Code that might raise an exception
#     x = 0
#     print(10 / x)
# except ZeroDivisionError:
#     # Code to handle the specific exception
#     print("I can not divide by 0")
# else:
#     print("Else: Division is successfull!")

# print("END")


# ----------------------------- Exception Classes ---------------------------- #
# try:
#     number = int(input("Enter a number: "))

#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except Exception as e:
#     # This block will execute if any other unexpected error occurs
#     print(f"Ups, something went wrong: {e}")


# ------------------------ Rainsing custom exceptions ------------------------ #
class InvalidAge(Exception):
    pass


while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise InvalidAge("Age must be between 1 and 99")
        break
    except ValueError:
        print("Invalid number")
    except InvalidAge:
        print("The age is invalied")

while True:
    try:
        number = int(input("Enter a number: "))
        print(age / number)
        break
    except ValueError:
        print("Invalid number")
    except ZeroDivisionError:
        print("Can not divide by zero")


print(f"Your age is: {age}")
print("End")
