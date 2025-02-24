string = '1 2 3 4 5 6 7 8 9'
print( len(string) )

splitted_by_space = string.split(' ')
print(splitted_by_space)

numbers = list(map(int, splitted_by_space))


print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]