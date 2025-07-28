# ----------------------------- Simplest Example ----------------------------- #
# # x = 10
# y = 0

# try:
#     print(x/y)
# except:
#     print("y can not be 0!")


# print("End")


# ------------------------------- Basic Syntax ------------------------------- #
# try:
#     # Code that may raise an exception
# except ExceptionType:
#     # Code to handle the specific exception
# else:
#     # Code that should run only if the try block was successful
# finally:
#     # Always executes, regardless of whether an exception occurred
#     # (useful for cleaning up resources such as closing files or network connections)


# # x = 10
# y = 0

# try:
#     result = x/y
# except ZeroDivisionError:
#     print("y can not be 0!")
#     exit()
# except NameError:
#     print("x is not defined")
#     exit()
# else:
#     print(f"result={result}")
# finally:
#     print("Finally!!!")

# print("End")


# --------------------------------- Example 1 -------------------------------- #
# try:
#     user_number = int(input("Enter a number: "))
# except ValueError as e:
#     print("You did not enter a integer number!")
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Ups, something went wrong: {e}")
# else:
#     print("Your number is ", user_number)
# finally:
#     print("Cleanup...")

# ------------------------- Raising custom exceptions ------------------------ #
# print("Start")
# raise ValueError("wrong value")
# print("End")
class InvalidAge(Exception):
    pass

# def get_user_age():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             if age < 0:
#                 raise InvalidAge("Age must be between 1 and 99")
#             return age
#         except ValueError:
#             print("You did not enter an number!")
#         except InvalidAge:
#             print("Invalid age")


# user_age = get_user_age()

# # Continue with your program using the valid age
# print(f"You are {user_age} years old.")


