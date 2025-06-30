# ---------------------------------------------------------------------------- #
#                               Boolean data type                              #
# ---------------------------------------------------------------------------- #
# print(12)
# print("true")
# # print(true)
# print(True)

# RAM:
#     0x123:0010101010(12)
#     0x143:01010111100000("true")
#     0x173:0000000000001 (True)


# print(True)
# print(type(True))
# print(type(False))

# print(bool(""))

# if "":
#     print("hello")

# --------------------------- Comparison Opertators -------------------------- #
# print( 3>2 )    # True
# print( 3!=3 )   #  False
# print( 3==3 )   #  False
# print( 3>"2" ) # Error


# print(9 < 1000)     # True
# print("9" < "1000") # False
# # print("9" < "1") # False
# # print(57 < 49)      #False


# print( "2">"21")
# print( "">"1") #False

# print(ord("9"))

# x = -4
# print( 1<=x<=10)

# user_age = int(input("Enter age:"))
# if 10<user_age<120:
#     print("Valid")
# else:
#     print("Invalid")



# ---------------------------- Logical Operations ---------------------------- #
# "if the user is adult AND the user is from Bulgaria"
# user_age = 19
# user_country = "UK"

# if user_age>=18 and user_country=="BG":
#     print("Добре дошли!")



#  2+3 = 3+2 (Associative Operations)
### and (Logical And)
# print(0 and "yes") # 0

# 1 and 2434343.989898-87884.8 # 0
# 1 and print("Hello")

### or (Logical Or)
# print( True or False) #True
# print( 2.14 or 56-8 ) #2.14


# ### not (Logical Not)
# print( not True) # False
# print( not 2.14) # False

#TASK: if user did not enter a name=> user_name = "Anonymous"
# user_name = "Ada"

# user_name = user_name or "Anonymous"

# print(user_name) #Anonymous>


# ------------------------------- if statement ------------------------------- #
# Task: if x is even, print("Even")
# x = 7
# if x%2==0:
#     print("~"*10)
#     print("Even")
#     print("~"*10)

# print("End")


# Task: if x is even, print("Even")
#       if x is odd, print("Odd")

# x = 8
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")



# Task: if x is even, print("Even")
#       if x is odd, print("Odd")
#       if x is 0, print("Zero")
#       if x is 3, print("Three")
# x = 8

# if x==0:
#     print("Zero")
# elif x==3:
#     print("Three")
# elif x%2==0:
#     print("Even")
# else:
#     print("odd")

# print("End")


# -------------------------- Conditional Expression -------------------------- #
# x if condition else y


# user_age = 55
# status = "adult" if user_age>=18 else "child"

# if user_age>=18:
#     status = "adult"
# else:
#     status = "child"


# print(status)

# # RAM:
# #          : 0x123: "" (imutable)
# #          status : Ox342: "adult"(imutable)


# -------------------------- Statement vs Expression ------------------------- #
# Statement:
# x=8
# if 2>3:5
# # print(x=8)

# # Expression
# print(2+2)
# print("5")
# print(55)
# print(x)
# print( 1 if 0 else 5 ) #5
# print( 1 if True else 5 ) #1


# ---------------------------- Operator precedence --------------------------- #
print( (2+3)*4 )

print( 2 + 3 * 4 > 3 and 3 )
print( ((2 + 3 * 4) > 3) and 3 )