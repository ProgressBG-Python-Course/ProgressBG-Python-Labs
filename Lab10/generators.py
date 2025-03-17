# class NumberIterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = self.start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration

#         self.current += 1
#         return self.current - 1


# def number_generator(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1


# numbers = NumberIterator(1, 5)
# # numbers = number_generator(1, 5)

# for num in numbers:
#     print(num)


# ------------------------------- How it workds ------------------------------ #
# def foo_generator():
#     print("generator start")

#     # yield is almost like return, but it freezes the execution
#     yield 1
#     yield 2

#     print("generator end")


# foo_gen = foo_generator()

# for el in foo_gen:
#     print(el)


# # try:
# #     print(next(foo_gen))  # 1
# #     print(next(foo_gen))
# #     print(next(foo_gen))
# #     print(next(foo_gen))
# #     print(next(foo_gen))
# #     print(next(foo_gen))
# #     print(next(foo_gen))
# # except StopIteration:
# #     pass


# ---------------------------------- Example --------------------------------- #
class LettersIterator:
    def __init__(self, start_code, end_code):
        self.start = start_code
        self.end = end_code
        self.code = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.code > self.end:
            raise StopIteration

        self.code += 1
        return chr(self.code - 1)


# letters_iterator = LettersIterator(start_code=97, end_code=122)


# def letters_genrator(start_code, end_code):
#     for code in range(start_code, end_code + 1):
#         yield chr(code)

#     # code = start_code
#     # while code <= end_code:
#     #     yield chr(code)
#     #     code += 1


# lg = letters_genrator(97, 122)


# for letter in lg:
#     print(letter)


# ------------------------- Generator comprehensions ------------------------- #
# []
# {}

l = [1, 2, 3, 4, 5]
evens_gen = (num for num in l if num % 2 == 0)

for num in evens_gen:
    print(num)

print(list(evens_gen))
