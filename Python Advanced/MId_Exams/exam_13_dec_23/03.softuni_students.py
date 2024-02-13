def softuni_students(*args, **kwargs):
    students = {}
    invalids = []

    for student in args:
        for id, course in kwargs.items():
            if student[0] == id:
                students[student[1]] = course
        if student[0] not in kwargs.keys():
            invalids.append(student[1])
    results = ""
    students_sorted = sorted(students.items())
    for data in students_sorted :
        results += f"*** A student with the username {data[0]} has successfully finished the course {data[1]}!"+"\n"
    if invalids:
        results += f"!!! Invalid course students: {', '.join(name for name in sorted(invalids))}"
    return results




# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))
