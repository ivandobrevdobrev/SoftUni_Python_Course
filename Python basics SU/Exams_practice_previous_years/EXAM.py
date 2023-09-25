# Задача 1. Коледна подготовка


# paper = int(input())
# cloth = int(input())
# glue = float(input())
# discount = int(input())
#
# total_paper = paper * 5.80
# total_cloth = cloth * 7.20
# total_glue = glue * 1.20
#
# cost = (total_paper + total_cloth + total_glue)
# total_cost = cost - (cost * discount/100)
#
# print(f"{total_cost:.3f}")


# Задача 2. Футболен екип


# В магазина, в който пазарувал предлагали тениски, шорти, чорапи и бутонки.
# Знае се, че цената на шортите е 75% от цената на тениските, а цената на чорапите е 20% от цената на
# шортите. Бутонките струват два пъти колкото тениската и шортите взети заедно. Тъй като Пепи редовно
# пазарува от този магазин, той има карта за отстъпка на стойност 15% от общата сума на покупката.

# tshirt_price = float(input())
# price_ball = float(input())
#
# shorts_price = 0.75 * tshirt_price
# socks_price = 0.20 * shorts_price
# shoes_price = 2 * (tshirt_price + shorts_price)
#
# total_cost = (tshirt_price + shorts_price + socks_price + shoes_price) * 0.85
# diff = price_ball - total_cost
# if total_cost >= price_ball :
#     print("Yes, he will earn the world-cup replica ball!")
#     print(f"His sum is {total_cost:.2f} lv.")
# else:
#     print("No, he will not earn the world-cup replica ball.")
#     print(f"He needs {abs(diff):.2f} lv. more.")


# Задача 3. Куриер Експрес

# weight = float(input())
# service = input()
# distance = int(input())
# price = 0
#
# if service == "standard":
#     if weight < 1:
#         price = distance * 0.03
#     elif 1 <= weight < 10 :
#         price = distance * 0.05
#     elif 10 <= weight < 40 :
#         price = distance * 0.10
#     elif 40 <= weight < 90 :
#         price = distance * 0.15
#     elif 90 <= weight <= 150 :
#         price = distance * 0.20
# elif service == "express":
#     if weight < 1:
#         price = distance * 0.03
#         top_up_kg = weight * 0.03 * 0.80
#         top_up_distance = distance * top_up_kg
#         price += top_up_distance
#     elif 1 <= weight < 10:
#         price = distance * 0.05
#         top_up_kg = weight * 0.05 * 0.40
#         top_up_distance = distance * top_up_kg
#         price += top_up_distance
#     elif 10 <= weight < 40:
#         price = distance * 0.10
#         top_up_kg = weight * 0.10 * 0.05
#         top_up_distance = distance * top_up_kg
#         price += top_up_distance
#     elif 40 <= weight < 90:
#         price = distance * 0.15
#         top_up_kg = weight * 0.15 * 0.02
#         top_up_distance = distance * top_up_kg
#         price += top_up_distance
#     elif 90 <= weight <= 150:
#         price = distance * 0.20
#         top_up_kg = weight * 0.20 * 0.01
#         top_up_distance = distance * top_up_kg
#         price += top_up_distance
#
# print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")


# Задача 4.Тренировка

# import math
# total_days = int(input())
# first_day_km = float(input())
# total_km_ran = first_day_km
# daily_km_sum = 0
# grand_tolal =first_day_km
# for day in range (1, total_days+1):
#     percent = int(input())
#     total_km_ran = total_km_ran +(total_km_ran * percent/100)
#     grand_tolal += total_km_ran
# diff = (grand_tolal - 1000)
# if grand_tolal >= 1000:
#     print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
# else:
#     print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(-(diff))} more kilometers")

# Задача 5. Разпродажба на екскурзии


# sea_number = int(input())
# mountain_number = int(input())
# command = input()
# sea_counter = sea_number
# mountain_counter = mountain_number
# profit = 0
# is_sold = False
# while command != "Stop":
#     if command == "sea" and sea_counter > 0:
#         profit += 680
#         sea_counter -= 1
#     if command == "mountain" and mountain_counter > 0:
#         profit += 499
#         mountain_counter -= 1
#     if sea_counter == 0 and mountain_counter == 0:
#         is_sold = True
#         break
#     command = input()
# if is_sold:
#     print(" Good job! Everything is sold.")
#     print(f"Profit: {profit} leva.")
# else:
#     print(f"Profit: {profit} leva.")

# Задача 6. Таблица за умножение

# number = int(input())
# num_to_string = str(number)
# num1 = int(str(num_to_string[0]))
# num2 = int(str(num_to_string[1]))
# num3 = int(str(num_to_string[2]))
#
# for first_num in range(1,num3+1):
#     for second_num in range(1,num2+1):
#         for third_num in range (1,num1+1):
#             if third_num <= 0 or second_num <= 0 or first_num <= 0:
#                 break
#             result = first_num * second_num * third_num
#             print(f"{first_num} * {second_num} * {third_num} = {result};")

231
205
212
213
228
229
230
235

250
225
224
225
228
231
235
234
235