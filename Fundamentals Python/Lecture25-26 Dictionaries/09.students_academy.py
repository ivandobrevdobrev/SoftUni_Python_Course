n = int(input())

students_info = {}
students_average_grades = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students_info.keys():
        students_info[name] = []
    students_info[name].append(grade)
for name,grade in students_info.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        students_average_grades[name] = average_grade

for name, averageGrade in students_average_grades.items():
    print(f"{name} -> {averageGrade:.2f}")