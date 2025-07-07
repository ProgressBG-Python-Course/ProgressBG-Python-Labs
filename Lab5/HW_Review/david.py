# legend: ✅-got correct output
#         ❌-couldnt get correct output

# ---------------------------------- Task 1 ---------------------------------- # ✅
""" DESCRIPTION:
    Write a program that asks the user to enter three numbers: start, stop, and step.
    Create a range object using these values and convert it to a list named 'numbers'.

    TIP: Use the range(start, stop, step) function and list() to convert it to a list.
"""

### Your code here


# start=input("Enter start: ")
# stop=input("Enter stop: ")
# step=input("Enter step: ")
# range=range(int(start), int(stop), int(step))
# list=list(range)
# print(list)


### EXPECTED OUTPUT:
# Enter start: 2
# Enter stop: 10
# Enter step: 2
# Generated list: [2, 4, 6, 8]

# ---------------------------------- Task 2 ---------------------------------- # ❌
""" DESCRIPTION:
    Write a program that asks the user to enter a list of numbers separated by spaces.
    Then, ask for two indices 'start' and 'end' to slice the list.
    Create a new list 'sliced_list' containing elements from 'start' to 'end' (excluding 'end').

    TIP: use str.split() method
    Use list slicing syntax list[start:end] to extract a sublist.
"""

### Your code here

numbers=input("Please enter numbers separated by spaces: ")
# start=int(input("Please enter start index: "))
# end=int(input("Please enter end index: "))
# numbers_sliced=numbers[start:end:2]
# print(list(numbers_sliced))


### EXPECTED OUTPUT:
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# Enter start index: 2
# Enter end index: 6
# Sliced list: [3, 4, 5, 6]

# ---------------------------------- Task 3 ---------------------------------- # ✅
""" DESCRIPTION:
    Write a program that generates a list of numbers from 1 to 50 using range().
    Then, create a new list 'evens' that contains only the even numbers from this list using slicing.

    TIP: Use range(start, stop) to create the initial list.
        Use slicing with a step to extract every second element.
"""

### Your code here

# numbers=range(1,51)
# numbers_list=list(numbers)
# evens=numbers_list[1:51:2]
# print(numbers_list)
# print(evens)


### EXPECTED OUTPUT:
# Original list: [1, 2, 3, ..., 50]
# Even numbers: [2, 4, 6, ..., 50]

# ---------------------------------- Task 4 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program that generates a list of numbers from 100 to 50 (inclusive), counting down by 5.
    Then, create a new list 'first_half' that contains only the first half of this list using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
        Use slicing to extract the first half.
"""

### Your code here \\ Comment: list of numbers from 100 to 50 (inclusive) has 11 elements,
### so cant be split in half

# numbers=range(100,49,-5)
# list_numbers=list(numbers)
# print(list_numbers)
# first_half=list_numbers[0:6]
# print(first_half)


### EXPECTED OUTPUT:
# Original list: [100, 95, 90, ..., 50]
# First half: [100, 95, 90, ..., 75]

# ---------------------------------- Task 5 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program that asks the user to enter a word.
    Create a new string 'reversed_word' that contains the word in reverse order using slicing.

    TIP: Use slicing with a negative step to reverse a string.
"""

### Your code here

# word=input("Please enter a word: ")
# word_reverse=word[-1::-1]
# print(word_reverse)

### EXPECTED OUTPUT:
# Enter a word: Python
# Reversed word: nohtyP

# ---------------------------------- Task 6 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program that generates a list of numbers from 10 to 100 with a step of 10.
    Then, create a new list 'middle_part' containing all elements except the first and last two using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
         Use slicing to remove the first and last two elements.
"""

### Your code here

# numbers=range(10,101,10)
# numbers_list=list(numbers)
# print(numbers_list)
# #print(len(numbers_list))
# middle=numbers_list[1:8]
# print(middle)


### EXPECTED OUTPUT:
# Original list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Middle part: [30, 40, 50, 60, 70, 80]

# ---------------------------------- Task 7 ---------------------------------- # ✅
###Comment: Description says to contain every second char, but expected output removes every second char.
### Will follow expected output

""" DESCRIPTION:
    Write a program that asks the user to enter a sentence.
    Create a new string 'every_second_char' that contains every second character from the sentence using slicing.

    TIP: Use slicing with a step to extract every second character.
"""

### Your code here

# sentence=input("Please enter a sentence: ")
# snec=sentence[0::2]
# print(snec)


### EXPECTED OUTPUT:
# Enter a sentence: Python slicing is powerful!
# Every second character: Pto lcn spwru!

# ---------------------------------- Task 8 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_names' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here

# name1=input("Please enter 1st name: ")
# name2=input("Please enter 2d name: ")
# name3=input("Please enter 3d name: ")
# names=[name1, name2, name3]
# print(names)
# names.sort()
# print(names)

### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']

# ---------------------------------- Task 9 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### Your code here

# word=input("Pleas enter a word: ")
# word_backup=word
# word=word.lower()
# drow=word[-1::-1]
# if word==drow:
#     print(f'The word {word_backup} is a palindrome')
# else:
#     print(f'The word {word_backup} is not a palindrome')


### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome