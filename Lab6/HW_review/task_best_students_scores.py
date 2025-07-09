student_scores = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00
}

best_students_scores = dict(student_scores.items())

for key,value in best_students_scores.items():
    if value > 4.00:
        print(f"{key:<10}- {value:.2f}")