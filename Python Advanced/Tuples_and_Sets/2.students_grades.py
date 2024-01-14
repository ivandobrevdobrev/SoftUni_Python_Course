n = int(input())

student_grades = {}

for _ in range(n):
    name, grades_as_str = input().split()
    grades = float(grades_as_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grades)
for name, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{(g):.2f}' for g in grades])}"
    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
