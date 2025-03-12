# ---------------------------------------------------------------------------- #
#                             Задачи върху списъци                             #
# ---------------------------------------------------------------------------- #

# --------------------------------- Задача 1. -------------------------------- #
# Напишете програма, която чете цели числа въведени от потребителя и ги
# съхранява в списък. Програма трябва да продължи да чете стойности, докато
# потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от
# потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност.
# Пример:
#     вход: 2,3,1,6,5,4,2,0
#     изход:1,2,2,3,4,5,6,

# YOUR CODE HERE

# list_of_numbers = []
# while True:
#     integer = int(input("Enter a number: "))
#     if integer != 0:
#         list_of_numbers.append(integer)
#         continue
#     else:
#         sorted_list = sorted(list_of_numbers)
#         print(*sorted_list, sep = ", ")
#         break


# --------------------------------- Задача 2. -------------------------------- #
# Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени.
# Пример:
#   вход: first; second; first; third; second
#   изход:first; second; third

# YOUR CODE HERE

# list_of_words = []
# while True:
#     word = (input("Enter a word: "))
#     if word != "":
#         if word in list_of_words:
#             continue
#         else:
#             list_of_words.append(word)
#         continue
#     else:
#         print(", " .join(list_of_words))
#         break


# --------------------------------- Задача 3. -------------------------------- #
# Да се създаде програма, която да чете цели числа въведени от потребителя,
# докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
# трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
# положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
# който са въведени от потребителя.
# Пример:
#   вход:   3, -4, 1, 0, -1, 0, -2
#   изход: -4, -1, -2, 0, 0, 3, 1

# YOUR CODE HERE

# negative_numbers = []
# zeros = []
# positive_numbers = []
# while True:
#     user_input = input("Enter a number: ")
#     if user_input != "":
#         user_number = int(user_input)
#         if user_number > 0 :
#             positive_numbers.append(user_number)
#         elif user_number < 0:
#             negative_numbers.append(user_number)
#         elif user_number == 0:
#             zeros.append(user_number)
#     else:
#         break
# print(*negative_numbers, *zeros, *positive_numbers, sep = ", ")


# --------------------------------- Задача 4. -------------------------------- #
# Напишете програма на Python, която намира най-дългата последователност от
# еднакви елементи в списък. Ако има няколко такива редици с еднаква дължина,
# върнете първата срещната.
# Пример:
#     дадено: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2, 1],       изход:  [2, 2, 2]
#     дадено: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],    изход:  [2, 2, 2]

# YOUR CODE HERE


def find_similar(list_of_numbers):
    # [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4]
    similar_lists = []

    for idx in range(1, len(list_of_numbers) - 1): # 1,2,3,4,...9
        sublist = []
        if list_of_numbers[idx] == list_of_numbers[idx + 1]:
            sublist.append(list_of_numbers[idx])
            sublist.append(list_of_numbers[idx + 1])
            count = 2
            while (idx + count) < len(list_of_numbers):
                if list_of_numbers[idx] == list_of_numbers[idx + count]:
                    sublist.append(list_of_numbers[idx + count])
                    count += 1
                else:
                    break
            similar_lists.append(sublist)
    return similar_lists


def find_longest_list(list_of_lists):
    print(max(list_of_lists, key=len))


l = [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4]
find_longest_list(find_similar(l))


# --------------------------------- Задача 5. -------------------------------- #
# Напишете програма, която създава следната квадратна матрица m(n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 4, 7]
#         [2, 5, 8]
#         [3, 6, 9]

#     вход: n=4
#     изход:
#         [1, 5, 9, 13]
#         [2, 6, 10, 14]
#         [3, 7, 11, 15]
#         [4, 8, 12, 16]

# YOUR CODE HERE

matrix_size = int(input("Enter matrix size: "))
matrix = []
for number in range(1, matrix_size + 1):
    element = [number]
    matrix.append(element)
    count = 1
    while count < matrix_size:
        element.append(element[-1] + matrix_size)
        count += 1

for element in matrix:
    print(element)

# --------------------------------- Задача 6. -------------------------------- #
# Напишете програма, която създава следната квадратна матрица (n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 6, 7]
#         [2, 5, 8]
#         [3, 4, 9]

#     вход: n=4
#     изход:
#         [1, 8, 9, 16]
#         [2, 7, 10, 15]
#         [3, 6, 11, 14]
#         [4, 5, 12, 13]

# YOUR CODE HERE
