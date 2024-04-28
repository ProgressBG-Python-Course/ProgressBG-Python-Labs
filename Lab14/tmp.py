class Person:
    def __init__(self, name, age):
        print('Init is called!')
        self.name = name
        self.age = age

    def greet(self):
        print(f'{self.name} iself {self.age} years old!')

class User(Person):
    id = 1
    def __init__(self, name, age):
        super().__init__(name, age)




user1 = User('ivan', 32)
user2 = User('maria', 22)
# User.__init__(user1, 'ivan', 32)
# User.__init__(user2, 'ivan', 32)

user1.greet()
user2.greet()
# User.greet(user1)
# User.greet(user2)

print(user1.id)
print(user2.id)