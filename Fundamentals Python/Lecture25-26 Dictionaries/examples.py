
# my_old_dict ={'fruit': 'orange', 'veg\'s': 'potato'}
# my_dict = dict(name="Ivan", age=22)
# print(my_dict)
# print(my_old_dict)
# print(my_dict['name'])
# print(my_dict.get('age'))
# #print(my_dict["address"])
# print(my_dict.get('address'))

# keys = ['name', 'age', 'major']
# values =['Ivan', 33, 'computer science']
# student = dict(zip(keys,values))
# print(student)
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     student[key] = value

# student1 = {'name': 'Ivan', 'age': 33, 'major': 'computer science'}
# student1['phone_number'] = '08886858260'


student1 = {'name': 'Ivan', 'age': 33, 'major': 'computer science', 'phone_number': '08886858260'}

           # using keys() metod

# for key in student1.keys():
#     print(key,end = " ")

# for key in student1.keys():
#     student1[key] = 0
# print(student1)

          # using keys() metod to get values
# for key in student1.keys():
#     print(student1[key],end= " ")

            # using values() metod

# for value in student1.values():
#     print(value,end =" ")

            # using items() - to get both

# for key,value in student1.items():
#     print(key,value)

                  # check for existence

# if 'name' in student1.keys():
#     print(student1['name'])
# if '08886858260' in student1.values():
#     print('yes')

# other_info = {'address': 'Burgas'}
# student1.update(other_info)
# print(student1)

           # Nested Dictionaries

# student_record = {
#     'Ivan':{'math': 5, 'english': 6}
# }
# print(student_record['Ivan'])
# print(student_record['Ivan']['math'])
#
# student_record['Mitko'] ={}
# student_record['Mitko']['math'] = 4
# print(student_record)
#
# for name,value in student_record.items():
#     print(f"*** {name} ***")
#     for subject, score in value.items():
#         print(f'{subject}:{score}')



          #Dictionary Comprehension

# fruits = ["banana", "apple", "plum"]
# fruit_length = {fruit:len(fruit) for fruit in fruits}
# print(fruit_length)

# text = input()
# while text != "end":
#    text_reversed = ""
#    for ch in reversed(text):
#       text_reversed += ch
#    print(text + " = " + text_reversed)
#    text = input()


#Sorting Dictionaries

some_dict = {"Pesho": 20, "Gosho": 30}
print(sorted(some_dict)) #сортира във възходящ по Keys само
print(sorted(some_dict.items(),key=lambda x:x[1])) # сортира Items според Value
print(sorted(some_dict.items(),key=lambda x:x[0])) # сортира Items според Key