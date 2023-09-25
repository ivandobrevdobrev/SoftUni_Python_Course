# Задача 1. Приход на агенция

# company_name = input()
# adult_tickets = int(input())
# kid_tickets = int(input())
# adult_ticket_price = float(input())
# service_fee = float(input())
#
# price_adult = adult_ticket_price + service_fee
# price_kid = (adult_ticket_price * 0.30) + service_fee
# profit = ((adult_tickets * price_adult) + (kid_tickets * price_kid)) * 0.20
#
# print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")


# до 10кг – 20% от цената на багаж над 20кг
#  между 10кг и 20кг вкл. – 50% от цената на багаж над 20кг.
#  над 20кг – таксата се чете от конзолата

# baggage_over_20 = float(input())
# kg_baggage = float(input())
# days_left = int(input())
# count_baggage = int(input())
# cost = 0
#
# if days_left > 30:
#     if kg_baggage < 10:
#         cost = baggage_over_20 * 0.20 * 1.10 # оскъпяване с 10% cost = cost * 1.10
#     elif 10 <= kg_baggage <= 20:
#         cost = baggage_over_20 * 0.50 * 1.10
#     else:
#         cost = baggage_over_20 * 1.10
# elif 7 <= days_left <= 30:
#     if kg_baggage < 10:
#         cost = baggage_over_20 * 0.20 * 1.15
#     elif 10 <= kg_baggage <= 20:
#         cost = baggage_over_20 * 0.50 * 1.15
#     else:
#         cost = baggage_over_20 * 1.15
# elif days_left < 7:
#     if kg_baggage < 10:
#         cost = baggage_over_20 * 0.20 * 1.40
#     elif 10 <= kg_baggage <= 20:
#         cost = baggage_over_20 * 0.50 * 1.40
#     else:
#         cost = baggage_over_20 * 1.40
# final_cost = cost * count_baggage
# print(f"The total price of bags is: {final_cost:.2f} lv.")


# Задача 3. Алуминиева дограма


# number_items = int(input())
# type_of_items = input()
# receipt_type = input()
# price = 0
#
# if number_items < 10:
#     print("Invalid order")
# else:
#     if type_of_items == "90X130":
#         price = number_items * 110
#         if 30 < number_items <= 60:
#             price *= 0.95
#         elif number_items > 60:
#             price *= 0.92
#     elif type_of_items == "100X150":
#         price = number_items * 140
#         if 40 < number_items <= 80:
#             price *= 0.94
#         elif number_items > 80:
#             price *= 0.90
#     elif type_of_items == "130X180":
#         price = number_items * 190
#         if 20 < number_items <= 50:
#             price *= 0.93
#         elif number_items > 50:
#             price *= 0.88
#     elif type_of_items == "200X300":
#         price = number_items * 250
#         if 25 < number_items <= 50:
#             price *= 0.91
#         elif number_items > 50:
#             price *= 0.86
#     if receipt_type == "With delivery":
#         delivery = 60
#         price += delivery
#     if number_items > 99 :
#         price *= 0.96
#
#     print(f"{price:.2f} BGN")


# Задача 4. Топки

#  Ако топката е “red” точките ни се повишават с 5.
#  Ако топката е “orange” точките ни се повишават с 10.
#  Ако топката е “yellow” точките ни се повишават с 15.
#  Ако топката е “white” точките ни се повишават с 20.
#  Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число

# num = int(input())
# points= 0
# divides_black = 0
# red = 0
# orange = 0
# yellow = 0
# white = 0
# other_balls = 0
#
# for _ in range(num):
#     color = input()
#     if color == "red":
#         points += 5
#         red += 1
#     elif color == "orange":
#         points += 10
#         orange += 1
#     elif color == "yellow":
#         points += 15
#         yellow += 1
#     elif color == "white":
#         points += 20
#         white += 1
#     elif color == "black":
#         points = int(points / 2)
#         divides_black += 1
#     else :
#         other_balls += 1
#         continue
#
# print(f"Total points: {points}")
# print(f"Red balls: {red}")
# print(f"Orange balls: {orange}")
# print(f"Yellow balls: {yellow}")
# print(f"White balls: {white}")
# print(f"Other colors picked: {other_balls}")
# print(f"Divides from black balls: {divides_black}")


                      # Задача 5. Най-добър играч
# import sys
# name = input()
# max_goals = -sys.maxsize
# winner = ""
#
# while name != "END":
#     goals = int(input())
#     if goals > max_goals:
#         max_goals = goals
#         winner = name
#     if max_goals >= 10:
#         break
#     name = input()
# print(f"{winner} is the best player!")
# if max_goals >= 3:
#     print(f"He has scored {max_goals} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {max_goals} goals.")


                     # Задача 6. Баркод Генератор

# start = int(input())
# final = int(input())
# start_string = str(start)
# final_string = str(final)
#
#
# num1_start = int(str(start_string[0]))
# num2_start = int(str(start_string[1]))
# num3_start = int(str(start_string[2]))
# num4_start = int(str(start_string[3]))
# num1_final = int(str(final_string[0]))
# num2_final = int(str(final_string[1]))
# num3_final = int(str(final_string[2]))
# num4_final = int(str(final_string[3]))
#
# for i in range(num1_start,num1_final+1):
#     if i % 2 == 0:
#         continue
#     for j in range(num2_start,num2_final +1):
#         if j % 2 == 0:
#             continue
#         for k in range(num3_start,num3_final+1):
#             if k % 2 == 0:
#                 continue
#             for m in range(num4_start, num4_final +1):
#                 if m % 2 == 0:
#                     continue
#                 print(f"{i}{j}{k}{m}",end=" ")



