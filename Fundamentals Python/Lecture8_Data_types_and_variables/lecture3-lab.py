         #1.	Concat Names

# first_name = input()
# second_name = input()
# delimiter = input()
# print(f"{first_name}{delimiter}{second_name}")

       # 2.	Convert Meters to Kilometers


# distance_in_meters = int(input())
# distance_in_kilometers = distance_in_meters / 1000
# print(f"{distance_in_kilometers:.2f}")


      #3.	Pounds to Dollars

# pounds = int(input())
# usd = pounds * 1.31
#
# print(f"{usd:.3f}")

                 #4.	Centuries to Minutes

# century = int(input())
#
# years = century * 100
# days = int(years * 365.2422)
# hours= days * 24
# minutes = hours * 60
#
# print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

                           #5.	Special Numbers


# num = int(input())
#
# for digit in range(1,num +1):
#     digit_as_str = str(digit)
#     digit_sum = 0
#     for current_digit in digit_as_str:
#         digit_sum +=int(current_digit)
#     is_special = False
#     if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#         is_special = True
#     print(f"{digit} -> {is_special} ")


                     #6.	Next Happy Year-    Проверка на различни цифри в число
                                                #да се намери следващата година, която няма повтаряща се цифра
#year = int(input())
# year_is_special = False
#
# while not year_is_special:
#       year += 1
#       year_as_str = str(year)
#       year_is_special = True
#       for digit in year_as_str:
#           if year_as_str.count(digit) > 1:
#               year_is_special = False
#               break
# print(year)

                # 6.1 използване на set()

# year = int(input())
# while True:
#     year += 1
#     year_as_string = str(year)
#     if len(year_as_string) == len(set(year_as_string)): # ако има повтарящо число, сет-а ще го отчете само веднъж и дължината на сета ще е по малко от стринга
#         break
# print(year)