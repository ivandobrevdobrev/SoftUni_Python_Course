# 1. Числа до 1000, завършващи на 7

# Solution 1
# for i in range(1, 1000):
#     if i % 10 == 7:
#         print(i)

# Solution 2

# for i in range(7, 1000, 10):
#     print(i)

# 2. Елемент, равен на сумата на останалите

# import sys
#
# count_of_numbers =int(input())
# max_num = -sys.maxsize
# sum_numbers = 0
#
# for i in range(count_of_numbers):
#     current_num = int(input())
#     sum_numbers += current_num
#     if current_num > max_num:
#         max_num = current_num
#
# sum_numbers = sum_numbers - max_num
# difference = abs(max_num - sum_numbers)
# if sum_numbers == max_num:
#     print(f"Yes\nSum = {max_num}")
# else:
#     print(f"No\nDiff = {difference}")


# 3. Хистограма

# count_of_numbers =int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
#
# for i in range(count_of_numbers):
#     current_num = int(input())
#     if current_num < 200:
#         p1 += 1
#     elif 200 <= current_num <= 399:
#         p2 += 1
#     elif 400 <= current_num <= 599:
#         p3 += 1
#     elif 600 <= current_num <= 799:
#         p4 += 1
#     elif current_num >= 800:
#         p5 += 1
# p1 = p1 / count_of_numbers * 100
# p2 = p2 / count_of_numbers * 100
# p3 = p3 / count_of_numbers * 100
# p4 = p4 / count_of_numbers * 100
# p5 = p5 / count_of_numbers * 100
# print(f"{p1:.2f}%")
# print(f"{p2:.2f}%")
# print(f"{p3:.2f}%")
# print(f"{p4:.2f}%")
# print(f"{p5:.2f}%")

# 4. Умната Лили

# age = int(input())
# price_washing_machine = float(input())
# single_toy_price = int(input())
# toys_num = 0
# money = 0
# even=0
# for birthdays in range(1,age+1):
#     if birthdays % 2 == 0:
#         even += 1
#         money += even * 10 -1
#     else:
#         toys_num += 1
# available_funds = money + (toys_num * single_toy_price)
# difference = abs(available_funds - price_washing_machine)
#
# if available_funds >= price_washing_machine:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")


# 5. Заплата - Използване на BREAK

# count_of_tabs = int(input())
# salary = float(input())
#
# fine = 0
# difference = salary - fine
# for i in range(count_of_tabs):
#     website = input()
#     if website == "Facebook":
#         fine += 150
#         if fine >= salary:
#             print("You have lost your salary.")
#             break
#     if website == "Instagram":
#         fine += 100
#         if fine >= salary:
#             print("You have lost your salary.")
#             break
#     if website == "Reddit":
#         fine += 50
#         if fine >= salary:
#             print("You have lost your salary.")
#             break
# difference = salary - fine
# if salary > fine:
#     print(int(difference))

# 6. Оскари

# actor = input()
# initial_points = float(input())
# number_of_assessors = int(input())
# total_points = initial_points # правим нова променлива за дя я манимпулираме по надолу , и да запазим initial points ст-ста
#
# for i in range(number_of_assessors):
#     assessor = input()
#     points_from_assessor = float(input())
#     total_points += len(assessor) * points_from_assessor / 2
#     if total_points > 1250.5:
#         break
#
# if total_points > 1250.5:
#     print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
# else:
#     print(f"Sorry, {actor} you need {1250.5 - total_points:.1f} more!")


# 7. Трекинг мания

# groups = int(input())
# musala_group = 0
# montblanc_group = 0
# kilimanjaro_group = 0
# k2_group = 0
# everest_group = 0
# total_people = 0
#
# for i in range(groups):
#     people_in_group = int(input())
#     total_people += people_in_group
#     if people_in_group <=5:
#         musala_group += people_in_group
#     elif  6<= people_in_group <= 12:
#         montblanc_group += people_in_group
#     elif  13 <= people_in_group <= 25:
#         kilimanjaro_group += people_in_group
#     elif  26<= people_in_group <= 40:
#         k2_group += people_in_group
#     elif people_in_group >= 41:
#         everest_group += people_in_group
#
# musala_group = musala_group / total_people *100
# montblanc_group = montblanc_group / total_people *100
# kilimanjaro_group = kilimanjaro_group / total_people *100
# k2_group = k2_group / total_people *100
# everest_group = everest_group / total_people *100
#
# print(f"{musala_group:.2f}%")
# print(f"{montblanc_group:.2f}%")
# print(f"{kilimanjaro_group:.2f}%")
# print(f"{k2_group:.2f}%")
# print(f"{everest_group:.2f}%")

                                  # 8. Световна ранглиста по тенис

# tournaments = int(input())
# initial_points = int(input())
# total_points = initial_points
# wins = 0
# for i in range(tournaments):
#     stage_won = input()
#     if stage_won == "W":
#         total_points += 2000
#         wins += 1
#     elif stage_won == "F":
#         total_points += 1200
#     elif stage_won == "SF":
#         total_points += 720
#
# average_points = int((total_points - initial_points) / tournaments)
# percent_wins = wins / tournaments * 100
#
# print(f"Final points: {total_points}")
# print(f"Average points: {average_points}")
# print(f"{percent_wins:.2f}%")
