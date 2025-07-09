# ---------------------------- List Comprehensions --------------------------- #
# # TASK: map list elements into new list
# # letters = ['a', 'b', 'c']

# # # upper_letters = []

# # # for l in letters:
# # #     upper_letters.append(l.upper())


# # # new_list = [expression for item in iterable]
# # upper_letters = [l.upper() for l in letters]

# # print(upper_letters)#  ['A', 'B', 'C']


# # TASK: filter list
# # Filtering Even Numbers:
# numbers = [1,2,3,4,5]

# # even_numbers=[]
# # for num in numbers:
# #     if num%2==0:
# #         even_numbers.append(num)

# # new_list = [expression for item in iterable if condition]
# even_numbers = [num for num in numbers if num%2==0]

# print(even_numbers) # [2,4]


# ------------------------- Dictionary Comprehensions ------------------------ #
# new_dict = {key: value for item in iterable if condition}

# d = {el:el**2 for el in range(3)}
# print(d)



# # TASK: Create new dictionary from student_scores, containing only the items which has values > 4.0

# student_scores = {
#     'ivan':4.5,
#     'maria':5.0,
#     'asen':3.5
# }

# # best_student_scores = {}

# # for name, score in student_scores.items():
# #     if score>4:
# #         best_student_scores[name]=score


# # new_dict = {key: value for item in iterable if condition}
# best_student_scores  = {name:score for name, score in student_scores.items() if score>4}


# print(best_student_scores)


# # TASK: swap key-value dict
# eng_bul = {
#     'apple':'ябълка',
#     'orange':'портокал',
#     'banana':'банан'
# }

# bul_eng = {value:key for key, value in eng_bul.items()}
# print(bul_eng)

keys =      ['a', 'b', 'c']
values =    [1, 2, 3]


# new_dict = {key: value for item in iterable if condition}
# d  = {k:v for k,v in keys,   }





