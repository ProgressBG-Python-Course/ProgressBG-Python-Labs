# --------------------------- Positional Arguments --------------------------- #
# def foo(a,b):
#     print(a,b)

# # a=9
# # b=10
# # foo(a,b)
# foo(1+3,3/2)

# ------------------------- Default Parameters Values ------------------------ #
# def foo(a=1,b=10):
#     print(a,b)

# foo()    # 1,10
# foo(3)   # 3,10
# foo(4,5) # 4,5


# ----------------------------- Keyword Arguments ---------------------------- #
# def foo(a,b):
#     print(a,b)

# foo(b=2, a=1) # 1,2
# foo(a=1, b=2) # 1,2

# def greet(name, age, salary ):
#     print(salary)


# greet(age=23, salary=345, name='Ada')


# def greet(msg, name):
#     print(f"{msg} {name}!")

# greet("Hi", name="Maria")

# -------------- Variable Number of Positional Arguments (*args) ------------- #
# def add(*args):
#     print(sum(args))


# add(2,3)
# add(2,3,4)
# add(2,3,4,5)


# def greet(first_name, *args):
#     # first_name='Ada'
#     # args = ( 'Byron', 'Second')
#     print(f"Hello, {first_name}!")
#     for other_name in args:
#         print(f"Hello, {other_name}!")


# greet('Ada', 'Byron', 'Second')



# def print_user_data(**kw):
#     for k,v in kw.items():
#         print(f'{k}:{v}')


# print_user_data(name='Ada', age=28)
# print_user_data(name='Maria', age=30, town='London')


# def foo(var1, *var2):
#     print(var2)    # 4 | (4, ) | '4'


# foo(1,2,3)

# ---------------------------- Unpacking Arguments --------------------------- #

# def foo(a,b,c):
#     print(a,b,c)


# data=(1,2,3)

# # foo(data[0], data[1], data[2])
# foo( *data )


# def bar(*args):
#     print(args)

# bar(1,2,3)


# def menu_print(fruit, price):
#     print(f"{fruit:.<20s}{price:.2f}")


# data = {
#     "price": 2.5,
#     "fruit": "apple"
# }

# menu_print( fruit=data['fruit'], price=data['price'])
# menu_print( **data )


# ---------------------------------- Return ---------------------------------- #
# def add(x,y):
#     pass


# print( add(2,4) ) #None
# print( add(4,89) ) #5


# ------------------------------Sorted

# l = [4,2,5]
# sorted_l = sorted(l)
# print(sorted_l)

# data = [
#     {
#         'prod_name':'Prod1',
#         'price': 4
#     },
#     {
#         'prod_name':'Prod2',
#         'price': 2
#     },
#     {
#         'prod_name':'Prod3',
#         'price': 5
#     }
# ]

# def sort_by_price(d):
#     return d['price']

# sorted_data = sorted(data, key=sort_by_price )
# print(sorted_data)




# ----------------------------- Funtions passed to function ---------------------------- #
# def caller(f):
#     # f=foo
#     f()

# def foo():
#     print('Foo')

# l = [1,2,3]

# # caller( l )
# caller( foo )
# # caller( foo() ) #?

# # OUTPUT:
# 'Foo'

# RAM:
#  l:0x123: 010101001 ([1,2,3])
#  foo:0x153: 011110101001 (function)
#  caller:0x153: 01101010100110101001 (function)

# ----------------------------- Lambda Expression ---------------------------- #
# def caller(key,a,b):
#     print(key(a,b))

# def add(a,b):
#     return a+b


# caller( key=lambda x,y: x+y, a=1, b=2 )




data = [
    {
        'prod_name':'Prod1',
        'price': 4
    },
    {
        'prod_name':'Prod2',
        'price': 2
    },
    {
        'prod_name':'Prod3',
        'price': 5
    }
]


sorted_data = sorted(data, key=lambda d:d['price'] )
print(sorted_data)

