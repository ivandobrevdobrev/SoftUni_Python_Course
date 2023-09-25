# 1. Рожден ден

# • Торта – цената ѝ е 20% от наема на залата
# • Напитки – цената им е 45% по-малко от тази на тортата
# • Аниматор – цената му е 1/3 от цената за наема на залата

# rent = float(input())
#
# cake = rent * 0.20
# drinks = cake * (1-0.45)
# animation = rent / 3
#
# total_expenses = cake +drinks + animation +rent
# print(total_expenses)

# Задача 1. Change бюро


# 1 биткойн = 1168 лева.
#  1 китайски юан = 0.15 долара.
#  1 долар = 1.76 лева.
#  1 евро = 1.95 лева.

# Обменното бюро има комисионна от 0 до 5 процента от крайната сума в евро

# bitcoin = int(input())
# chinese = float(input())
# commision = float(input())
#
# bitcoin_leva = 1168 * bitcoin
# chinese_dollar = 0.15  * chinese
# dollar_leva = chinese_dollar * 1.76
#
# euro = (bitcoin_leva + dollar_leva) / 1.95
# commision = euro * commision/100
# total_euro = euro - commision
#
# print (f"{total_euro:.2f}")

# Задача 2. Котешка разходка

# На първия ред - минути разходка на ден - цяло число в интервала [1...50]
#  На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
#  На третия ред - приетите от котката калории на ден – цяло число в интервала [100…4000]

# За всяка минута от разходката,
# котката гори по 5 калории. Разходката е достатъчна, ако котката изграря 50% от приетите калории.

# minutes_walking = int(input())
# daily_walks = int(input())
# daily_calories = int(input())
#
# total_minutes_walking = minutes_walking * daily_walks
# total_calories_burned = total_minutes_walking * 5
#
# if total_calories_burned >= (0.5 * daily_calories):
#     print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
# else:
#     print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")


# Задача 2. Скоростно изкачване


# наклона на терена го забавя на всеки 50 м. с 30 секунди. Да се изчисли
# времето в секунди, за което Георги ще изкачи разстоянието до върха и разликата спрямо рекорда.
# Когато се изчислява колко пъти Георги ще се забави в резултат на наклона на терена, резултатът трябва да
# се закръгли надолу до най-близкото цяло число.

# import math
# record_seconds = float(input())
# distance_meters = float(input())
# seconds_per_meter = float(input())
#
# george_climb_seconds = distance_meters * seconds_per_meter
# slowing_seconds = math.floor(distance_meters/50)*30
# geogre_record = george_climb_seconds + slowing_seconds
# difference = (abs(record_seconds - geogre_record))
# if geogre_record < record_seconds:
#     print(f"Yes! The new record is {(geogre_record):.2f} seconds.")
# else:
#     print(f"No! He was {difference:.2f} seconds slower.")


# Задача 3. Енергийни гелове

#                 Диня          Манго           Ананас          Малина
# 2 броя (small) 56 лв./бр.    36.66 лв./бр.   42.10 лв./бр.   20 лв./бр.
# 5 броя (big)   28.70 лв./бр. 19.60 лв./бр.   24.80 лв./бр.   15.20 лв./бр.

# fruit = input()
# size_set = input()
# set_orders = int(input())
# price = 0
#
# if fruit == "Watermelon":
#     if size_set == "small":
#         price = set_orders * 56 * 2
#     elif size_set == "big":
#         price = set_orders * 28.70 * 5
# elif fruit == "Mango":
#     if size_set == "small":
#         price = set_orders * 36.66 * 2
#     elif size_set == "big":
#         price = set_orders * 19.60 * 5
# elif fruit == "Pineapple":
#     if size_set == "small":
#         price = set_orders * 42.10 * 2
#     elif size_set == "big":
#         price = set_orders * 24.80 * 5
# elif fruit == "Raspberry":
#     if size_set == "small":
#         price = set_orders * 20.00 * 2
#     elif size_set == "big":
#         price = set_orders * 15.20 * 5
#
# if 400<= price <= 1000:
#     price -= price * 0.15
# elif price > 1000 :
#     price = price * 0.5
#
# print(f"{price:.2f} lv.")

