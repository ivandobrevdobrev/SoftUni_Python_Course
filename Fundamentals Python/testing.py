# a = "hello"
#
# if a.isupper():
#     print("yes")
# else:
#     print("lower")

# ---------------------

# word ="coding"
# sliced_word = word[0:5] #или word[:5] result is "codin" ,5ия индекс не се взима
# sliced_word_2 = word[2:] #result is "ding" , започва от 2рия индекс до края
# sliced_word_3 = word[0::2] #reslut is "cdn", започва от 0 до края със стъпка 2
# #word[start:end:step]
# sliced_word_2 = word[::] #отначало до края
# print(sliced_word)
# print(sliced_word_2)
# print(sliced_word_3)


# ---------------- Set()
# my_text ="iivannov"
# my_new_set = {"ajsdh", "asfja", "afa"}  #creating a set
#
# print(my_new_set)
# print(set(my_text))  #covert my_text as a set and print , result : {'o', 'a', 'v', 'n', 'i'} only single unique symbols

# ---------------- COUNT()

# text = "112356"
# print(text.count("1"))   връща 2 , защото 1 го има 2 пъти в стринга

# ASCII

# symbol = "M"
# print(ord(symbol))
# number = 75
# print(chr(number))

# number = 10
# res = number % 3
# print(res)


# year = int(input())
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


# Lists

# data_list = [10, 3.14, 'hello',{"name": 'ivan', "age": 32}, True, False]

# text = "a b c d"
#
# split_text = text.split(" ")
# print(split_text)

# my_list = ["a","b","c"]
# print("-".join(my_list))

# my_list = ["cucumber","bear","apple","Apple"]
# my_list.sort()
# print(my_list)

# my_list = [2,3,4,1,5,1]
# print(my_list.index(5,2))
# popped_element = my_list.pop(3)
# print(my_list)

# my_list.extend([100,101])
# print(my_list)

# my_list = [1,2,3,4,5,6,7,8]
# print(my_list[::-2])

# for number in my_list:
#     print(number, end=" ")

# search_element = 3
#
# for element in my_list:
#     if element == search_element:
#         print(f"found the number {my_list[element]}")
#         break
# else:
#     print("not found")

# print( 2 in my_list) - -> True - проверява дали числото 2 е в листа

# print(*my_list) принтира лист без запетаи и кавички - разкомплектова го

# for num in my_list:
#     print(num, end=", ")


# Zadacha 9
# items = input().split("|")
# budget = float(input())
# final_budget = 0
# ticket_price = 150
# new_prices = []
# profit = 0
# sell_price = 0
#
#
# for item in items:
#     current_item = item.split("->")
#
#     if current_item[0] == "Clothes":
#         if float(current_item[1]) <= 50.00:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
#     elif current_item[0] == "Shoes":
#         if float(current_item[1]) <= 35.00:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
#     elif current_item[0] == "Accessories":
#         if float(current_item[1]) <= 20.50:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
# final_budget = budget + sum(new_prices)
#
# for new_price in new_prices:
#     print(f"{new_price:.2f}", end=" ")
# print()
#
# print(f"Profit: {profit:.2f}")
# if final_budget >= ticket_price:
#     print("Hello, France!")
# else:
#     print("Not enough money.")

# # операции с числа на даден индекс от лист
#
# my_list = [2, 3, 4, 8, 5, 1]
# index1 = 1
# index2 = 4
# if index1 in range(len(my_list)) and index2 in range(len(my_list)):  # проверявам дали идексите са валидни в листа
#
#     for i in range(index1, index2 + 1):  # намалям числата (от индекс 1 до 4 вкл) с 1
#         my_list[i] -= 1
#
# print(my_list)  # -->  [2, 2, 3, 7, 4, 1]


#some_words =["Medallion", "Cup", "Gold", "silver", "titanium"]
# num = 3
# print(some_words[-1:-(num+1):-1])
#
# for i in range(3):
#     some_words.pop()
# print(some_words)


my_list = [2, 3, 4, 8, 4, 1]
# my_list =[num-1 for num in my_list]
# print(my_list)
# number = 3
# index = 2
# if number < len(my_list[index+1:]):  проверка на индекс(число) дали го има в част от лист
#     print("ok")
# else:
#     print(len(my_list[index+1:]))
# if 7 in my_list:
#     my_list.remove(7)
# else:print("no")

# for num in my_list:
#     if num < 5:
#         my_list.remove(num)
# print(*my_list)

# Последния елемент
# last =my_list[-1]
# print(last)

# first = my_list[0]
# my_list.pop(-1)
# my_list.insert(-1,first)
# print(my_list)

# lesson = "list"
# exersice = lesson + "-Exercise"
# print(exersice)

# some_string = "Ivan"
# for index, character in enumerate(some_string,1):
#    print(f"index {index}, symbol is {character}")
#
# if some_string[0] == "I":
#    print("yes")

#добавяне на символ между другите

#some_string = "Ivan"
# index = 2
# value = "G"
# some_string = some_string[:index]+ value + some_string[index:]
# print(some_string)

#moving first symbols to end fo rthe string
# some_string = some_string[index:] + some_string[:index]
# print(some_string)


# string = "Ivann is tenn"
# print(string.replace("n","F"))

# activation_key = 'absuyrghkdteruu'
# start = 3
# end = 8
# uppers = activation_key[start:end]
# print(uppers.upper())


# word = 'Shy'
# suma = sum([ord(symbol) for symbol in word])
# print(suma)

# Remove part of a string only one occurrence and add its reversed version at the end
# string = "Ivan is in the van"
# substring = "van"
# new_substring = substring[::-1]
# string = string.replace(substring,"",1) + new_substring
# print(string)


# text = "computerIsfinepute"
# index = 3
# length = 4
# sub = text[index:index+length]
# print(sub)
# text = text.replace(sub,"",1)
# print(text)

# a = 5
# b = a > 10
# if not a:
#     print(a)
# if b:
#     print(b)


