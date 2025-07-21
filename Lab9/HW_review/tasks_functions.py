# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""


### YOUR CODE HERE


### TEST:
# print(calculate_area(10, 5))

### EXPECTED OUTPUT:
# 50


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""


### TODO: discuss shorter

# def is_even(number):
#     return number%2 == 0

### TEST:
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT
# True
# False


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'multiply_elements' that takes a list of integers and returns the product of all the elements in the list.
"""


### TODO: discuss bug
# def multiply_elements(a,b,c):
#     return a * b * c

# print(multiply_elements(a = 2,b = 3, c = 4))


### TODO: discuss shorthand syntax
# def multiply_elements(numbers):
#     """Multiply all elements in a list"""
#     result = 1
#     for number in numbers:
#         result *=  number
#     return result


## TEST:
# print(multiply_elements([2, 3, 4]))

### EXPECTED OUTPUT:
# 24


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### TODO: discuss generators?
# vowels = ("aeiou")
# def count_vowels(word):
#     return sum(1 for char in word if char in vowels)

# return sum(1 for char in s.lower() if char in 'aeiou')


### TODO: count_v = count_v + 1
### YOUR CODE HERE
# def count_vowels(my_str):
#     count_v = 0
#     vowels = 'aeiou'
#     for el in my_str:
#         if el in vowels:
#             count_v +=  1

#     return count_v


### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'reverse_string' that takes a string and returns the string reversed.
"""

# ### TODO: make it lambda
# def reverse_string(s):
#     """Reverses a string"""
#     return s[::-1]


# reverse_string = lambda s: s[::-1]
### TEST:
# print(reverse_string("hello"))

### EXPECTED OUTPUT:
# "olleh"


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a function 'find_max' that takes a list of numbers and returns the largest number in the list.
"""


### TODO: discuss manual solution for algotithmic skills
def find_max(lst_number):
    # [1, 3, 2, 8, 5]
#     max_number = lst_number[0]
#     for el in lst_number[1:]:
#         print(el)
#         if el>max_number:
#             max_number = el
#     return max_number

# def find_max(*args):
#     index=-math.inf
#     for number in args:
#         if number>index:
#             max=number
#             index=number
#         else:max=index

#     return max


### TEST:
# print(find_max([1, 3, 2, 8, 5]))

### EXPECTED OUTPUT:
# 8


# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""


### TODO: discuss other solution

# def remove_duplicates(items):
#     """Removes duplicates from a list, preserving order"""
#     return list(dict.fromkeys(items))


# items=[1,2,3,2,2]
# # d = dict.fromkeys(items)
# # print(list(d.keys()))
# print( list(set(items)))

### TEST:
# print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]


# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""

### TODO: discuss the bug
is_palindrome = lambda x: True if x[0] == x[::-1][0] else False


### TODO: make it lambda
# def is_palindrome(my_str):
#     reverse_string = lambda my_str: my_str[::-1] # обръща стринга
#     if my_str == reverse_string(my_str): # сравнява оригиналния стринг с обърнатия стринг
#         answers = True # ако е палиндром
#     else:
#         answers = False # ако не е палиндром
#     return answers


# def is_palindrome(word):
#     """Check if a word is palindrome"""
#     return word == word[::-1]

### TEST:
# print(is_palindrome("mdam"))
# print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False


# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### YOUR CODE HERE

### TEST:
# print(add(2, 3))

### EXPECTED OUTPUT:
# 5


# ---------------------------------- Task 10 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""


## TODO: discuss shorter solution

# def filter_words(words, minimum_lenght):
#     filtered_words = []
#     for x in words:
#         if len(x) > minimum_lenght:
#            filtered_words.append(x)
#     return filtered_words

### TEST:
# print(filter_words(["apple", "pear", "banana", "cherry"], 5))

### EXPECTED OUTPUT:
# ['banana', 'cherry']


# ---------------------------------- Task 11 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### TODO: discuss why create new key var
sort_by_last_letter = lambda x: x[-1]

### TEST:
print(sorted(["cherry", "banana", "apple"], key=lambda x: x[-1]))


# def sort_by_last_char(words):
#     """Sorts words by their last character"""
#     return sorted(words, key=lambda word: word[-1])

### EXPECTED OUTPUT:
# ['banana', 'apple', 'cherry']