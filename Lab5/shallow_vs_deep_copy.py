# ---------------------------- THIS IS NOT A COPY ---------------------------- #
user_data = ["Ada", 23, ["beer","coca-cola"]]
# user_data_copy = user_data

# RAM:
#     user_data, user_data_copy: 0x332: 0x123, 0x163
#         0x123: "Ada"
#         0x163: 23
#         0x163: ...


# user_data[1]+=1 # user_data[1] = user_data[1] + 1

# print(user_data)
# print(user_data_copy)

# ------------------------------- Shallow Copy ------------------------------- #
# user_data = ["Ada", 23, ["beer","coca-cola"]]
# user_data_copy = user_data[:]

# # user_data_copy[2] = user_data[2]

# user_data[2][1] = "pepsi"
# user_data[1]+=1

# print(user_data)
# print(user_data_copy)


# --------------------------------- Deep Copy -------------------------------- #
import copy

# user_data = ["Ada", 23, ["beer","coca-cola"]]
# user_data_copy = copy.deepcopy(user_data)

# # user_data_copy[2] = user_data[2]

# user_data[2][1] = "pepsi"
# user_data[1]+=1

# print(user_data)
# print(user_data_copy)