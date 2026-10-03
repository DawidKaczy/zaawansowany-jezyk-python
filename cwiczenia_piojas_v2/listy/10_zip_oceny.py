student_names = ["Alice", "Bob", "Charlie", "Diana"]
student_grades = [85, 92, 78, 95]
student_records = zip(student_names, student_grades)

for names, grades in student_records:
    if grades > 80:
        print(names, grades)