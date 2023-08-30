student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


# 🚨 Don't change the code above 👆

def convert_score_to_grade(score):
    grade = ""

    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"
    else:
        "Greater than 100?"

    return grade


# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_grades[key] = convert_score_to_grade(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)
