# ----------------------------------- *args ----------------------------------- #
# def process_user_data(name, *args):
#     print(f"name: {name}")
#     print(f"args: {args}")


# process_user_data("Maria")
# process_user_data("Maria", 23)
# process_user_data("Maria", 23, "Sofia")


# --------------------------------- **kwargs --------------------------------- #
# def process_user_data(name, **kwargs):
#     print(f"name: {name}")
#     print(f"kwargs: {kwargs}")


# process_user_data("Maria")
# process_user_data("Maria", age=23)

# process_user_data(
#     name="Maria",
#     age=23,
#     city="Sofia"
# )

### Example
# def foo(name, age, city="Sofia", *args, **kwargs):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"city: {city}")
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")


# # foo("Maria")
# foo("Maria", 23, 45)
# foo("Maria", 23, 45, "bar", color="black")



# def foo(*args, **kw):
#     print(f"args:{args}")
#     print(f"kw:{kw}")


# foo(2,3,b=4)


# --------------------- Python is Dynamic Typing Language -------------------- #
# def foo(a:int,b:int):
#     print( a+b )


# x = "1"
# y = "2"
# foo( x,y )

# print()


# ---------------------------- unpacking arguments --------------------------- #
# def my_func(p1,p2,p3):
#     print(p1, p2, p3)


# data = [1,2,3]

# my_func( data[0], data[1], data[2] )
# my_func(*data)


# def menu_print(fruit, price):
#     print(f"{fruit:.<20s}{price:.2f}")

# data = {
#     "price": 2.5,
#     "fruit": "apple"
# }

# menu_print( data["fruit"], data["price"] )
# menu_print( **data )

# x = sum((2,3,4))+1


# ---------------------------------- Return ---------------------------------- #
# def foo(x,y):
#     print(x,y)
#     return 5+5
#     print("End")


# print( 10 )

#1,2
#None

# --------------------------- First-Class Functions -------------------------- #
# A function can be assigned to variable

# def foo():
#     print('Foo')


# foo()
# bar = foo
# bar()

# # RAM:

# #     foo,bar: 0x123: print('Foo')

# def foo():
#     print('Foo')

# def bar():
#     print('Bar')

# functions = [foo, bar]

# functions[0]()
# functions[1]()


#A function can be passed as argument to another function
# def foo():
#     print('Foo')

# def bar(f):
#     print( f() )


# bar( foo )

# Foo


# # example
# def apply_function(func, value):
#     #func=square, value=5
#     return func(value)

# def square(x):
#     return x * x

# def cube(x):
#     return x ** 3

# print( apply_function(square, 5) )
# print( apply_function(cube, 5) )

### A function can be returned as value from another function
# def foo():
#     print('Foo')

# def bar():
#     return foo

# foo()
# bar()()


# ----------------------- lambda parameters: expression ---------------------- #
# def data_sorting(el):
#     return el[0]


# data = (
#     [6,5,3],
#     [2,5,6]
# )

# # sorted(iterable, /, *, key=None, reverse=False)
# # sorted_data = sorted(data,key=data_sorting )
# sorted_data = sorted(data,key=lambda el:el[0])

# print(sorted_data)
# # data = (
# #     [2,5,6]
# #     [6,5,3],
# # )


# # foo = lambda parameters: expression

# # def foo(x,y):
# #     return x+y

# foo = lambda x,y:x+y
# print( foo(3,4) )


# data = [
#     {
#         "name":"Maria",
#         "age":23
#     },
#     {
#         "name":"Ada",
#         "age":34
#     },
#     {
#         "name":"Pesho",
#         "age":16
#     }
# ]

# sorted_by_age = sorted(data, key=lambda el:el["name"])
# print(sorted_by_age)


# products = {
#     'apple': 3,
#     'coffee': 2.5,
#     'beer': 4.20
# }

# print( sorted( products.items(), key=lambda product:product[1] ))

# # [
# #     ('coffee': 2.5),
# #     ('apple': 3),
# #     ('beer': 4.20),
# # ]
