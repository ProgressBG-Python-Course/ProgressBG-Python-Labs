# class User:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f'{self.name}, {self.age}'

# # User.__init__(user1, 'Ivan', 23)
# user1 = User('Ivan', 23)
# print(user1)



def foo(name, age):
    print(name, age)


user = ['Ivan', 3]
foo(*user)