                                  # 1. Старата библиотека
# # Solution 1
# checked_books = 0
# target_book = input()
#
#
# command = input()
# while command != "No More Books":
#     current_book = command
#     if current_book == target_book:
#         break
#
#     checked_books += 1
#     command = input()
#
# if command != "No More Books":
#     print(f"You checked {checked_books} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")
#
#             # Solution 2
# NO_MORE_BOOKS_COMMAND = "No More Books"
#
# checked_books = 0
# target_book = input()
#
# command = input()
# while not command == NO_MORE_BOOKS_COMMAND:
#     current_book = command
#     if current_book == target_book:
#         print(f"You checked {checked_books} books and found it.")
#         break
#
#     checked_books += 1
#     command = input()
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")
#

# Solution 3
# NO_MORE_BOOKS_COMMAND = "No More Books"
#
# checked_books = 0
# target_book = input()
#
# is_book_found = False
# while True:
#     command = input()
#     if command == NO_MORE_BOOKS_COMMAND:
#         break
#
#     current_book = command
#     if current_book == target_book:
#         is_book_found = True
#         break
#
#     checked_books += 1
#
# if is_book_found:
#     print(f"You checked {checked_books} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")


                             # 2. Подготовка за изпит

# threshold = int(input())
# #command = input()
# #grade = int(input())
# counter_task = 0
# bad_grades = 0
# total_sum_grades = 0
# last_task = ""
# is_failed = True
#
# while bad_grades < threshold:
#     command = input()
#     if command == "Enough":
#         is_failed = False
#         break
#     grade = int(input())
#     if grade <= 4:
#         bad_grades += 1
#     total_sum_grades += grade
#     counter_task += 1
#     last_task = command
#
#
#
# average_grade = total_sum_grades / counter_task
# if is_failed:
#     print(f"You need a break, {bad_grades} poor grades.")
# else:
#     print(f"Average score: {average_grade:.2f}")
#     print(f"Number of problems: {counter_task}")
#     print(f"Last problem: {last_task}")

                     # 3. Почивка

# needed_money = float(input())
# owned_money = float(input())
#
# days_counter = 0
# spending_counter = 0
#
# while spending_counter < 5:
#     command =input()
#     spend_or_save_amount = float(input())
#     if command == "spend":
#         owned_money -= spend_or_save_amount
#         if owned_money < 0:
#             owned_money = 0
#         spending_counter += 1
#         days_counter += 1
#     elif command == "save":
#         owned_money += spend_or_save_amount
#         spending_counter = 0
#         days_counter += 1
#         if owned_money >= needed_money:
#             break
# if owned_money >= needed_money:
#     print(f"You saved the money for {days_counter} days.")
# else:
#     print(f"You can't save the money.\n{days_counter}")

                                     #4. Стъпки

# GOAL = 10_000
# daily_steps = 0
#
# while daily_steps <= GOAL:
#     command = input()
#     if command != "Going home":
#         current_steps = int(command)
#         daily_steps += current_steps
#     else:
#         steps_to_home = int(input())
#         daily_steps += steps_to_home
#         break
#
# steps_difference = daily_steps - GOAL
# if daily_steps >= GOAL:
#     print(f"Goal reached! Good job!")
#     print(f"{abs(steps_difference)} steps over the goal!")
# else:
#     print(f"{abs(steps_difference)} more steps to reach goal.")




                     #5. Монети

# amount = float(input())
# amount_in_coins = int(amount * 100)
# coins_count = 0

# while amount_in_coins > 0:
#     if amount_in_coins >= 200:
#         amount_in_coins -= 200
#         coins_count +=1
#     elif amount_in_coins >= 100:
#         amount_in_coins -= 100
#         coins_count += 1
#     elif amount_in_coins >= 50:
#         amount_in_coins -= 50
#         coins_count += 1
#     elif amount_in_coins >= 20:
#         amount_in_coins -= 20
#         coins_count += 1
#     elif amount_in_coins >= 10:
#         amount_in_coins -= 10
#         coins_count += 1
#     elif amount_in_coins >= 5:
#         amount_in_coins -= 5
#         coins_count += 1
#     elif amount_in_coins >= 2:
#         amount_in_coins -= 2
#         coins_count += 1
#     elif amount_in_coins >= 1:
#         amount_in_coins -= 1
#         coins_count += 1
# print(coins_count)




                      # 6. Торта

# length_cake = int(input())
# width_cake = int(input())
# size = length_cake * width_cake
# command = input()
#
# while not command == "STOP":
#     size -= int(command)
#     if size <= 0:
#         break
#     command = input()
#
# if command == "STOP":
#     print(f"{size} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(size)} pieces more.")


                         #7. Преместване

# width = int(input())
# length = int(input())
# height = int(input())
# command = input()
# filled_space = 0
# cubic_free_space = width * length * height
#
#
# while command != "Done":
#     boxes = int(command)
#     filled_space += boxes
#     if filled_space >= cubic_free_space:
#         break
#
#     command = input()
# if command == "Done":
#     print(f"{cubic_free_space-filled_space} Cubic meters left.")
# else:
#     print(f"No more free space! You need {filled_space - cubic_free_space} Cubic meters more.")

