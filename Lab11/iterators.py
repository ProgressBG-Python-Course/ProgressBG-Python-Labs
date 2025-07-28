# from random import randint

# class RandomInteger:
#     def __init__(self,count) -> None:
#         self.count = count

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count>0:
#             self.count-=1
#             return randint(1,10)
#         else:
#             raise StopIteration

# my_iterable = RandomInteger(count=10)
# my_iterator = my_iterable.__iter__()

# try:
#     print(my_iterator.__next__())
#     print(my_iterator.__next__())
#     print(my_iterator.__next__())
#     print(my_iterator.__next__())
#     print(my_iterator.__next__())
#     print(my_iterator.__next__())
# except StopIteration:
#     pass


# for num in my_iterator:
#     print(f"num = {num}")


### with list
# my_randoms = [randint(1,10) for el in range(1,10)]

# class Fibonachi:
#     a = 0
#     b = 1

#     def __init__(self, count) -> None:
#         self.count = count

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count<=0:
#             raise StopIteration

#         self.count-=1
#         a=Fibonachi.a
#         b=Fibonachi.b

#         Fibonachi.a,Fibonachi.b = b,a+b
#         return a


# for fib in Fibonachi(10):
#     print(fib, end=",")
