# # global scope
# x=1

# def foo():
#     # local scope
#     y=1

# foo()

# ---------------------------------- Example --------------------------------- #
# def foo():
#     x=1
#     print(f'x in foo: {x}')

# x=99
# foo()
# print(f'x in main: {x}')

# ---------------------------------- Example --------------------------------- #
# def foo():
#     print(f"x in foo: {x}")


# x = 99
# foo()
# print(f"x in main: {x}")


# foo = {

# }

# global = {
#     foo: func,
#     x:99
# }

# ---------------------------------- Example --------------------------------- #
# x = 10  # A global variable


# def foo():
#     x = 20  # A local variable
#     print("Local Scope:", locals())
#     print("Global Scope:", globals())


# foo()

# print(__name__)


# # ------------------------------- Nested scopes ------------------------------ #
# def outer():
#     x = 2

#     def inner():
#         x = 3
#         print(f"x = {x} in inner")

#     inner()
#     print(f"x = {x} in outer")


# x = 1
# outer()
# print(f"x = {x} in global")


# ---------------------------- Global and nonlocal --------------------------- #
# def change_X():
#     global x
#     x = 99


# x = 1

# change_X()
# print(x)


### example
# def outer():
#     x = 2

#     def inner():
#         nonlocal x
#         x = 3
#         print(f"x = {x} in inner")

#     inner()
#     print(f"x = {x} in outer")


# x = 1
# outer()
# print(f"x = {x} in global")
