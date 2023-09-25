# 1. Сумиране на секунди
import math
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
#
# total_time =time_third + time_second + time_first
# time_hour =total_time // 60
# time_minutes =total_time % 60
#
# if time_minutes <10:
#     print(f"{time_hour}:0{time_minutes}")
# else:
#     print(f"{time_hour}:{time_minutes}")

# 2. Бонус точки

# number = int(input())
# bonus_points =0
# extra_bonus =0
#
# if number <= 100 :
#     bonus_points = 5
# elif number <=1000 :
#     bonus_points = 0.2 * number
# else:
#     bonus_points = 0.1 * number
#
#
# if number % 2 == 0 :
#     extra_bonus = 1
# elif number % 10 == 5:
#     extra_bonus = 2
#
# total_bonus_points =bonus_points + extra_bonus
# total_number = total_bonus_points + number
#
# print(total_bonus_points)
# print(total_number)

# 3 Време + 15 минути

# hour = int(input())
# minutes = int(input())
#
# hour_in_minutes =hour * 60
# time = hour_in_minutes + minutes + 15
#
# hour = time // 60
# minutes =time % 60
#
# if hour >= 24 :
#     hour= hour -24
# if minutes <10 :
#     print(f"{hour}:0{minutes}")
# else:
#     print(f"{hour}:{minutes}")


#4. Магазин за детски играчки

# trip_price = float(input())
# puzzles = int(input())
# dolls = int(input())
# teddy_bears = int(input())
# mignons = int(input())
# truck_toys = int(input())
#
# number_of_toys = puzzles + dolls + teddy_bears + mignons + truck_toys
#
# puzzle_price = 2.60 * puzzles
# doll_price = 3 * dolls
# teddy_bear_price = 4.10 * teddy_bears
# mignon_price = 8.20 * mignons
# truck_toy_price = 2 * truck_toys
#
# sub_income =puzzle_price + doll_price + teddy_bear_price + mignon_price +truck_toy_price
#
# if number_of_toys >= 50:
#     sub_income -= sub_income * 0.25
#
# income =sub_income - (sub_income * 0.10)
#
# if income >= trip_price:
#     money_left = income - trip_price
#     print(f"Yes! {money_left:.2f} lv left.")
# else:
#     money_needed =trip_price - income
#     print(f"Not enough money! {money_needed:.2f} lv needed.")


#5. Годзила срещу Конг

# budget = float(input())
# number_stunts = int(input())
# price_cloths_per_stunt = float(input())
#
# decor_cost =budget * 0.10
# stunts_cost = number_stunts * price_cloths_per_stunt
#
# if number_stunts > 150:
#     stunts_cost -= stunts_cost * 0.10
#
# total_cost = decor_cost + stunts_cost
# difference = abs(budget - total_cost)
# if total_cost > budget:
#     #money_needed= total_cost - budget
#     print("Not enough money!")
#     print(f"Wingard needs {difference:.2f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {difference:.2f} leva left.")


#6. Световен рекорд по плуване

# world_record_seconds = float(input())
# distance_meters = float(input())
# time_per_meter_seconds = float(input())
#
# delays_seconds =12.5 * math.floor(distance_meters // 15)
#
# ivan_time = distance_meters * time_per_meter_seconds + delays_seconds
#
# if world_record_seconds > ivan_time:
#     print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
# else:
#     difference =ivan_time - world_record_seconds
#     print(f"No, he failed! He was {difference:.2f} seconds slower.")

#7. Пазаруване
#
# budget = float(input())
# number_video_card = int(input())
# number_processor = int(input())
# number_ram = int(input())
#
# video_card = 250
# processor = 0.35 * number_video_card * video_card
# ram = 0.10 * number_video_card * video_card
#
# total_cost = number_video_card * video_card + \
#              number_processor * processor + \
#              number_ram * ram
# if number_video_card > number_processor:
#     total_cost -= total_cost * 0.15
#
# difference = abs(budget - total_cost)
#
# if budget >= total_cost:
#     print(f"You have {difference:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {difference:.2f} leva more!")


#8. Обедна почивка

name_of_serries =input()
episode_lenght =int(input())
break_lenght =int(input())


time_for_lunch = 1/8 * break_lenght
time_for_break = 1/4 * break_lenght

time_needed =time_for_lunch + time_for_break + episode_lenght

difference = math.ceil(abs(break_lenght - time_needed))

if break_lenght >= time_needed:
    print(f"You have enough time to watch {name_of_serries} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serries}, you need {difference} more minutes.")









