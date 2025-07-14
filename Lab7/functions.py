# What is function (in Math, or Pure Function in Programming):


# y = f(x)

# X: f=> Y
# 1: => 8.7
# 2
# 3


# ---------------------------- Why usign functions --------------------------- #
# Get user name
# user_name = "Ada"

# # # Define greet_user function
def greet_user():
    print("*"*30)
    print(f"Hello, {user_name}")
    print("*"*30)


# greet_user()


# user_name ="Pesho"
# greet_user()


# ---------------------------- Function Definition --------------------------- #
# def function_name(param_list):
#     '''docstring'''
#     code block
#     return expression
# from math import pi

# def calc_circle_square(r):
#     """string"""
#     return pi*r**2

# x  = 1

# RAM:
#     calc_circle_square: 0x123: 0101010101
#                      x: 0x435: 0000000001



# # main program
# circle1_square = calc_circle_square(10)


# user_name = "Ada"
# def greet_user():
#     """ Function that greets a user"""
#     print("*"*30)
#     print(f"Hello, {user_name}")
#     print("*"*30)


# help(greet_user)



# def greet():
#     """Just prints hello"""

#     print("Hello!")



# x = 1
# l = [1,2,3]

# print( l[0] )
# print( x+1 )
# print( greet() )
# print( greet )




#1
#2
#Hello
#None


# def greet_user(user_name):
#     print("*"*30)
#     print(f"Hello, {user_name}")
#     print("*"*30)


# greet_user("Ada")
# greet_user("Pesho")


# def add(x,y):
#     print(x+y)

# x = int(input("x="))
# y = int(input("y="))

# res1 = add(x,y)
# res2 = add(5,8)

# print(res1)
# print(res2)



# def add(x,y=1):
#     # x=3
#     #y=1
#     print(x+y)


# add(3)




# def greet( name, msg="Hi"):
#     print(f"{msg} {name}!")

# greet("Maria", "Howdy")

# greet("Howdy", "Maria")
# greet("Howdy")

# def foo(a=1,b=2,c=3):
#     print(a,b,c) # 1,9,3

# foo(1,9,3)
# foo(b=9) #


# def greet(name, msg, time):
#     print(name, msg, time)


# greet("Maria", "Howdy", "9.45")
# greet(time="9.45", msg="Howdy", name="Maria" )
# # greet(9.45, name="Maria", msg="Hi")
# greet(tme="9.45", msg="Howdy", name="Maria" )


# def foo(*x):
#   print(x)


# foo(1,2)
# foo(1,2,3)

def add(*args):
    print(sum(args))

add(1,2)
add(1,2,3)