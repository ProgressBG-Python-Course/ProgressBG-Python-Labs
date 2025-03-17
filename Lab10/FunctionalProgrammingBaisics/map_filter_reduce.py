# ------------------------------------ Map ----------------------------------- #
# syntax: map(function, iterable1, ...)

# numbers = [1, 2, 3, 4, 5]

# # map with comprehension
# # output = [num**2 for num in numbers]


# # map with map
# # def mapping(el):
# #     return el**2
# # output = map(mapping, numbers)

# # output = map(lambda el:el**2, numbers)
# # for el in output:
# #     print(el)


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# l_sum = map(lambda a, b: a + b, l1, l2)
# print(list(l_sum))


# ---------------------------------- filter ---------------------------------- #
# # syntax: filter(function, iterable)
# l = [1, 2, 3, 4, 5]
# # evens = [num for num in l if num%2==0]
# # evens = filter(lambda num: num % 2 == 0, l)

# # for el in evens:
# #     print(el)

# # print(list(evens))


names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
not_empty_names = filter(None, names)

print(list(not_empty_names))


# ---------------------------------- reduce ---------------------------------- #
from functools import reduce

# reduce(function, iterable[, initializer])

# reduce list elements to its sum
# l = [1, 2, 3, 4, 5]
# print(sum(l))


# def reducer(a, b):
#     print(f"a={a}, b={b}")
#     return a + b


# list_sum = reduce(reducer, l, 100)
