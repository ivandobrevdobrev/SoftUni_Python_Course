# Упражнения: Вложени условни конструкции

# 1. Кино

# projection = input()
# rows = int(input())
# columns = int(input())
#
# income = 0
# cinema_capacity = rows * columns
#
# if projection == "Premiere":
#     income = cinema_capacity * 12.00
# elif projection == "Normal":
#     income = cinema_capacity * 7.50
# elif projection == "Discount":
#     income = cinema_capacity * 5.00
#
# print(f"{income :.2f} leva")

# 2. Лятно облекло

# degrees = int(input())
# time_of_day = input()
#
# outfit = ""
# shoes = ""
#
# if time_of_day == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
# elif time_of_day == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
# elif time_of_day == "Evening":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")


# 3. Нов дом

# type_of_flowers = input()
# number_of_flowers = int(input())
# budget = int(input())
# cost = 0
# if type_of_flowers == "Roses":
#     cost = number_of_flowers * 5
#     if number_of_flowers > 80:
#         cost *= 0.90
# elif type_of_flowers == "Dahlias":
#     cost = number_of_flowers * 3.8
#     if number_of_flowers > 90:
#         cost *= 0.85
# elif type_of_flowers == "Tulips":
#     cost = number_of_flowers * 2.8
#     if number_of_flowers > 80:
#         cost *= 0.85
# elif type_of_flowers == "Narcissus":
#     cost = number_of_flowers * 3
#     if number_of_flowers < 120:
#         cost += (cost * 0.15)
# elif type_of_flowers == "Gladiolus":
#     cost = number_of_flowers * 2.5
#     if number_of_flowers < 80:
#         cost += (cost * 0.20)
# difference = abs( budget - cost)
#
# if budget >= cost:
#     print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {difference:.2f} leva more.")


# 4. Лодка за риболов

# budget = int(input())
# season = input()
# fishermen = int(input())
#
# rent_price = 0
#
# if season == "Spring":
#     rent_price = 3000
#     if fishermen <= 6:
#         rent_price *= 0.90
#     elif 7 <= fishermen <= 11:
#         rent_price *= 0.85
#     elif fishermen >= 12:
#         rent_price *= 0.75
# if season == "Summer":
#     rent_price = 4200
#     if fishermen <= 6:
#         rent_price *= 0.90
#     elif 7 <= fishermen <= 11:
#         rent_price *= 0.85
#     elif fishermen >= 12:
#         rent_price *= 0.75
# if season == "Autumn":
#     rent_price = 4200
#     if fishermen <= 6:
#         rent_price *= 0.90
#     elif 7 <= fishermen <= 11:
#         rent_price *= 0.85
#     elif fishermen >= 12:
#         rent_price *= 0.75
# if season == "Winter":
#     rent_price = 2600
#     if fishermen <= 6:
#         rent_price *= 0.90
#     elif 7 <= fishermen <= 11:
#         rent_price *= 0.85
#     elif fishermen >= 12:
#         rent_price *= 0.75
#
# extra_discount = 0
#
# if fishermen % 2 == 0 and not season == "Autumn":
#     # extra_discount = rent_price * 0.05
#     # rent_price -= extra_discount
#     rent_price *= 0.95
#
# difference = abs(budget - rent_price)
#
# if budget >= rent_price:
#     print(f"Yes! You have {difference:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {difference:.2f} leva.")


# 5. Пътешествие


# budget = float(input())
# season = input()
# destination = ""
# accommodation = ""
# cost = 0
#
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         accommodation = "Camp"
#         cost = budget * 0.30
#     elif season == "winter":
#         accommodation = "Hotel"
#         cost = budget * 0.70
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         accommodation = "Camp"
#         cost = budget * 0.40
#     elif season == "winter":
#         accommodation = "Hotel"
#         cost = budget * 0.80
# elif budget > 1000:
#     destination = "Europe"
#     if season == "summer" or season == "winter":
#         accommodation = "Hotel"
#         cost = budget * 0.90
#
# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {cost:.2f}")


# 6. Операции между числа

