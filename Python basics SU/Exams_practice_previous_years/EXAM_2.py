# Задача 1. Машина за копаене

# from math import ceil
# video_card_price = int(input())
# transition_price = int(input())
# daily_electricity_consumption = float(input())
# daily_profit_per_card = float(input())
#
# other_components = 1000
#
# total_price_cards = 13 * video_card_price
# total_transition_price = 13 * transition_price
#
#
# total_cost = other_components + total_price_cards + total_transition_price
# daily_net_profit = daily_profit_per_card - daily_electricity_consumption
# total_daily_net_profit = 13 * daily_net_profit
#
# days_roi = total_cost / total_daily_net_profit
#
# print(total_cost)
# print(ceil(days_roi))

                     #Задача 2. Космически кораб


# width = float(input())
# length = float(input())
# height = float(input())
# astronauts_avg_height = float(input())
#
# spaceship_size = width  * length * height
# astronaut_room_size = 2 * 2 * (astronauts_avg_height + 0.40)
#
# astronauts_numbers = int(spaceship_size / astronaut_room_size)
#
# if 3 <= astronauts_numbers <= 10:
#     print(f"The spacecraft holds {astronauts_numbers} astronauts.")
# elif astronauts_numbers < 3:
#     print(f"The spacecraft is too small.")
# elif astronauts_numbers > 10:
#     print("The spacecraft is too big.")

                     #Задача 3. Компютърна зала

# Входът се чете от конзолата и съдържа точно 4 реда:
# • На първия ред - месецът - текст с възможности: "march", "april", "may", "june", "july", "august"
# • На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
# • На третия ред - броят на хората в групата - цяло число в диапазона [1...10]
# • На четвъртия ред - времето от деня – текст с възможности: "day" или "night"

# month = input()
# hours = int(input())
# number_people = int(input())
# day_or_night = input()
# price_per_hour = 0
# if day_or_night == "day":
#     if month == "march" or month == "april" or month == "may":
#         price_per_hour = 10.50
#         if number_people >= 4:
#             price_per_hour *= 0.90
#         if hours >= 5:
#             price_per_hour *= 0.50
#     elif month == "june" or month == "july" or month == "august":
#         price_per_hour = 12.60
#         if number_people >= 4:
#             price_per_hour *= 0.90
#         if hours >= 5:
#             price_per_hour *= 0.50
# elif day_or_night == "night":
#     if month == "march" or month == "april" or month == "may":
#         price_per_hour = 8.40
#         if number_people >= 4:
#             price_per_hour *= 0.90
#         if hours >= 5:
#             price_per_hour *= 0.50
#     elif month == "june" or month == "july" or month == "august":
#         price_per_hour = 10.20
#         if number_people >= 4:
#             price_per_hour *= 0.90
#         if hours >= 5:
#             price_per_hour *= 0.50
# total_visit_cost = number_people * price_per_hour * hours
#
# print(f"Price per person for one hour: {price_per_hour:.2f}")
# print(f"Total cost of the visit: {total_visit_cost:.2f}")


                                  # Задача 4. Котешка храна

# price_food_kg = 12.45
# cats = int(input())
# group1 = 0
# group2 = 0
# group3 = 0
# food_eaten_grams = 0
# for _ in range(cats):
#     food_grams = int(input())
#     if 100 <= food_grams < 200:
#         group1 += 1
#     elif 200 <= food_grams < 300:
#         group2 += 1
#     elif 300 <= food_grams < 400:
#         group3 += 1
#     food_eaten_grams += food_grams
# total_food_cost = (food_eaten_grams/1000) * price_food_kg
#
# print(f"Group 1: {group1} cats.")
# print(f"Group 2: {group2} cats.")
# print(f"Group 3: {group3} cats.")
# print(f"Price for food per day: {total_food_cost:.2f} lv.")


                      # Задача 5. Грижи за кученце

# food_bought_kg = int(input())
# command = input()
# food_bought_gr = food_bought_kg * 1000
# total_eaten_gr = 0
# while not command == "Adopted":
#     food_eaten_grams = int(command)
#     total_eaten_gr += food_eaten_grams
#     command = input()
# difference = abs(food_bought_gr - total_eaten_gr)
# if food_bought_gr >= total_eaten_gr:
#     print(f"Food is enough! Leftovers: {difference} grams.")
# else:
#     print(f"Food is not enough. You need {difference} grams more.")

                #Задача 6. Златна минa

# locations = int(input())
#
# for _ in range(locations):
#     average_daily_production = 0
#     all_days_sum_production = 0
#     expected_daily_gold_produce = float(input())
#     days_digging = int(input())
#     for days in range(days_digging):
#         daily_gold_production = float(input())
#         all_days_sum_production += daily_gold_production
#     average_daily_production = all_days_sum_production / days_digging
#     diff_expected_and_actual = expected_daily_gold_produce - average_daily_production
#     if average_daily_production >= expected_daily_gold_produce:
#         print(f"Good job! Average gold per day: {average_daily_production:.2f}.")
#     else:
#         print(f"You need {diff_expected_and_actual:.2f} gold.")



num = 13
dig = num % 3
print(dig)