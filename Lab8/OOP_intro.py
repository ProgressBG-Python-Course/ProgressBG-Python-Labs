# ---------------------------- Procedural Paradigm --------------------------- #
# get_user_number
# def get_user_number():
#     pass


# def set_level():
#     user_input = input("Select level: ")
#     if user_input == 1:
#         level = "easy"

#     return level


# def main():
#     level = set_level()


# main()


# ----------------------------- Class definition ----------------------------- #
# class Car:
#     def __init__(self, maker, speed):
#         # print("Object is initialized")
#         self.maker = maker
#         self.speed = speed

#     def stop(self):
#         print("stop is executed")
#         self.speed = 0


# ford = Car("Ford", 200)
# honda = Car("Honda", 230)
# bmw = Car("BMW", 260)

# print(f"{ford.maker} speed is {ford.speed}")
# print(f"{honda.maker} speed is {honda.speed}")
# print(f"{bmw.maker} speed is {bmw.speed}")


# ------------------------------ __init__ method ----------------------------- #
# class A:
#     def __init__(self, color):
#         self.color = color


# a1 = A("red")  # A.__init__(a1,"red")
# a2 = A("green")  # A.__init__(a2, "green")

# print(a1.color)
# print(a2.color)

# -------------------------------- Attributes -------------------------------- #


# # ----------------------- Access  Attributes and Instance Methods ---------------------- #
# class A:
#     def __init__(self, id):
#         print(self)
#         self.id = id

#     def show_ID(self):
#         print(self)
#         print(self.id)


# a1 = A(1)
# a2 = A(2)


# print(a1.id)  # 1
# print(a2.id)  # 2

# a1.show_ID()  # 1
# a2.show_ID()  # 2


# ----------------------- Instance and class attributes ---------------------- #
# class A:
#     # count is class attribute
#     count = 0

#     def __init__(self, id):
#         self.id = id  # id is instance attribute


# a1 = A(1)
# a2 = A(2)

# a1.id = 2

# print(f"a1.id={a1.id}")
# print(f"a2.id={a2.id}")

# a1.count = 999  # did not modify class attribut, but creates/modifies the instance attrbute
# print(f"A.count: {A.count}")
# print(f"a1.count: {a1.count}")
# print(f"a2.count: {a2.count}")


# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         # increment count
#         Person.count += 1


# maria = Person("Maria")
# pesho = Person("Petar")

# print(Person.count)

# print(f"maria's attributes: {maria.__dict__}")


# ---------------------------------- Example --------------------------------- #
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # define instance method
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# maria = Person("Maria", 23)
# pesho = Person("Pesho", 34)

# # call greet() method on maria. python will send the maria object reference to the self parameter.
# maria.greet()
# pesho.greet()


# ------------------------------- Library ------------------------------ #
# book:
#     title: string
#     author: string

#     show_details: function, that prints book details

# library:
#     books: []
#     add_book: function, that add a book
#     show_books: function() that print all books titles


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")


book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")

sofia_library = Library()
sofia_library.add_book(book1)
sofia_library.add_book(book2)
sofia_library.show_books()  #
