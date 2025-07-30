def greet(name):
    print(f"Hello, {name}!")

def foo():
    print("This is a function in my_module.")
    bar()

def bar():
    print("This is another function in my_module.")


# print("This is my_module.py, and it has been imported.")


# print(f"__file__: {__file__}")
print(f"__name__ in my_module: {__name__}")