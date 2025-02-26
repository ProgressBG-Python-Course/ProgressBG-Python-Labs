# new_list = [item for item in iterable if condition]
# new_dict = {key: value for item in iterable if condition}

# TASK:  swap key:value in a dict and generate a new one
# eng_bul = {
#     'apple':'ябълка',
#     'orange':'портокал',
#     'banana':'банан'
# }

# # bul_eng = {}
# # for k,v in eng_bul.items():
# #     bul_eng[v.upper()]=k.upper()

# bul_eng = {v.upper():k.upper() for k,v in eng_bul.items()}
# print(bul_eng)

#TASK: create best_students_score which have score>=4
# student_scores = {
#     'ivan':4.5,
#     'maria':5.0,
#     'asen':3.5
# }

# best_students_score = {k:v for k,v in student_scores.items() if v>=4}
# print(best_students_score)


# d = {x:x**2 for x in range(1,6)}
# print(d)

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]

# dictionary = {keys[i]: values[i] for i in range(len(keys))}
# print(dictionary)

# --------------------- Counting word frequency in a text -------------------- #
# ### Variant 1:
# # text = "apple banana apple apple banana plum"
# # words = text.split(' ')

# # word_counts = { }

# # for w in words:
# #     if word_counts.get(w):
# #         word_counts[w]+=1
# #     else:
# #         word_counts[w] = 1


# # print(word_counts)

# ### Variant 2:
# text = "apple banana apple apple banana plum"
# words = text.split(' ')

# # word_counts = {}

# # for w in set(words):
# #     word_counts[w]=words.count(w)

# word_counts = {w:words.count(w) for w in set(words)}

# print(word_counts)



# Filtering sales data for a quarterly report
# # Get quarters with average sales above 18000
sales_data = {
    'Q1': {'Jan': 10000, 'Feb': 12000, 'Mar': 15000},
    'Q2': {'Apr': 14000, 'May': 16000, 'Jun': 18000},
    'Q3': {'Jul': 17000, 'Aug': 19000, 'Sep': 21000},
    'Q4': {'Oct': 20000, 'Nov': 22000, 'Dec': 25000}
}

filtered = {
    k:round(sum(d.values())/len(d), 2)
    for k,d in sales_data.items()
    if round(sum(d.values())/len(d), 2)>18000
}
print(filtered)

# {'Q3': 19000.0, 'Q4': 22333.333333333332}