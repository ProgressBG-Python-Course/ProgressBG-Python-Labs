# # for el in "abc":
# #     print(el)

# # print("End")

# # TASK: print "Hi" 5 times
# # for el in range(5):
# #     print(el, "hi")

# # # TASK: find index of element in list
# # element = 3
# # l = [2,4,3,5,1]

# # # index = 0
# # # index_of_element = 0

# # # for el in l:
# # #     if el==element:
# # #         index_of_element = index
# # #     index+=1

# # index_of_element = l.index(element)
# # print(index_of_element) #
# # # OUTPUT: 2

# # TASK:
# colors = ["red", "green", "blue"]
# # OUTPUT:
# # red:    0
# # green:  1
# # blue:   2

# # variant1
# # index = 0
# # for color in colors:
# #     print(f"{color:10}:{index}")
# #     index+=1

# # variant2
# # for index in range(len(colors)):
# #     print(f"{colors[index]:10}:{index}")

# # # varaint 3 (Pythonic)
# # for index, color in enumerate(colors):
# #     print(f"{color:10}:{index}")


# # print( list(enumerate(colors)) )

# m = [
#     [1,2,3],
#     [4,5,6]
# ]


# for row in m:
#     # print(row)
#     for el in row:
#         print(el)



# ---------------------------- break and continue ---------------------------- #
# while True:
#     print("Hi")
#     break

# for _ in range(100):
#     print("Howdy")
#     break

# print("END")


# TASK:Output letters in a string, until 'i' letter is reached:
# user_input = "abic"
# for letter in user_input:
#     if letter=="i":
#         break
#     print(letter)


# # TASK: user must enter non empty name
# while True:
#     user_name = input("name: ")
#     if user_name!="":
#         break


# print(f"Hi {user_name}!")



#TASK: print all numbers in [1..5], but skip 3:

# for number in range(1,6):
#     if number==3:
#         continue

#     print(number)
