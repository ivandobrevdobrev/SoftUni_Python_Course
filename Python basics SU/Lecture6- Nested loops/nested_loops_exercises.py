# 1. Пирамида от числа
# num = int(input())
# current = 1
# is_current_bigger_than_num = False
#
# for row in range (1,num+1):
#     for col in range(1,row+1):
#         if current > num:
#             is_current_bigger_than_num =True
#             break
#         print(str(current)+" ", end="")
#         current += 1
#     if is_current_bigger_than_num:
#         break
#     print()

# 2. Еднакви суми на четни и нечетни позиции
#
# num1 = int(input())
# num2 = int(input())
#
#
# for number in range(num1,num2+1):
#     num_to_string =str(number)
#     even_sum = 0
#     odd_sum = 0
#     for index,digit in enumerate(num_to_string):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     if even_sum == odd_sum:
#             print(number,end=" ")


# 3. Суми прости и непрости числа

# command = input()
# sum_primes = 0
# sum_non_primes = 0
# while command != "stop":
#     current_num = int(command)
#     if current_num < 0:
#         print("Number is negative.")
#         command = input()
#         continue
#
#     is_prime = True                  # намиране на съставни(не прости) числа чрез проверка дали е просто
#     for num in range(2,current_num): # започва от 2, защото простите се делят на 1 и 0. Тоест ако числото се дели на 2 без остатък значи е съставно( не просто) , ако не се дели на 2 - просто число
#       if current_num % num == 0:
#             is_prime = False
#             break
#     if is_prime:
#         sum_primes += current_num
#     else:
#         sum_non_primes += current_num
#
#     command = input()
#
# print(f"Sum of all prime numbers is: {sum_primes}")
# print(f"Sum of all non prime numbers is: {sum_non_primes}")


# 4. Train the Trainers

# number_judges = int(input())
# command = input()
# counter_command= 0
# total_average = 0
# while command != "Finish":
#     counter_command += 1
#     grades_sum = 0
#     average_grade = 0
#     for _ in range(number_judges):
#         grades = float(input())
#         grades_sum += grades
#     average_grade = grades_sum / number_judges
#     total_average += average_grade
#     print(f"{command} - {average_grade:.2f}.")
#     command = input()
# average_all = total_average / counter_command
# print(f"Student's final assessment is {average_all:.2f}.")

# 5. Специални числа - обхождане на числа като стринг

# number = int(input())
#
# for i in range(1111, 10000):
#     is_special = True
#     special_number = str(i)
#     for index, digit in enumerate(special_number):
#         if int(digit) == 0:
#             is_special = False
#             break
#         if number % int(digit) != 0:
#             is_special = False
#             break
#     if is_special:
#         print(special_number, end=" ")


                               # 6. Билети за кино

# command = input()
# student_tickets = 0
# standard_tickets = 0
# kid_tickets = 0
# total_tickets = 0
#
# while not command == "Finish":
#     movie = command
#     free_seats = int(input())
#     tickets_bought = 0
#     while tickets_bought < free_seats:
#         command = input()
#         if command == "End":
#             break
#         ticket_type = command
#         tickets_bought += 1
#         if ticket_type == "student":
#             student_tickets += 1
#         if ticket_type == "standard":
#             standard_tickets += 1
#         if ticket_type == "kid":
#             kid_tickets += 1
#     total_tickets += tickets_bought
#     capacity_filled = tickets_bought / free_seats * 100
#     print(f"{movie} - {capacity_filled:.2f}% full.")
#     command = input()
# print(f"Total tickets: {total_tickets}")
# print(f"{student_tickets / total_tickets *100:.2f}% student tickets.")
# print(f"{standard_tickets / total_tickets *100:.2f}% standard tickets.")
# print(f"{kid_tickets / total_tickets *100:.2f}% kids tickets.")
