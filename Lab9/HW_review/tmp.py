list_of_numbers = [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4]

for idx in range(1, len(list_of_numbers) - 1):
    print(list_of_numbers[idx], list_of_numbers[idx + 1])
    if list_of_numbers[idx] == list_of_numbers[idx + 1]:
        pass
