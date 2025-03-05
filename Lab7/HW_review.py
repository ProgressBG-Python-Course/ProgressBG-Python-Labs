# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of ststars in the first line is 1,
      in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here
# n = int(input('Enter stars number : '))

# for stars in range(1,n+1): # [1,2,3]
#     print('*'*stars)


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


# while True:
#     user_input = input("Enter a word (or '0' to stop): ")
#     if user_input=='0':
#         break


# if user_input != 0:
#     print(input("Enter a word (or '0' to stop): "))
# else:
#      print('Words that starts with a vowel : ')



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

# ## Given:
# words = ["hello", "world", "python", "is", "fun", "and", "useful"]
# index=0
# print(words[0])
# print(len(words[0]))

# index = 0
# words_dictionary = {}
# for w in set(words):
#     for l in w:
#      print(l,w.count(l))
    # k = len(w)
    # # v = [len(w)] gluposti
    # words_dictionary=k,v
    # print(words_dictionary)

## Your code here



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

# ### Given
# refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
# sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

### Your code here


# refrigerated_sale_categories = refrigerated.intersection(sale)
# print('Categories both refrigerated and on sale: ',refrigerated_sale_categories)
# sale_no_refrigerated_categories = sale.difference(refrigerated)
# print('Sale categories not needing refrigeration: ',sale_no_refrigerated_categories)
# new_sale_categories = refrigerated .difference(sale)
# print('Suggested new sale categories from refrigerated items: ',new_sale_categories)

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}