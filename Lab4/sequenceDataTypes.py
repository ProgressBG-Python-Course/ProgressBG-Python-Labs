# ---------------------------------- Tuples ---------------------------------- #
# t = 1,2
# print(type(t))

# # TASK: swap values in x and y
# x = 1
# y = 2

# # tmp = y
# # y=x
# # x=tmp

# # (x,y) = (y,x)

# # print(x, y) # 2, 1


### Change values in tuple:
# t = (
#     [1,2,3],
#     [4,5],
# )


# t[0][1]=10
# print(t)


# def getData():
#     return (1,2,3,66)

# address = getData()
# print(address)


# # # convert value in address to list
# address = list(address)
# print(address)

# # # now address is a list, so we can mutate it
# address[3] = 25
# print(address)

# t = (1,2,3,4)
# print(t)
# ----------------------------------- Range ---------------------------------- #

# range([start,] stop[, step])
# r1 = range(1,5) # 1,2,3,4
# r1 = range(5)  # 0,1,2,3,4
# r1 = range(2,5,2)  # 2,4,

# r1 = range(5,2,1) # invalid range=>empty range
# r1 = range(2,5,-2)  # 2,0, -2,  => invalid range
# r1 = range(2,11,2)
# print(r1)
# print(tuple(r1)) # 2,4,6,8,10


### get range items:
# r1 = range(5)
# print( r1[0] )


# # range vs list size
# l1 = [1,2,3,4,5,6,7,8,9,10]
# r1 = range(1,5000)
# l_from_range = list(r1)  # convert range to list


# # get size of list in bytes
# import sys
# print(sys.getsizeof(l1))  # size in bytes of the list object
# print(sys.getsizeof(r1))  # size in bytes of the range object
# print(sys.getsizeof(l_from_range))  # size in bytes of the range object


# r1 = range(1, 5000)
# print(r1[49])

# for i in range(1, 11):
#     print(i, end=',')


# ---------------------------- Sequence Operations --------------------------- #
# # l1 = [1, 2, 3, 4, 5]
# # l2 = [6, 7, 8, 9, 10]
# # print(l1 + l2)  # Concatenation
# # print(l1 * 3)  # Repetition
# # print(l1[0])  # Indexing

# l1 = ["ala", "bala", "goga"]
# l2 = [ [1,2], 3]
# print(l1 + l2)  # Concatenation


# names=[]

# while True:
#     name = input("Enter name: ")
#     if not name:
#         break
#     names.append(name)

# print(names)

# if "maria" in names:
#     print("Hello, Maria!")

# if "ivan" not in names:
#     names.append("ivan")


# print( 23 in range(5,55) ) #True


# l1 = [1,2,3]
# l2 = [2,3]

# print( l2 in l1) #


# names = ["ivan", "maria", "pesho"]
# print(names[-1])

# names.append(99)
# print(names[-1])
# print(names[-3])

# ---------------------------------- SLicing --------------------------------- #
# # sliced = sequence[start:end:step]
l = [1,2,3,4,5]
# # print( l[1:4:2] ) # /1,3/ =>[2,4]
# # print(l[1:4]) # [2,3,4]
# print(l[2:])

# l2 = l[:] # copy list
# l[0] = 100
# print(l)
# print(l2)


# l = list(range(1,11))
# print(l)

# # print(l[-3:]) # [8,9,10]
# # print(l[-3::-1]) # [8,7,...,1]
# # print(l[:5:-1]) #

# # print(l[3:]) #
# # print(l[:3])

# ------------------------------- List Methods ------------------------------- #
l = [1,2,3]
# l.append("X")
# l.insert(1,"X")

# l.extend([5,6])
# l.remove(2)

# l.pop(0)
# print(l)


# print( l.sort(reverse=True) )
# print( l )


# list.sort vs sorted()
# user_data_from_server = ["Ada","Pesho"]
# # user_data_from_server.sort(reverse=True)
# user_data_from_server_sorted = sorted(user_data_from_server, reverse=True)
# print(user_data_from_server)
# print(user_data_from_server_sorted)
