
# Given
#     'Maria', 'Ivan', 'Pesho'
#         4,     5,       2
# TASK:
#     print the name of the student with max score

# student_names = ['Maria', 'Ivan','Pesho']
# student_scores = [4,5,2]

# print( student_names[1] )

# student1_data = ['Maria', 4]
# student2_data = ['Ivan', 5]

# l1 = [
#     1,
#     [4,5,6],
#     'Hijsdfkdshjdshjfdshjd'
# ]

# tmp_list = l1[1]
# print(tmp_list)
# print(tmp_list[2])

# print( l1[1][2] ) # [4,5,6]


# ------------------------------- Lists in RAM ------------------------------- #
# x = 4
# y = 5
# l = [4,5]

# print( x )
# print( l[0] )

# x = 9
# l[0] = 9
# print(l) # [9,5]


# RAM:
#     x:0x234: 4
#     y:0x254: 5

#     l:   0x432: 0x876,0x873
#     l[0]:0x876: 4
#     l[1]:0x873: 5


# l = [1,2,3,4]

# print( l[3-2] ) #?

# user_names = []
# user_names.append('Maria')
# user_names.append('Ivan')
# print(user_names)

# ----------------------------------- Tuple ---------------------------------- #
# user_birth_date_as_list = [21,'January',1990]
# user_birth_date_as_tuple = (21,'January',1990)

# print(user_birth_date_as_tuple[1])
# print(user_birth_date_as_tuple[-2])


# print( type([1]) )
# print( type((1)) )
# print( type((1,)) )

# t = (1,)
# print( t[0] )
# t[0] = 9

# ------------------------------- Change tuple? ------------------------------ #
# t = (
#     [1,2,3],
# )

# t[0][1] = 9
# print(t)


# # --------------------------------- Examples --------------------------------- #
# t1 = (1,2,3)
# l1 = list(t1)
# l1[1] = 9
# t1 = tuple(l1)
# print(t1)


# l = [1,2,3]
# t = tuple(l)
# print(t)

# ----------------------------------- Range ---------------------------------- #
# import sys

# l = [1,2,3,4,5,6,7,8,9,10]
# r = range(1,11)


# print( l )
# print( list(r) )

# print( f'Size of l: {sys.getsizeof(l)}')
# print( f'Size of r: {sys.getsizeof(r)}')


# r = range(3) # range(start=0, stop, step=1)
# r = range(3,1,-1)
# r = range(1,10,-2)

# r = range(10, 3, -2) # [10, 8,6,4]
# print( list(r) ) # [1, -1, -3]

# range(5) # 0,1,2,3,4

# ----------------------------- use case of range ---------------------------- #
# user_names = []

# for _ in range(3):
#     user_name = input('Enter name: ')
#     user_names.append(user_name)

# print(user_names)


# Sequence Data TYpes:
# list, tuple, range, string

# ---------------------------- Membership testing ---------------------------- #
# x in sequence
# user_name = 'Ada'
# print('a' in user_name)
# print('D' in user_name)
# print('D' not in user_name)

# print( 8 in range(5,8) )

# print( range(1,99,3)[-1] )
# print( range(1,99,3)[-2] )


# ---------------------------------- Slicing --------------------------------- #
# sliced = sequence[start:end:step]
# l = [1,2,3,4,5]
# print( l[1:3:1] ) #[2,3]
# print( l[3:] ) #[4,5]
# print( l[:3] ) #[1,2,3]
# print( l[:] ) # [1,2,3,4,5]

# l2 = l[:] # copy

# ----------------------------- Copy by reference ---------------------------- #
# l1 = [1,2]
# l2 = l1
# l1[0] = 9

# print(l1)
# print(l2)


# # RAM:
# #     l1,l2: 0x234: 0x254, 0x255
# #         0x254:1
# #         0x255:2

# ------------------------------- Copy by value ------------------------------ #
# l1 = [1,2]
# l2 = l1[:]
# l1[0] = 9

# print(l1)
# print(l2)


# RAM:
#     l1: 0x234: 0x254, 0x255
#         0x254:1
#         0x255:2
#     l2: 0x456:
#         0x454:1
#         0x455:2


# ----------------------------- Slicing Examples ----------------------------- #
# greeting = "Hello, World!"
# print( greeting[1::4] ) # "e,r"
# print( greeting[::-1])



# ---------------------------- List from sequence ---------------------------- #
# var = 'abc'
# l = list(var)
# print(l)

# ------------------------------- List Methods ------------------------------- #
l = [1,2,3]
# l.append(9)
# l.insert(1,'a')
# l.pop()
# l.pop()
# l.reverse()
# l2 = l[::-1]
# print(l)
# print(l2)
