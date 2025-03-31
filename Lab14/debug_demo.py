import logging

# Configure logging
logging.basicConfig(filename="factorial.log", level=logging.ERROR)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = i

    return result


print(factorial(5))