# n1 = int(input())
# n2 = int(input())
# operator = input()
# result = 0
# even_odd = ""
#
# if operator == "+":
#     result = n1 + n2
#     if result % 2 == 0:
#         even_odd = "even"
#     else:
#         even_odd = "odd"
#     print(f"{n1} {operator} {n2} = {result} - {even_odd}")
# elif operator == "-":
#     result = n1 - n2
#     if result % 2 == 0:
#         even_odd = "even"
#     else:
#         even_odd = "odd"
#     print(f"{n1} {operator} {n2} = {result} - {even_odd}")
# elif operator == "*":
#     result = n1 * n2
#     if result % 2 == 0:
#         even_odd = "even"
#     else:
#         even_odd = "odd"
#     print(f"{n1} {operator} {n2} = {result} - {even_odd}")
# elif operator == "/":
#     if n2 != 0:
#         result = n1 / n2
#         print(f"{n1} {operator} {n2} = {result:.2f}")
#     else:
#         print(f"Cannot divide {n1} by zero")
# elif operator == "%":
#     if n2 != 0:
#         result = n1 % n2
#         print(f"{n1} {operator} {n2} = {result}")
#     else:
#         print(f"Cannot divide {n1} by zero")


# 7. Хотелска стая

# month = input()
# number_nights = int(input())
# price_studio = 0
# price_apartment = 0
#
# if month == "May" or month == "October":
#     if 7 < number_nights <= 14:
#         price_studio = number_nights * 50 * 0.95
#         price_apartment = number_nights * 65
#     elif number_nights > 14:
#         price_studio = number_nights * 50 * 0.70
#         price_apartment = number_nights * 65 * 0.90
#     else:
#         price_studio = number_nights * 50
#         price_apartment = number_nights * 65
# elif month == "June" or month == "September":
#     if number_nights > 14:
#         price_studio = number_nights * 75.20 * 0.80
#         price_apartment = number_nights * 68.70 * 0.90
#     else:
#         price_studio = number_nights * 75.20
#         price_apartment = number_nights * 68.70
# elif month == "July" or month == "August":
#     if number_nights > 14:
#         price_apartment = number_nights * 77 * 0.90
#         price_studio = number_nights * 76
#     else:
#         price_apartment = number_nights * 77
#         price_studio = number_nights * 76
#
# print(f"Apartment: {price_apartment:.2f} lv.\nStudio: {price_studio:.2f} lv.")


                     # 8. Навреме за изпит

# exam_hour = int(input())
# exam_minutes = int(input())
# arrival_hour = int(input())
# arrival_minutes = int(input())
#
# exam_time = exam_hour * 60 + exam_minutes
# arrival_time = arrival_hour * 60 + arrival_minutes
# time_difference = abs(exam_time - arrival_time)
# hour = 0
# minutes = 0
#
# if exam_time < arrival_time:
#     print("Late")
#     if time_difference < 60:
#         print(f"{time_difference} minutes after the start")
#     else:
#         hour = time_difference // 60
#         minutes = time_difference % 60
#         if minutes < 10:
#             print(f"{hour}:0{minutes} hours after the start")
#         else:
#             print(f"{hour}:{minutes} hours after the start")
#
# elif exam_time >= arrival_time and time_difference <= 30:
#     if time_difference == 0:
#         print("On time")
#     else:
#         print(f"On time\n{time_difference} minutes before the start")
# elif exam_time > arrival_time:
#     print("Early")
#     if time_difference < 60:
#         print(f"{time_difference} minutes before the start")
#     else:
#         hour = time_difference // 60
#         minutes = time_difference % 60
#         if minutes < 10:
#             print(f"{hour}:0{minutes} hours before the start")
#         else:
#             print(f"{hour}:{minutes} hours before the start")


                               # 9. Ски почивка
# "room for one person" – 18.00 лв за нощувка
# "apartment" – 25.00 лв за нощувка
# "president apartment" – 35.00 лв за нощувкa

days = int(input()) - 1  # 10 = 10-1->9 nights
room_type = input()
review = input()
price = 0
if room_type == "room for one person":
    if days < 10:
        price = days * 18
    elif 10 <= days <= 15:
        price = days * 18
    else:
        price = days * 18
elif room_type == "apartment":
    if days < 10:
        price = days * 25 * 0.70
    elif 10 <= days <= 15:
        price = days * 25 * 0.65
    else:
        price = days * 25 / 2  # ili * 0.50
elif room_type == "president apartment":
    if days < 10:
        price = days * 35 * 0.90
    elif 10 <= days <= 15:
        price = days * 35 * 0.85
    else:
        price = days * 35 * 0.80
if review == "positive":
    price *= 1 + 0.25   # plus 25% extra
else:
    price *= 1 - 0.10   # minus 25% extra

print(f"{price:.2f}")
