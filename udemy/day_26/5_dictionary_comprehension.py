import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(20, 100) for student in names}

# dictionary comprehension
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)
