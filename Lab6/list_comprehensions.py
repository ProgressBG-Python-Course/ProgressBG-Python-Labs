# ----------------------- TASK: map input to an output ----------------------- #
# numbers = [1,2,3]

# # squares = []
# # for num in numbers:
# #     squares.append(num**2)

# # new_list = [expression for item in iterable if condition]
# squares = [num**2 for num in numbers]

# print(squares) #[1,4,9]

# ------------------------------- TASK: filter ------------------------------- #
# numbers = [1,2,3,4,5]

# evens = []
# for num in numbers:
#     if num%2==0:
#         evens.append(num)

# evens = [num for num in numbers if num%2==0]

# print(evens) #[2,4]


# TASK: create squares of evens from iterable
# numbers = [1,2,3,4,5]
# squares_of_evens = [num**2 for num in numbers if num%2==0]

# print(squares_of_evens) # [4,16]


# Map Celsius temperatures to Fahrenheit
# celsius = [0, 20, 37, 100]
# fahrenheit = [(temp * 9/5) + 32  for temp in celsius]

# Flattening a nested list
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # flatten = []
# # for row in matrix:
# #     for el in row:
# #         flatten.append(el)

# flatten = [el for row in matrix for el in row ]

# print(flatten) # [1,2,3,4,5,6,7,8,9]


