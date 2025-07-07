# d = {
#     'a': 1,
#     'b': 1
# }

# s1 = {1,2,1}
# print(s1)

# # TASK: remove duplicate ids
# user_ids = [111, 222, 222, 44, 111]
# user_ids = list(set(user_ids))
# print(user_ids)


# print(1 in s1)


# ------------------------------ Set operations ------------------------------ #

s1 = {1,2,3}
s2 = {3,4,5}

print( s1.union(s2))
print( s2.union(s1))

print( s1.intersection(s2))
print( s2.intersection(s1))

print( s1.difference(s2)) # {1,2}
print( s2.difference(s1)) # {4,5}

print( s1.symmetric_difference(s2)) # {1,2,4,5}
print( s2.symmetric_difference(s1))# {1,2,4,5}



