# 1. Ден от седмицата

# day_of_the_week =int(input())
#
# if day_of_the_week == 1:
#     print("Monday")
# elif day_of_the_week == 2 :
#     print("Tuesday")
# elif day_of_the_week ==3:
#     print("Wednesday")
# elif day_of_the_week ==4 :
#     print("Thursday")
# elif day_of_the_week ==5 :
#     print("Friday")
# elif day_of_the_week ==6 :
#     print("Saturday")
# elif day_of_the_week ==7 :
#     print("Sunday")
# else:
#     print("Error")

# 2. Почивен или работен ден

# day_of_the_week = input()
#
# if day_of_the_week == "Monday" \
#     or day_of_the_week == "Tuesday"\
#     or day_of_the_week == "Wednesday"\
#     or day_of_the_week == "Thursday"\
#     or day_of_the_week == "Friday":
#     print("Working day")
# elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
#     print("Weekend")
# else:
#     print("Error")

# 3. Клас животно

# animal =input()
#
# if animal == "dog":
#     print("mammal")
# elif animal == "crocodile" \
#         or animal == "tortoise" \
#         or animal == "snake":
#     print("reptile")
# else:
#     print("unknown")

# 4. Обръщение според възраст и пол

# age =float(input())
# gender = input()
#
# if gender == "m":
#     if age >= 16:
#         print("Mr.")
#     else:
#         print("Master")
# if gender == "f":
#     if age >= 16:
#         print("Ms.")
#     else:
#         print("Miss")

# 5. Квартално магазинче

# product = input()
# city  = input()
# quantity = float(input())
# price= 0
# if city == "Sofia":
#     if product == "coffee":
#         price = 0.5
#     elif product == "water":
#         price = 0.80
#     elif product == "beer":
#         price = 1.20
#     elif product == "sweets":
#         price = 1.45
#     elif product == "peanuts":
#         price = 1.60
# elif city == "Plovdiv":
#     if product == "coffee":
#         price = 0.40
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.15
#     elif product == "sweets":
#         price = 1.30
#     elif product == "peanuts":
#         price = 1.50
# elif city == "Varna":
#     if product == "coffee":
#         price = 0.45
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.10
#     elif product == "sweets":
#         price = 1.35
#     elif product == "peanuts":
#         price = 1.55
#
# final_price =price * quantity
#
# print(final_price)

# 6. Число в интервалa

# number = int(input())
#
# if (number >= -100 and number <= 100) and number != 0:
#     print("Yes")
# else:
#     print("No")

# 7. Работно време

# hour =int(input())
# day_of_the_week = input()
#
# if 10<= hour <= 18:
#     if day_of_the_week == "Monday":
#         print("open")
#     elif day_of_the_week == "Tuesday":
#         print("open")
#     elif day_of_the_week == "Wednesday":
#         print("open")
#     elif day_of_the_week == "Thursday":
#         print("open")
#     elif day_of_the_week == "Friday":
#         print("open")
#     elif day_of_the_week == "Saturday":
#         print("open")
#     else:
#         print("closed")
# else:
#     print("closed")

# 8. Билет за кино

# day_of_the_week = input()
# price = 0
# if day_of_the_week == "Monday" \
#         or day_of_the_week == "Tuesday" \
#         or day_of_the_week == "Friday":
#     price = 12
# elif day_of_the_week == "Wednesday" \
#         or day_of_the_week == "Thursday":
#     price = 14
# elif day_of_the_week == "Saturday" \
#         or day_of_the_week == "Sunday":
#     price =16
#
# print(price)

# 9. Плод или зеленчук

# product = input()
#
# if product == "banana" \
#         or product == "apple" \
#         or product == "kiwi" \
#         or product == "cherry" \
#         or product == "lemon" \
#         or product == "grapes":
#     print("fruit")
# elif product == "tomato" \
#         or product == "cucumber" \
#         or product == "pepper" \
#         or product == "carrot" :
#     print("vegetable")
# else:
#     print("unknown")

# 10. Невалидно число

# number = int(input())
#
# if (number < 100 or number > 200) and number != 0:
#     print("invalid")


# 11. Магазин за плодове

# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
#
# price = 0
#
# if day_of_the_week == "Monday" \
#          or day_of_the_week == "Tuesday" \
#          or day_of_the_week == "Wednesday"\
#          or day_of_the_week == "Thursday"\
#          or day_of_the_week == "Friday":
#     if fruit == "banana":
#         price = 2.5
#     elif fruit == "apple":
#         price = 1.2
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.7
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#
# elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#
# final_price = price * quantity
# if price == 0:
#     print("error")
# else:
#     print(f"{final_price:.2f}")


# 12. Търговски комисионни

city = input()
sales = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
total_commission = commission * sales

if total_commission == 0:
    print("error")
else:
    print(f"{total_commission:.2f}")
