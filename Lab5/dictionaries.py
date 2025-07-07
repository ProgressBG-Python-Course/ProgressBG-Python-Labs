# dev1_list = ["Ada", 23, ["Python", "JS"]]


# # RAM:
# #     dev1        :0x123: ...
# #     dev1[0]     :0x345: "Ada"
# #     dev1[1]     :0x355: 23
# #     dev1[2]     :0x357: ...
# #     dev1[2][0]  :0x347: "Python"
# #     dev1[2][1]  :0x747: "JS"

# print(dev1_list[1])

# ---------------------------- Create Dictionary: ---------------------------- #
# dev1_dict = {
#     "name":"Ada",
#     "age":23,
#     "skills":["Python", "JS"],
#     "employed": True
# }

# RAM:
#     dev1        :0x123: ...
#     dev1["name"]     :0x345: "Ada"
#     dev1["age"]      :0x355: 23
#     dev1["skills"]     :0x357: ...
#     dev1["skills"][0]  :0x347: "Python"
#     dev1["skills"][1]  :0x747: "JS"
# ...

# print(dev1_dict)
# print(dev1_dict["age"])

### keys can be any immutable
# d = {
#     1: 'a',
#     2: 'b'
# }

# d[2] = 'c'

# print(d)

# d = {
#     (2025, 1):234,
#     (2025, 2):908
# }

# d[(2025, 2)]+=1
# print(d)

###Keys must be unique
# d = {
#     "name": "Ada",
#     "age":23,
#     "name": "Pesho"
# }

# print(d)

### Add item
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }
# prices["cherry"] = 9.5

# print(prices)


### Remove item
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }
# del prices["cherry"]
# fruit_price = prices.pop("bananas",0 )

# print(prices, fruit_price)

### Get keys and values and (key, value) pairs
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# prices_keys = prices.keys()
# prices_values = prices.values()
# prices_items = prices.items()

# print(list(prices_keys) )
# print(list(prices_values))
# print(list(prices_items))

# # del prices["apples"]
# # print(list(prices_keys))
# # print(list(prices_values))
# # print(list(prices_items))


# # TASK: get third item key

# prices_items_list = list(prices_items)
# print(prices_items_list)
# print(prices_items_list[2][0])


# TASK: get sum of prices
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# total = sum(list(prices.values()))
# print(total)




### Loop on dict values
# prices = {
#     "apples":  2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# for p in prices.values():
#     print(p)


# TASK: print keys, but uppercased
# for key in prices.keys():
#     print(key.upper())


# TASK: output:
# prices = {
#     "apples":  2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# for key, value in prices.items():
#     print(f"{key.upper()}-{value}")


# APPLES-2.50
# ORANGES-2.43
# BANANAS-3.50



# dev1 = {
#     "name":"Ada",
#     "age":23,
#     "skills":["Python", "JS"],
#     "employed": True,
#     "address": {
#         "country":"BG",
#         "town":"Sofia"
#     },
# }

# print( dev1["address"]["country"])