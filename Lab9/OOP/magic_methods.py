class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name:{self.name}, age:{self.age}"

    def __lt__(self, other):
        return self.age < other.age


maria = Person("Maria", 23)  # Person.__init__(maria, 'Maria', 23)
pesho = Person("Petar", 43)  # Person.__init__(pesho, 'Maria', 23)


print(maria)  # maria.__str__(maria)

print(maria < pesho)  # maria.__lt__(maria, pesho)
