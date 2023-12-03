import re

text = input()
pattern = r'([#|])([A-Za-z\s]+)(\1)(\d{2}+\/\d{2}\/\d{2})(\1)(\d+)(\1)'

matches = re.findall(pattern,text)
total_calories = sum([int(match[5]) for match in matches]) # обикаляме Тюпъла и взимаме Калориите , които са на индекс 5 и после ги сумираме

days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")


# Това решение минава в Judge, тука специалните символи # | не ги групираме( само в началото)

# import re
# foods = input()
# pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
#
# match = re.findall(pattern, foods)
# total_calories = sum([int(calorie[3]) for calorie in match])
# days = total_calories // 2000
#
# print(f"You have food to last you for: {days} days!")
#
# for index in match:
#     food = index[1]
#     expiration_date = index[2]
#     calories = int(index[3])
#
#     print(f"Item: {food}, Best before: {expiration_date}, Nutrition: {calories}")