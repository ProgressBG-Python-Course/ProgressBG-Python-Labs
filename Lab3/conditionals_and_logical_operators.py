# ------------------------------- Boolean type ------------------------------- #
# print( type(True) )
# print( False )

# print( bool(0) )
# print( bool(0.08) )
# print( bool(-0.08) )

# print( bool('') ) #
# print( bool(' ') ) #


# -------------------------- Comparison Operatotions ------------------------- #
# x = 1
# print( 1==3 )
# print( 3<=3 ) #

# lexicographic sorting
# print('a'<'A') # False
# print(97<65) # False

# print('12'<'9')
# print('1'<'9') #True

# print('12'<'1a')
# print('2'<'a')

# user_age = -149
# print( 0<user_age<150 )
# print( user_age>0 and user_age<150 )


# user_age = int(input('Enter your age: '))

# print( user_age>=18 )

# x = 3
# print( str(x) < 'a' )

# ----------------------------- Logical Operation ---------------------------- #
# user_age = 1000
# print(user_age>0 and user_age<150)
# print(user_age>0 or user_age<150)



# print( True or False ) # True
# print( True and False )# False


# print( 'Hi' and 5 ) # 	if x is false, then x, else y

# print( False and 34*897 ) # False
# print( 0 and 34-89 )  # 0

# print( True or 789-8787) # True
# print( 4 or False) #4
# print( 4 or True) #4

# if user_name is empty, then user_name = 'Anonymous'
# user_name = 'Ada'

# # user_name or (user_name:='Anonymous')

# if(user_name==''):
#     user_name = 'Anonymous'

# print(user_name)




# x = 5
# print( x>0 and 5 ) #


# ------------------- Control flow (Conditional) statements ------------------ #
# user_age = 19

# if user_age>=18 :
#     print('Welcome')
#     print('*'*30)


# user_name = 'Ada'
# if user_name:
#     print('hi')


# If x is even => 'x is even!'

x = 6
if x%2==0:
    print('x is even!')