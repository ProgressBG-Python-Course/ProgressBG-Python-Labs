# ------------------------ Pure vs Non-pure functions ------------------------ #
# None pure
# def add(x,y):
#     print(x+y) # side effect

# Pure:
# def add(x,y):
#     return x+y


# # print( add(1,2) ) #3, None


# ------------------------------- map functions ------------------------------ #
# map(function, iterable, ...)

# input_data = [1,2,3,4]
# # output_data = [el*10 for el in input_data]
# output_data = map(lambda el:el*10, input_data)
# print(list(output_data))

# for el in output_data:
#     print(el)


# letters = map(chr, range(1040, 1072)) # chr(1040), chr(1041),..., chr(1071)

# ------------------------------ filter function ----------------------------- #
# filter(function, iterable)

input_data = [1,2,3,4]
# output_data = [el for el in input_data if el%2==0]
output_data = filter(lambda el: el%2==0, input_data)
print(list(output_data))