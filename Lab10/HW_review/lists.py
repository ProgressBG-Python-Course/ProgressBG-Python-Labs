# --------------------------------- Задача 4. -------------------------------- #
# Напишете програма на Python, която намира най-дългата последователност от
# еднакви елементи в списък. Ако има няколко такива редици с еднаква дължина,
# върнете първата срещната.
# Пример:
#     дадено: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2, 1],       изход:  [2, 2, 2]
#     дадено: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],    изход:  [2, 2, 2]

# YOUR CODE HERE


def find_max_sequence(numbers):
    current_sequence = []
    max_sequence = []

    numbers.append(None)  # Solution for last element problem on last sequence

    for num in numbers:
        if not current_sequence or num == current_sequence[0]:
            # update current sequence
            current_sequence.append(num)
        else:
            # update max sequence and create new current sequence
            if len(current_sequence) > 1 and len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [num]

    print(max_sequence)


def find_all_sequences(numbers):
    current_sequence = []
    sequences = []

    # numbers.append(None) # Solution for last element problem on last sequence

    for num in numbers:
        if not current_sequence or num == current_sequence[0]:
            # update current sequence
            current_sequence.append(num)
        else:
            # update sequences and create new current sequence
            if len(current_sequence) > 1:
                sequences.append(current_sequence)
            current_sequence = [num]

    print(sequences)


numbers = [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4, 4]


find_max_sequence(numbers)
find_all_sequences(numbers)
