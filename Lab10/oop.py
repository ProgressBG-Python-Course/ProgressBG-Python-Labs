# ------------------ Class Attributes vs Instance Attributes ----------------- #
# class Person:
#     count=0

#     def __init__(self, name="Anonymous", age=0) -> None:
#         print("A new Person is created!")
#         self.name=name
#         self.age=age
#         Person.count+=1



# pesho = Person("Petar", 24) # Person.__init__(pesho, "Petar", 24)
# maria = Person()

# print(pesho.__dict__)
# print(maria.__dict__)

# pesho.count = 10

# print(pesho.__dict__)
# print(maria.__dict__)



# # print(Person.count) # 2
# # print(maria.count) # 2


# # RAM:
# #     Person:
# #         count: 2

# #     pesho:
# #         name: Petar
# #         age: 24
# #         count: 10
# #     maria:
# #         name: Anonymous
# #         age: 0


# print(pesho.name)
# print(pesho.age)

# print(maria.name)
# print(maria.age)

# print(Person.count)


# ----------------------------- Instance Methods ----------------------------- #
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # define instance method
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")



# pesho = Person("Petar", 24) # Person.__init(pesho, "Petar", 24)
# maria = Person("Maria", 30)
# pesho.greet()    # Person.greet(pesho)
# maria.greet()    # Person.greet(maria)


# # ------------------------------- More on self ------------------------------- #
# class A:
#     def method1(self, obj):
#         print(self)
#         print(obj)
#         print(self==obj)

# # create an object of class A
# a = A()

# # call method1 on the object a
# a.method1(a)

# # is equivalent to:
# A.method1(a, a)

# ------------------------------- Class Methods ------------------------------ #

# class Person:
#     count = 0

#     @classmethod
#     def increment_count(obj):
#         # do additional actions or checks...
#         obj.count +=1

#     def __init__(self, name):
#         self.name = name
#         Person.increment_count() #Person.increment_count(Person)


#     # define instance method
#     def greet(self):
#         print(f"Hello, my name is {self.name} !")


# maria = Person("Maria Popova")
# petar = Person("Petar Ivanov")

# print(Person.count)

# maria.greet()

# ------------------------------ Static Methods ------------------------------ #
# class Car:
#     count = 0
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     @classmethod
#     def increment_count(cls):
#         print(f"id(cls):{id(cls)}")
#         Car.count+=1

#     @staticmethod
#     def convert_to_celsius(cls):
#         print("Converted!")

#     # instance method
#     def drive(self):
#         print("Driving")


# car1 = Car("Ford", "Fiesta")
# car1.drive()  # Car.drive(car1)
# Car.increment_count() # Car.increment_count(Car)
# print(f"id(Car): {id(Car)}")
# Car.convert_to_celsius() #Car.convert_to_celsius()


# -------------------------- Magic methods (__str__) ------------------------- #
# class A:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         print("str is called!")
#         return f"name:{self.name}"




# a1 = A("a1")
# a2 = A("a2")
# print(a1)
# print(a2)


# class BankAccount:
#     def __init__(self, name, balance) -> None:
#         self.name=name
#         self.balance=balance

#     def __add__(obj1,obj2):
#         return obj1.balance + obj2.balance


# account1 = BankAccount("Maria", 100)
# account2 = BankAccount("Pesho", 200)



# print(account1+account2) # BankAccount.__add__(account1, account2)


# ------------------------ Example: create student objects ----------------------- #
# TASK:
# 1. Define class Student:
#     name: string,
#     score: int

# 2, User enters data for 2 students:

# class Student:
#     def __init__(self,name,score) -> None:
#         self.name=name
#         self.score=score

#     def __str__(self) -> str:
#         return f"name:{self.name}\nscore:{self.score}"


# maria = Student("Maria",5)
# print(maria)
# students = [
#     Student("Maria",5),
#     Student("Pesho", 4)
# ]

# print(students[1].score)


# students = []
# for _ in range(2):
#     name = input("Enter a name: ")
#     score = input("Enter a score: ")

#     student = Student(name, score)
#     students.append(student)


# for student in students:
#     print(student)


# -------------------------------- Inheritance ------------------------------- #

# class A:
#     def __init__(self,id) -> None:
#         self.id = id


# class B(A):
#     pass


# class C(B):
#     pass


# c = C(1)
# print(c.id)


# class Person():
#     def __init__(self,name) -> None:
#         if len(name)>3:
#             self.name=name

#     def greet(self):
#         print(f"Hi, my name is {self.name}")


#     def __str__(self) -> str:
#         return f"name: {self.name}"


# class Student(Person):
#     def __init__(self, name, score):
#         # Person.__init__(self, name)
#         super().__init__(name)
#         self.score = score


#     def __str__(self) -> str:
#         return super().__str__() + f"\nscore:{self.score}"

#     def greet(self):
#         # Person.greet(self)
#         super().greet()
#         print(f"My score is {self.score}")



# class Teacher(Person):
#     pass



# pesho = Student("Pesho", 5) # Student.__init__(pesho, "Pesho",5)
# maria = Teacher("Maria") # Teacher.__init__(maria, "Maria")
# print(pesho)
# print(maria)

# pesho.greet()


# ------------------------------- Encapsulation ------------------------------ #
class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance


    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance

    def get_balance(self):
        return self.__balance




acc1 = BankAccount(100)

# acc1.set_balance(300)
acc1._BankAccount__balance=-99999

print(acc1.get_balance())

