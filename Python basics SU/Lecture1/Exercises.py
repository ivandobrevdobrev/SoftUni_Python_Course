# # USDto BGN
# #1 USD = 1.79549 BGN

# usd= float(input())
# coversion =usd * 1.79549
# print(coversion)


#Zadacha2- Radians to dregrees
# градус = радиан * 180 / π. Числото π в Python м
# from math import pi
#
# radians = float(input())
# deregrees = radians * 180/pi
#
# print(deregrees)

#Zadacha 3 - Deposits

# deposit_amount = float(input())
# period_months = int(input())
# interest_rate =float(input())/100
# final_amount  =deposit_amount + period_months * ((deposit_amount * interest_rate)/12)
# print(final_amount)

#Zadacha 4 - Literature

# pages_book = int(input())
# pages_per_hour =int(input())
# days =int(input())
#
# total_hours_needed =pages_book / pages_per_hour
# daily_hours =total_hours_needed / days
#
# print(int(daily_hours))

#Zadacha 5 - Uchebni Materiali

# pens =int(input())
# markers =int(input())
# liters_cleaner =int(input())
# discount_percent =int(input())
#
# sum_pens =pens * 5.80
# sum_markers =markers * 7.20
# sum_liters_cleaner =liters_cleaner * 1.20
# sub_total =sum_pens + sum_markers + sum_liters_cleaner
# total_average = sub_total-(sub_total * discount_percent / 100)
#
# print(total_average)

#Zadacha 6 - Painting


# nylon_m2 = int(input())
# paint_liters = int(input())
# diluent = int(input())
# hours = int(input())
#
# total_nylon = nylon_m2 * 1.50 + 2*1.5
# total_diluent =diluent * 5
# total_paint_liters = paint_liters * 14.50 + (paint_liters * 14.50 * 0.10)
# bags =0.40
# price_per_hour_work =(total_nylon + total_diluent + total_paint_liters + bags) * 0.30
# total_hour_price =hours * price_per_hour_work
#
# total_amount_expenses =(total_nylon + total_diluent
#                         +total_paint_liters
#                         +bags
#                         +total_hour_price)
#
# print(total_amount_expenses)


#Zadacha 7- Food delivery

# number_chicken_menues = int(input())
# number_fish_menues = int(input())
# number_veggie_menues = int(input())
#
#
# price_chicken = 10.35 * number_chicken_menues
# price_fish = 12.40 * number_fish_menues
# price_veggie = 8.15 * number_veggie_menues
# price_desert = 0.20 * (price_veggie + price_fish +price_chicken)
# price_delivery = 2.50
#
# order_price =(price_delivery + price_desert + price_fish + price_chicken + price_veggie)
#
# print(order_price)

#Zadacha 8 - baskeball field

# annual_fee = int(input())
#
# shoes =annual_fee -(annual_fee * 0.40)
# clothes = shoes - (shoes * 0.20)
# ball = 0.25 * clothes
# accessories =0.20 * ball
#
# total_average = annual_fee +shoes + clothes + ball + accessories
#
# print(total_average)

#Zadacha 9 Accuarium

lenght = int(input())
width = int(input())
high = int(input())
percent = float(input())

figure_m3_in_dcm =lenght * width * high / 1000 # Kubik na paralelepiped = a*b*c -> deleno na 1000 dava v decimeter

#/ 1л=1 дм3/.
liters = figure_m3_in_dcm - percent * figure_m3_in_dcm /100

print(liters)
