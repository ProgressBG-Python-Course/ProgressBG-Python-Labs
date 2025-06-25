# 2+3+2.0
# x=4
# x=5

# RAM:
# ...
#     0x123:000000010 (2)
#     0x432:000000011 (3)
#     0x632:0000000110101010100 (2.0)
#      :0x822:000000111 (4)
#     x:0x812:000000011 (5)
# # ---------------------------------- Numbers --------------------------------- #
# print( 4 )
# print( +4 )
# print( --4 )

# print( .2 )
# print( 0.2 )

# print( 3_459_987_654 )



# --------------------------- Arithmetic Operations -------------------------- #
# print(7%3) #1
# print(7%4) #3
# print(7//4) #3
# print(7/4) #3


# print(0.1+0.2)


# -------------------------------- Math Module ------------------------------- #
# import math
# # Example: Calculate square root of a number
# number = 16
# sqrt_value = math.sqrt(number)
# print(sqrt_value)

# ---------------------------- Built in functions ---------------------------- #
# numbers = [1,5,3,2]
# max_number = max(numbers)
# print(max_number)



# ---------------------------------- Strings --------------------------------- #
# print('abc')
# print("abc")

# print("""Strings are immutable sequences of Unicode code points (will be discussed further).
# Single-line strings literal should be closed in single or double quotes
# No difference between single or double quoted strings!
# Multi-line strings literal should be closed in triple single or double quotes""")

# print('Tom's pub') # TODO: fix

# ----------------------------- String operations ---------------------------- #
# print( 2+2 ) #4
# print( '2'+'2' ) #'22'
# print( '2'+2 ) # Error


# print( 10*'~')

# ------------------------------ String Methods ------------------------------ #
# user_name = "Ada"
# print( user_name.count('a')) #1
# if user_name.find('i')==-1:
#     print('No i')


# --------------------------------- Variables -------------------------------- #
# x=4
# user_name = "Ada"


# RAM:
#     x:0x321: 010101010 (4)
#     user_name:0x121: 001010101010101010 ("Ada")

# ...
# user_first_name = "Ada"
# user_sur_name = "Byron"

# print( user_first_name + " " +user_sur_name + "!")

# ...
# count = 1

# # count=count+1
# count += 1

# print(count)


# RAM:
#  count: 2 

# a = 5
# print( id(a))

# a = 6
# print( id(a))


# ----------------------------- Escape Sequences ----------------------------- #
print("a/b")
print("a\b")
print("a\tb")
print("a    b")
print("a\\b")


print('Tom\'s pub')
print('Line1\nLine2' )