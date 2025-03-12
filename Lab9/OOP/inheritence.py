class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            print("Age is invalid")
            age = 100
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}!")

    def __str__(self):
        return f"name:{self.name}, age:{self.age}"


class Employee(Person):
    def __init__(self, name, age, salary):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.salary = salary

    def greet(self):
        # Person.greet(self)
        super().greet()
        print(f"I'm employee!")

    def __str__(self):
        return f"name:{self.name}, age:{self.age}, salary:{self.salary}"


empl1 = Employee("Petar", -23, 4000)
empl1.greet()
