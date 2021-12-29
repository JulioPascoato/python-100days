import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {name: random.randint(1, 101) for name in names}
print(student_score)

passed_students = {student: value for (student, value) in student_score.items() if value >= 60}
print(passed_students)