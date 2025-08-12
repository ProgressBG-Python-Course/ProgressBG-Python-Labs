def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= n

    return result


print(factorial(5))
