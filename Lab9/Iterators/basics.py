# l = [1, 2, 3, 4, 5]
# r = range(1, 6)

# for num in r:
#     if num==3:
#         break
#     print(num)


class LettersIterator:
    def __iter__(self):
        pass

    def __next__(self):
        # a => 97
        # z => 122


for letter in LettersIterator:
    print(letter, end="")

# # a,b
