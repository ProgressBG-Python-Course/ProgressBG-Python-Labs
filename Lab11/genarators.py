# def foo():
#     print("Start")
#     yield 1#
#     print("1 continue")
#     yield 2#
#     print("2 continue")
#     yield 3#
#     print("3 continue")



# foo_generator = foo()
# print(foo_generator.__next__())
# # Start, 1
# print(foo_generator.__next__())
# # 1 continue, 2
# print(foo_generator.__next__())
# print(foo_generator.__next__())

# # for el in foo():
# #     print(el)


# def number_generator(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1


# # Use the generator in a loop
# for num in number_generator(1, 5):
#     print(num)

# ---------------------------------- Example --------------------------------- #
# from random import randint

# def random_int(count):
#     # count =10
#     # while count>0:
#     #     yield randint(1,10)#
#     #     count-=1

#     for _ in range(count):
#         yield randint(1,10)



# random_int_generator= random_int(count=3)
# random_int_generator = (randint(1,10) for _ in range(3))

# # print(next(random_int_generator))
# # print(next(random_int_generator))

# for el in random_int_generator:
#     print(el, end=",")


# print(sum( randint(1,10) for _ in range(3) ))



# ---------------------------------- Example --------------------------------- #
# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''
print( chr(1041) )
# 'Б'
print( chr(1071) )
# 'Я'
"""


### YOUR CODE HERE
print( chr(1040) )
print( chr(1071) )

cyrilic_letter_generator = (chr(char_code) for char_code in range(1040, 1072))

# TEST:
for l in cyrilic_letter_generator:
    print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,