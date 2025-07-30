from functools import reduce

# # reduce(function, iterable[, initializer])


# input_data = [1, 2, 3, 4, 5]
# # reduced = reduce(lambda x, y: x+y, input_data)  # (((1+2)+3)+4)+5)
# reduced = reduce(lambda x, y: x+y, input_data, 100)  # ((((100+1)+2)+3)+4)+5
# print(reduced)


# products = [
#     {'name':'apples', 'price': 2},
#     {'name':'oranges', 'price': 5},
#     {'name':'bananas', 'price': 3},
# ]

# total_sum = sum( map(lambda el:el['price'], products) )
# total_sum = sum( [el['price'] for el in products] )
# total_sum = sum( (el['price'] for el in products) )

# total_sum =  reduce(a,b:a+b, map(lambda el:el['price'], products))
# print(total_sum)



# #note that here we must provide initializer
# total_sum = reduce(lambda a,b:a+b["price"], products, 0)
# #a= 0, b={'name':'apples', 'price': 2},
# #a=7, b={'name':'bananas', 'price': 3},
# print(total_sum)


# ---------------------------- map-reduce example ---------------------------- #
l1 = [1,2,3]
l2 = [4,5,6]

# # # TODO: why print is not executed
# mapped = map(lambda *elements:sum(elements), l1,l2)
# for el_sum in mapped:
#     print(el_sum)
#     if el_sum >5:
#         break




