# ------------------------------- Pure function ------------------------------ #
def pure(x):
    return x**2


def dirty(x):
    print(x)
    return x**2


print(pure(2))  # 4


# ------------------------------- Immutability ------------------------------- #
# def change_list(l):
#     # l[0]=999
#     new_list = l.copy()
#     new_list[0] = 999
#     return new_list


# change_list([1,2,3])

# ---------------------------------- Lambdas --------------------------------- #


# def caller(f, x):
#     return f(x)


# def sqrt(x):
#     return x**2


# print(caller(lambda x: x**2, 2))  # None
