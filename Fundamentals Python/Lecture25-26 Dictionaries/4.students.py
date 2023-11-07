students = {}


while True:
    command = input()
    if ":" not in command:
        searched_course = " ".join(command.split("_"))
        break
    name,id,course = command.split(":")
    if course not in students:
        students[course] ={}
    students[course][id] = name


for key, value in students.items():
    if key == searched_course:
       for id,name in value.items():
           print(f"{name} - {id}")


# students_dict = {}
# command = input()
# while ":" in command:
#     info = command.split(":")
#     name, id, course = info[0], info[1], info[2]
#     if course not in students_dict:
#         students_dict[course] = {}
#     students_dict[course][id] = name
#     command = input()
#
# print(students_dict)
