# ----------------------------- Basic Data Types ----------------------------- #
# print( 1 + 2 ) # 3
# print( '1' + '2' ) # 12
# print( True + True ) # 2
# print( 3 * 4 ) # 12
# print( 3 * '4' ) # 444

# print(+42)
# print(3.14 + 2)
# print(3,14 +2)
# print(3_000_000)

# print( 5/2 )
# print( 5//2 )

# print( 2**3 )

# print( 0.1+0.2 )

# import math
# print(math.sqrt(4))
# print( round(4.57,1) )


# print( 2 )
# print( '2' )

# # RAM:
# #     0x123: 00000010 (2)
# #     0x623: 01010101 ('2')


# print( '2' )
# print( "2" )
# print( "a'b")
# print( 'a'b')
# print('''1
# 2''')

# print( '1' + '2' ) # '12'
# print( '1'+'2'+'3')

# # print ( '1' + 2 ) # Error...

# print( '@'*40 )
# print( 40*'@' )

# print( 'aDa'.capitalize() )


# print( 2+3 )


# --------------------------------- Varibales -------------------------------- #
# x=4;
# print( x+1 )

# RAM:
#     x:0x123: 00000100 (4)


# Variables Rules:
# user_first_name = 'Ada'
# print(User_first_name) # Error

# User_first_name


# -------------------------------- Assignment -------------------------------- #
# x=4+1
# print(x)

# y=x+1
# print(y)

# age=35
# age=age+1 # increment
# print(age)

# RAM:
#         :0x123: 35
#     age :0x432: 36


# budget_of_current_year=2_000_000
# # budget_of_current_year=budget_of_current_year+1
# budget_of_current_year+=1


# x=1
# x-=5 # x=x-5
# print(x)


# # Statement VS Expression
# x=4  # statement
# x+1  # expression

# print(2+3)
# print( x=2 )



# a=3
# b=a
# c=a
# a=4
# a=5


# RAM:
#     b,c:0x123: 3
#        :0x456: 4!
#       a:0x426: 5!





# Comments (Toggle CTRL+/)
x=5
# if x is odd
if x%2:
    print('@')


