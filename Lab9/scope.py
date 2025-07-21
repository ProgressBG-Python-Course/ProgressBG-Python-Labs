import pprint

# --------------------------------- Example 1 -------------------------------- #
# x = 10  # A global variable

# def foo():
#     x = 20  # A local variable

#     def bar():
#         pass

#     print("Local Scope:")
#     pprint.pprint(locals())
#     print("Global Scope:")
#     pprint.pprint( globals())


# foo()


# print(__file__)


# # global = {
# #     x:10,
# #     foo: function
# # }


# --------------------------------- Example 2 -------------------------------- #

# def outer():
#     def inner():
#         print(f'x = {x} in inner')

#     inner()
#     print(f'x = {x} in outer')

# x = 1
# outer()
# print(f'x = {x} in global')


# # global = {
# #     outer: fn,
# #     x:1,

# # }

# # local_outer = {
# #     inner: fn
# # }

# # local_inner = {

# # }


# --------------------------------- Example 3 -------------------------------- #

# def change_x(a):
#     # global x
#     return a

# x = 1
# x = change_x(5)

# print(x) #


# --------------------------------- Example 4 -------------------------------- #
# def foo():
#     max = 5
#     print(max([1,2,3]))


# foo()


# print(max([1,2,3]))