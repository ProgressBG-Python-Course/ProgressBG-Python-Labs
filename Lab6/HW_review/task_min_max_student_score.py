# --------------------------------- Varaint 1 -------------------------------- #
# student_score = {
#     'Ivan'  :5.00,
#     'Alex'  :3.50,
#     'Maria' :5.50,
#     'Georgy':5.00
# }

# # преобразувам ключовете в списък и стойностите в списък
# student_names = list(student_score.keys())
# student_scores = list(student_score.values())

# # намирам максималната и минималната стойности в списъка със стойности
# max_score = max(student_scores)
# min_score = min(student_scores)

# # отпечатвам max
# for key, value in student_score.items():
#     if value == max_score:
#         print(f'{key} - {value}')

# # отпечатвам max и min
# for key, value in student_score.items():
#     if value == min_score:
#         print(f'{key} - {value}')


# --------------------------------- Variant 2 -------------------------------- #

# scores  = [9, 2, 5, 50]
# curent_max_score = 0

# for score in scores:
#     if score>curent_max_score:
#         curent_max_score = score

# print(curent_max_score)


# student_scores = {
#     'Ivan'  :5.00,
#     'Alex'  :3.50,
#     'Maria' :5.50,
#     'Georgy':5.00,
#     'Pesho' :1.50,
# }

# curent_max_score = 0
# curent_max_score_name = ""

# for name,score in student_scores.items():
#     if score>curent_max_score:
#         curent_max_score = score
#         curent_max_score_name=name

# print(name, score)