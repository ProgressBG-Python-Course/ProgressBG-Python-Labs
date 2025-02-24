# Imutable data types
# int, float, string, boolean, tuple
# Copy by value
# a = 1
# b = a # copy by value
# print(f'Before change: {a}, {b}')
# a = 9
# print(f'After change: {a}, {b}')


# Mutable:
# list
# Copy by reference with assigned
# a = [1,2,3]
# b = a # copy by reference()
# print(f'Before change: {a}, {b}')
# a[0] = 999
# print(f'After change: {a}, {b}')

# print( id(a) )
# print( id(b) )

# # shallow copy:
# a = [[1],2,3]
# # b = list(tuple(a))
# b = a[:]

# a[0][0] = 999
# print(f'After change: {a}, {b}')

# print( id(a) )
# print( id(b) )


# deep copy:
import copy
a = [[1],2,3]
b = copy.deepcopy(a)

a[0][0] = 999
print(f'After change: {a}, {b}')

print( id(a) )
print( id(b) )


# Caching data
# a = 1
# b = 1
# print( id(a) )
# print( id(b) )
# b = 2
# print( id(a) )
# print( id(b) )


# # RAM:
# #       a: 139823466547648: 1
#         b: 139823466547652: 2



