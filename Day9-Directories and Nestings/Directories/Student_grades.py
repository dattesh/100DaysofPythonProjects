student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student_name in student_scores:
    if 90 < student_scores[student_name] <= 100:
        student_grades[student_name] = "Outstanding"
        # print('Outstanding')
    elif 80 < student_scores[student_name] <= 90:
        student_grades[student_name] = "Exceeds Expectations"
        # print("Exceeds Expectations")
    elif 70 < student_scores[student_name] <= 80:
        student_grades[student_name] = "Acceptable"
        # print("Acceptable")
    elif student_scores[student_name] < 70:
        student_grades[student_name] = "Fail"
        # print("Fail")
print(student_grades)

