# Задача 1. Великденски обяд


# cakes = int(input())
# eggs = int(input())
# cookies_kg = int(input())
#
# cakes_price = cakes * 3.20
# eggs_price = eggs * 4.35
# painting = eggs * 12 * 0.15
# cookies_kg_price = cookies_kg * 5.40
#
# total = cakes_price + eggs_price + painting + cookies_kg_price
#
# print(f"{total:.2f}")

# Задача 2. Великденско парти


# guests = int(input())
# price_per_guest = float(input())
# budget = float(input())
#
# if 10 <= guests <= 15:
#     price_per_guest *= 0.85
# elif 15 < guests <= 20:
#     price_per_guest *= 0.80
# elif guests > 20:
#     price_per_guest *= 0.75
# cake_price = 0.10 * budget
# total_cost = guests * price_per_guest + cake_price
# diff = abs(total_cost - budget)
#
# if total_cost <= budget:
#     print(f"It is party time! {diff:.2f} leva left.")
# else:
#     print(f"No party! {diff:.2f} leva needed.")


# Задача 3. Великденска екскурзия

#  Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
#  Втори ред - дати, през които си е резервирала екскурзията - текст с възможности "21-23",
# "24-27" или "28-31"
#  Трети ред - брой нощувки - цяло число в интервала

# destination = input()
# dates = input()
# nights = int(input())
# price_per_night = 0
# if destination == "France":
#     if dates == "21-23":
#         price_per_night = 30
#     elif dates == "24-27":
#         price_per_night = 35
#     elif dates == "28-31":
#         price_per_night = 40
# elif destination == "Italy":
#     if dates == "21-23":
#         price_per_night = 28
#     elif dates == "24-27":
#         price_per_night = 32
#     elif dates == "28-31":
#         price_per_night = 39
# elif destination == "Germany":
#     if dates == "21-23":
#         price_per_night = 32
#     elif dates == "24-27":
#         price_per_night = 37
#     elif dates == "28-31":
#         price_per_night = 43
#
# total_cost = nights * price_per_night
#
# print(f"Easter trip to {destination} : {total_cost:.2f} leva.")


# Задача 4. Битката на великденските яйца

# Solution 1

# first_player_eggs = int(input())
# second_player_eggs = int(input())
# command = input()
# while command != "End":
#     if command == "one":
#         second_player_eggs -= 1
#     elif command == "two":
#         first_player_eggs -= 1
#     if first_player_eggs == 0 or second_player_eggs == 0:
#         break
#     command = input()
#
# if first_player_eggs == 0:
#     print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
# elif second_player_eggs == 0:
#     print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
# elif command == "End":
#     print(f"Player one has {first_player_eggs} eggs left.")
#     print(f"Player two has {second_player_eggs} eggs left.")

#  Solution 2

# while True:
#     command = input()
#     if command == "End":
#         break
#     elif command == "one":
#         second_player_eggs -= 1
#     elif command == "two":
#         first_player_eggs -= 1
#     if first_player_eggs == 0 or second_player_eggs == 0:
#         break
#
# if first_player_eggs == 0:
#     print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
# elif second_player_eggs == 0:
#     print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
# elif command == "End":
#     print(f"Player one has {first_player_eggs} eggs left.")
#     print(f"Player two has {second_player_eggs} eggs left.")

#Задача 5. Великденски яйца
# import sys
# eggs = int(input())
# red_eggs = 0
# green_eggs = 0
# blue_eggs = 0
# orange_eggs = 0
# max_eggs = -sys.maxsize
# max_color = ""
#
# for _ in range(eggs):
#     color = input()
#     if color == "red":
#         red_eggs +=1
#         if red_eggs > max_eggs:
#             max_eggs = red_eggs
#             max_color = "red"
#
#     elif color == "green":
#         green_eggs += 1
#         if green_eggs > max_eggs:
#             max_eggs = green_eggs
#             max_color = "green"
#     elif color == "blue":
#         blue_eggs += 1
#         if blue_eggs > max_eggs:
#             max_eggs = blue_eggs
#             max_color = "blue"
#     elif color == "orange":
#         orange_eggs += 1
#         if orange_eggs > max_eggs:
#             max_eggs = orange_eggs
#             max_color = "orange"
#
# print(f"Red eggs: {red_eggs}")
# print(f"Orange eggs: {orange_eggs}")
# print(f"Blue eggs: {blue_eggs}")
# print(f"Green eggs: {green_eggs}")
# print(f"Max eggs: {max_eggs} -> {max_color}")

#Задача 6. Великденска украса


customers = int(input())
grand_total = 0

for _ in range(customers):
    command = input()
    current_bill = 0
    final_bill = 0
    product_counter = 0
    while command != "Finish":
        product = command
        if product == "basket":
            current_bill += 1.50
        elif product == "wreath":
            current_bill += 3.80
        elif product == "chocolate bunny":
            current_bill += 7
        product_counter += 1
        command = input()
    if product_counter % 2 == 0:
        final_bill = current_bill * 0.80
    else:
        final_bill = current_bill

    grand_total += final_bill

    print(f"You purchased {product_counter} items for {final_bill:.2f} leva.")
average_client_spend = grand_total / customers
print(f"Average bill per client is: {average_client_spend:.2f} leva.")