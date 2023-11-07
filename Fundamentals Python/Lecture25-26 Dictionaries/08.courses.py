courses_info = {}

while True:
    command = input()
    if command == "end":
        break
    course, name = command.split(" : ")
    if course not in courses_info.keys():
        courses_info[course] = []
    courses_info[course].append(name)
for course, names in courses_info.items():
    print(f"{course}: {len(names)}")
    for student_name in names:
        print(f"-- {student_name}")

