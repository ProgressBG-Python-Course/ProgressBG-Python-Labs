import sys


def my_range(start, end):
    number = start
    while number < end:
        yield number
        number += 1


letters = [code for code in my_range(1, 1_000_0000)]
letters_gen = (code for code in my_range(1, 1_000_0000))

print(f"Size of my_range: {sys.getsizeof(my_range)} bytes")
print(f"Size of letters list: {sys.getsizeof(letters)} bytes")
print(f"Size of letters generator: {sys.getsizeof(letters_gen)} bytes")

# for letter in letters:
#     print(letter, end=",")

# print()

# for letter in letters_gen:
#     print(letter, end=",")
