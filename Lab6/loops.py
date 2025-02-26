# --------------------------------- for loop --------------------------------- #
# for num in range(3):
#     print(num)

# for l in 'abc':
#     print(l)

# d = { 'a':1, 'b':2, 'c':3 }

# for key,value in d.items():
#     print(key, value)

# total = sum(d.values())
# print(total)


# sum of 1 .. 10
# total = 0
# for num in range(1,11):
#     total+=num
# print(total)


# print( sum(range(1,11)) )


# pairs = [
#     (1, 'one'),
#     (2, 'two'),
#     (3, 'three')
# ]

# for el1,el2 in pairs:
#     print(el1, el2)


# data = ('Maria', 23)
# user_name, user_age=data
# print(user_name, user_age)

# letters = ['a', 'b', 'c']
# print( len(letters) )

# for index in range(len(letters)):
#     print(letters[index]+str(index))

# for index,el in enumerate(letters):
#     print(el+str(index))

# for i in [1,2,3]:
#     for j in "abv":
#         print(f'{i}:{j}', end=" ")

#     print('\n', '~'*30, sep='')


# 1:a 1:b 1:c
# ~~~~~~~~~~~~~~~~~~~~~~~~~


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for el in row:
#         print(el)



# ------------------------------ break operator ------------------------------ #

# for el in [1,2,3]:
#     print(el)
#     break

# print('END')


# string = "albaiba"
# for l in string:
#     if l == "i":
#         break
#     print(l)


# ----------- TASK : print odd numbers until an even number is met ----------- #
# numbers = [1,3,1,5,4,7,8]
# for num in numbers:
#     if num%2==0:
#         break

#     print(num)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# search_value = 4

# for row in matrix:
#     print(f'Processing row: {row}')
#     for element in row:
#         print(element, end=',')
#         if element == search_value:
#             break  # Breaks out of the inner loop
#     print() # print new line




# Task: user must enter a valid name, len(user_name)>3

# user_name = input('Enter a name: ')

# while len(user_name)<=3:
#     user_name = input('Enter a valid name: ')

# print(user_name)

# while True:
#     user_name = input('Enter a name: ')

#     if len(user_name)>3:
#         break

# print(user_name)



# --------------------------- Switch-case emulation -------------------------- #
# print program menu:
# print("Select an action:")
# print("1. Action 1")
# print("2. Action 3")
# print("3. Exit")

# user_choice = int(input("Enter a number [1-3]: "))
# if user_choice==1:
#     print('Action 1')
# elif user_choice==2:
#     print('Action 2')
# elif user_choice==3:
#     print('Exit')
# else:
#     print('Wrong choice!')

# match user_choice:
#     case 1:
#         print('Action 1')
#     case 2:
#         print('Action 2')
#     case 3:
#         print('Exit')
#     case _:
#         print('Wrong choice!')


# --------------------------------- Continue --------------------------------- #
# print all numbers in [1..5], but skip 3:

# for num in range(1,6):
#     if num==3:
#         continue

#     print(num, end=" ")








