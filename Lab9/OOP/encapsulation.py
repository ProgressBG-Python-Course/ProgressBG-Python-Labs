class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private (self._Person__age)

    def __str__(self):
        return f"name = {self.name}; age = {self.__age}"

    def set_age(self, new_age):
        self.__age = new_age


maria = Person("Maria Popova", 25)

maria.set_age(-100)
print(maria)
# maria.__age = -100
# print(dir(maria))
print(maria.__dict__)
