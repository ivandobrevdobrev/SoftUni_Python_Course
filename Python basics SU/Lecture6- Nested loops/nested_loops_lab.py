                             #1. часовник
# FOR

# for hours in range(0,24):
#     for minutes in range(0,60):
#         print(f"{hours}:{minutes}")

# WHIHLE

# hours = 0
# while hours < 24:
#     minutes = 0
#     while minutes < 60:
#         print(f"{hours}:{minutes}")
#         minutes += 1
#     hours += 1

# 2. Таблица за умножение

# for first_num in range(1,11):
#     for second_num in range(1,11):
#         result = first_num * second_num
#         print(f"{first_num} * {second_num} = {result}")


                      #3. Комбинации

# number = int(input())
# counter_combinations = 0
# for x1 in range (number +1):
#     for x2 in range(number +1):
#         for x3 in range(number + 1):
#             if x1 +x2 +x3 == number:
#              counter_combinations +=1
# print(counter_combinations)

                    #4. Сума от две числа
# start = int(input())
# final = int(input())
# magic_num = int(input())
#
# combination_is_found = False
# counter = 0
#
# for first_num in range(start,final+1):
#     for second_num in range(start,final+1):
#         counter += 1
#         if first_num + second_num == magic_num:
#             combination_is_found = True
#             break
#     if combination_is_found:
#         break
# if combination_is_found:
#     print(f"Combination N:{counter} ({first_num} + {second_num} = {magic_num})")
# else:
#     print(f"{counter} combinations - neither equals {magic_num}")


                             #5. Пътуване

# destination = input()
# while destination != "End":
#     needed_money = float(input())
#     current_money = 0
#     while current_money < needed_money:
#         saved_money = float(input())
#         current_money += saved_money
#     print(f"Going to {destination}!")
#     destination = input()

                            #6. Сграда

# floors = int(input())
# rooms = int(input())
# floor_letter =""
# for current_floor in range(floors, 0, -1):
#     if current_floor == floors:
#         floor_letter = "L"
#     elif current_floor % 2 == 0:
#         floor_letter = "O"
#     else:
#         floor_letter = "A"
#     for current_rooms in range(rooms):
#         print(f"{floor_letter}{current_floor}{current_rooms}",end = " ")
#     print()

