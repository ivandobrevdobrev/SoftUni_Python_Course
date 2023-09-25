# number = 1
# while number <10:
#     print(number)
#     number+=1
# print(number)

        # 1 Read Text

# command = input()
# while command != "Stop":
#     print(command)
#     command = input()

        #2. Парола

# username = input()
# correct_password = input()
# new_password = input()
#
# while new_password != correct_password:
#     new_password = input()
# print(f"Welcome {username}!")

       #3. Сума от числа

# control_number = int(input())
# sum = 0
#
# while sum < control_number:
#     new_number = int(input())
#     sum += new_number
# print(sum)

                         #4. Редица числа 2k + 1

# number = int(input())
# current_num = 1
#
# while current_num <= number:
#     print(current_num)
#     current_num= current_num * 2 +1

                         # 5. Баланс по сметка

# total_average = 0
# command = input()
#
# while command != "NoMoreMoney":
#     current_sum = float(command)
#     if current_sum <0:
#         print("Invalid operation!")
#         break
#     print(f"Increase: {current_sum:.2f}")
#     total_average += current_sum
#     command = input()
#
# print(f"Total: {total_average:.2f}")


                   #6. Най-голямо число
# import sys
# command = input()
# max_num = - sys.maxsize
#
#
# while command != "Stop":
#     current_num = int(command)
#     if current_num > max_num:
#         max_num = current_num
#     command = input()
# print(max_num)

                       #7. Най-малко число

# import sys
# command = input()
# min_num = sys.maxsize
#
#
# while command != "Stop":
#     current_num = int(command)
#     if current_num < min_num:
#         min_num = current_num
#     command = input()
# print(min_num)

                     #8. Завършване

# name = input()
# count_class = 1
# total_grade = 0
# bad_tries = 0
# while count_class <= 12:
#     grade = float(input())
#     if grade < 4:
#         bad_tries +=1
#         if bad_tries > 1 :
#             break
#         continue
#     count_class += 1
#     total_grade += grade
# if count_class <= 12:
#   print(f"{name} has been excluded at {count_class} grade")
# else:
#   print(f"{name} graduated. Average grade: {total_grade/12:.2f}")

# 8.1

# student_name = input()
# bad_tries = 0
# current_class = 1
# total_grade = 0
# while current_class <= 12:
#     current_grade = float(input())
#     if current_grade < 4:
#         bad_tries += 1
#         if bad_tries > 1:
#             print(f"{student_name} has been excluded at {current_class} grade")
#             break
#         continue
#     current_class += 1
#     total_grade += current_grade
# else:
#     average_grade = total_grade / 12
#     print(f"{student_name} graduated. Average grade: {average_grade:.2f}")


## 8.2

# student_name = input()
# bad_tries = 0
# current_class = 1
# total_grade = 0
# is_excluded = False
# while current_class <= 12:
#     current_grade = float(input())
#     if current_grade < 4:
#         bad_tries += 1
#         if bad_tries > 1:
#             is_excluded = True
#             break
#         continue
#     current_class += 1
#     total_grade += current_grade
# if is_excluded: # if is_excluded == True
#     print(f"{student_name} has been excluded at {current_class} grade")
# else:
#     average_grade = total_grade / 12
#     print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

