# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here

# triangle_len = int(input("Enter start number: "))
# counter = 0
# print_symbol = 1

# while counter != triangle_len:
#     print("*" * print_symbol)
#     print_symbol += 1
#     counter +=1


# for counter in range(1,triangle_len+1 ):
#      print("*" * counter)


### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code
# words_list = []
# words_that_start_with_a_vowel =[]

### Get words from user
# while True:
#     user_input = input("Enter a word (or '0' to stop): ")
#     if user_input == "0":
#         break
#     words_list.append(user_input)

words = ["word", "One", "two", "apple"]

### Filter words
# for x in words:
#     if x[0] in "aeiou":
#         words_that_start_with_a_vowel.append(x)

# words_that_start_with_a_vowel =[word for word in words if word[0].lower() in "aeiou"]
# print(f"Words that start with a vowel: {words_that_start_with_a_vowel}")

### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
# words = ["hello", "world", "python", "is", "fun", "and", "useful"]
# length_dict = {}

### Your code here

### Variant 1
# for word in words:
#     word_lenght = len(word)

#     if word_lenght not in length_dict:
#         length_dict[word_lenght] = [word]

#     length_dict[word_lenght].append(word)


# ### Variant 2:
# from collections import defaultdict

# words = ["hello", "world", "python", "is", "fun", "and", "useful"]
# length_dict = defaultdict(list)

# for word in words:
#     word_lenght = len(word)

#     length_dict[word_lenght].append(word)

# print(dict(length_dict))




### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    In a supermarket inventory system, there are two sets of product categories:
    1. Categories that need refrigeration.
    2. Categories on sale this week.

    Write a script, which performs the following tasks:
    a. Find and print the categories that are both refrigerated and on sale.
    b. Find and print categories that are on sale but do not require refrigeration.
    c. Suggest new sale categories from the refrigerated items which are not yet on sale.

    Note: The category names are assumed to be in lowercase.
"""

### Given
refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

### Your code here

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}