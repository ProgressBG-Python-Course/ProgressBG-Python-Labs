# class FooIterator:
#     def __iter__(self):
#         return self

#     def __next__(self):
#         return 1


# foo_iterator = FooIterator()

# print(next(foo_iterator))
# print(next(foo_iterator))
# print(next(foo_iterator))
# print(next(foo_iterator))
# print(next(foo_iterator))


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


letters_iterator = LettersIterator(start_code=97, end_code=122)

# print(next(letters_iterator))
# print(next(letters_iterator))
# print(next(letters_iterator))

for letter in letters_iterator:
    print(letter, end="; ")

# # # a,b
