# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# maria = Person("Maria Popova", 25)

# print(dir(maria))
# print(dir())


# --------------------------------- Example 2 -------------------------------- #
# class Person:
#     def __init__(self, name):
#         self.name = name


# maria = Person("Maria")

# print(maria.age)

# if hasattr(maria, "age"):
#     print(maria.age)
# else:
#     print("Attribute 'age' not found")

# # Output: Attribute 'age' not found


# print(getattr(maria, "age", 0))

# maria.age = 34

# print(maria.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# maria = Person("Maria", 34)

# user_attr = "score"

# # maria.user_attr = "5"
# setattr(maria, user_attr, 5)

# print(getattr(maria, user_attr))


# class Animal:
#     pass


# class Dog(Animal):
#     pass


# d = Dog()

# if isinstance(d, Dog):
#     print("d is a Dog")  # Output: d is a Dog

# if isinstance(d, Animal):
#     print("d is also an Animal")  # Output: d is also an Animal


import inspect


def foo():
    func_name = inspect.stack()[0][3]
    caller_name = inspect.stack()[1][3]
    print(f"I'm {func_name}.\n{caller_name} called me!")


def bar(f):
    f()


def baz(f):
    f()


bar(foo)
baz(foo)
foo()
