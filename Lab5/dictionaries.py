# Lists and Dictionaries
# userAsList = ['Maria', 23, 'BG']
# userAsDict = {
#     'age':23,
#     'country':'BG',
#     'name':'Maria',
# }

# # RAM:
# #     userAsList[0]:0x123: 'Maria'
# #     userAsList[1]:0x125: 23
# #     userAsList[2]:0x151: 'BG'

# #     userAsList['name']:0x123: 'Maria'
# #     userAsList['age']:0x125: 23
# #     userAsList['country']:0x151: 'BG'

# --------------------------------- Examples --------------------------------- #
# phonebook = {
#     'maria':'0881234567',
#     'petar':'0881234543'
# }

# phonebook['maria']  = '0661234567'
# print(phonebook['maria'])

# keys may be any immutable data, even tuples
# d = {
#     ('name', 0): 'Maria',
#     ('name', 1): 'Ivan'
# }

# print(d[('name', 1)])

# unique keys
# en_bg_dict = {
#     'apple': 'ябълка',
#     'orange':'портокал',
#     'banana':'банан',
#     'apple':'манго',
# }
# print(en_bg_dict['apple'])

# prices = {
#     'apples': 2.50,
#     'oranges': 2.43,
#     'bananas': 3.50
# }

# prices['apples'] = 3.00
# print(prices)




# # Append key:value to dict
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# prices['plums'] = 1.88
# print(prices)

# Remove item
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# price_to_remove = 'Oranges'
# del prices[price_to_remove]
# print(prices)

# orange_prices = prices.pop(price_to_remove, None)
# print(prices)
# print(orange_prices)

# ------------------- Get all dictionary keys: dict.keys() ------------------- #
# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# keys = prices.keys()
# values = prices.values()
# items = prices.items()

# print(keys)
# print(values)
# print(items)

# prices['plums'] = 3.45
# print(keys)
# print(values)
# print(items)


prices = {
    "apples": 2.50,
    "oranges": 2.43,
    "bananas": 3.50
}

# for key in prices:
#     print(key)

# for fruit in prices.keys():
#     print(fruit)

# for price in prices.values():
#     print(price)

# for item in prices.items():
#     print(item[0], item[1])


# for fruit,price in prices.items():
#     print(fruit,price)



