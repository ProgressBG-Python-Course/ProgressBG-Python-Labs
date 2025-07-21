

# def get_data():
#     car1 = {
#         "model": "Ford",
#         "year": 2020,
#         "color":"black",
#         "speed": 240
#     }

#     return car1


# def show():
#     print(car1)

# def make_test_drive(car):
#     car["speed"] = 240*2
#     print(f'The {car1["model"]} from {car["year"]} is drivng with {car["speed"]}')



# car1 = get_car_data()
# make_test_drive(car1)
# show_car()

# cars = []
# cars.append(get_data())


# print( type(2.34) )


# ----------------------------- Creating objects ----------------------------- #

# # class B:
# #     def __init__(obj):
# #         print("Object from A is created!")

# # class A:
# #     def __init__(obj):
# #         # obj = a (0x345 )
# #         print("Object from A is created!")
# #         print(id(obj))


# a1 = A() # A.__init__(a1)
# # print(id(a1))

# # a2 = A() # A.__init__(a2)

# # b = B() # B.__init__(b)

# # RAM:
# #     A: 0x123 (class def)
# #     a: 0x345
# #     b: 0x785



# define Car class:
class Car:
    # class attribute
    count = 0
    def __init__(self, model, year, color, speed):
        # Define instance attribute
        self.model= model
        self.year= year
        self.color= color
        self.speed= speed


    # define instance methods
    def make_test_drive(self):
        print(f'The {self.model} from {self.year} is drivng with {self.speed}')




# # # create Car instances
car1 = Car("Ford", "2020", "black", 240)
car2 = Car("BMW", "2022", "red", 340)

print(car1.model)
print(car2.model)

car1.make_test_drive() #Car.make_test_drive(car1)
car2.make_test_drive() #Car.make_test_drive(car1)




# RAM:
#     car1:
#         model: Ford,
#         ...:
#         speed: 240

#     car2:
#         model: BMW,
#         ...:
#         speed: 240