# Задача 3. Карта за фитнес


# Gym Boxing Yoga Zumba Dances Pilates
# $35 $37 $42 $31 $53 $37
# available_sum = float(input())
# gender = input()
# age = int(input())
# sport = input()
# needed_sum = 0
#
# if gender == "m":
#     if sport == "Gym":
#         needed_sum = 42
#     elif sport == "Boxing":
#         needed_sum = 41
#     elif sport == "Yoga":
#         needed_sum = 45
#     elif sport == "Zumba":
#         needed_sum = 34
#     elif sport == "Dances":
#         needed_sum = 51
#     elif sport == "Pilates":
#         needed_sum = 39
# elif gender == "f":
#     if sport == "Gym":
#         needed_sum = 35
#     elif sport == "Boxing":
#         needed_sum = 37
#     elif sport == "Yoga":
#         needed_sum = 42
#     elif sport == "Zumba":
#         needed_sum = 31
#     elif sport == "Dances":
#         needed_sum = 53
#     elif sport == "Pilates":
#         needed_sum = 37
#
# if age <= 19:
#     needed_sum = needed_sum * 0.80
# difference = abs(available_sum - needed_sum)
# if available_sum >= needed_sum:
#     print(f"You purchased a 1 month pass for {sport}.")
# else:
#     print(f"You don't have enough money! You need ${difference:.2f} more.")


# Задача 4. Храна за домашни любимци


# days = int(input())
# quantity_food = float(input())
# total_dog_food = 0
# total_cat_food = 0
# biscuits = 0
# total_biscuits = 0
# for day in range(1,days+1 ):
#     daily_dog_food = int(input())
#     daily_cat_food = int(input())
#     if day % 3 == 0:
#         biscuits = 0.10*(daily_dog_food + daily_cat_food)
#         total_biscuits += biscuits
#     total_dog_food += daily_dog_food
#     total_cat_food += daily_cat_food
# percent_eaten_food = (total_cat_food + total_dog_food) / quantity_food * 100
# percent_eaten_food_dog = total_dog_food / (total_cat_food + total_dog_food) * 100
# percent_eaten_food_cat = total_cat_food / (total_cat_food + total_dog_food) * 100
#
# print(f"Total eaten biscuits: {total_biscuits:.0f}gr.")
# print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
# print(f"{percent_eaten_food_dog:.2f}% eaten from the dog.")
# print(f"{percent_eaten_food_cat:.2f}% eaten from the cat.")


# Задача 4. Трекинг мания - решена е  в Лекция 4- упражнения

                   # Задача 5. Товарене на багажи

# free_capacity = float(input())
# command = input()
# counter_suitcase = 0
# while not command == "End":
#     size_suitcase = float(command)
#     counter_suitcase += 1
#     if counter_suitcase % 3 == 0 and counter_suitcase != 0:
#         size_suitcase *= 1 + 0.10
#     if free_capacity < size_suitcase:
#         counter_suitcase -=1
#         break
#     free_capacity -= size_suitcase
#     command = input()
#
# if command == "End":
#     print(f"Congratulations! All suitcases are loaded!")
# else:
#     print("No more space!")
# print(f"Statistic: {counter_suitcase} suitcases loaded.")


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


# Задача 6. Коледен турнир


# days = int(input())
# total_won_money = 0
# total_won_games = 0
# total_lost_games = 0
#
# for num in range(1, days + 1):
#     command = input()
#     money_won = 0
#     won_games = 0
#     lost_games = 0
#     while not command == "Finish":
#         sport = command
#         result = input()
#         if result == "win":
#             money_won += 20
#             won_games += 1
#         elif result == "lose":
#             lost_games += 1
#         command = input()
#     if won_games > lost_games:
#         money_won *= 1.10
#     total_won_money += money_won
#     total_won_games += won_games
#     total_lost_games += lost_games
#
# if total_won_games > total_lost_games:
#     total_won_money *= 1.20
#     print(f"You won the tournament! Total raised money: {total_won_money:.2f}")
# elif total_won_games < total_lost_games:
#     print(f"You lost the tournament! Total raised money: {total_won_money:.2f}")


