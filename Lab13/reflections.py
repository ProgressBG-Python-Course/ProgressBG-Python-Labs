class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# print(dir("1"))
# print("1".__dir__())

p1 = Person("Maria", 23)
# print(type(p1))
# print(type(1))

# print(hasattr(p1, "name"))
# print(hasattr(p1, "town"))

attribute_name = "name"
# print(getattr(p1, "town", None))
print(getattr(p1, attribute_name, None))
