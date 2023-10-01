# a = "hello"
#
# if a.isupper():
#     print("yes")
# else:
#     print("lower")

#---------------------

# word ="coding"
# sliced_word = word[0:5] #или word[:5] result is "codin" ,5ия индекс не се взима
# sliced_word_2 = word[2:] #result is "ding" , започва от 2рия индекс до края
# sliced_word_3 = word[0::2] #reslut is "cdn", започва от 0 до края със стъпка 2
# #word[start:end:step]
# sliced_word_2 = word[::] #отначало до края
# print(sliced_word)
# print(sliced_word_2)
# print(sliced_word_3)


#---------------- Set()
# my_text ="iivannov"
# my_new_set = {"ajsdh", "asfja", "afa"}  #creating a set
#
# print(my_new_set)
# print(set(my_text))  #covert my_text as a set and print , result : {'o', 'a', 'v', 'n', 'i'} only single unique symbols

#---------------- COUNT()

# text = "112356"
# print(text.count("1"))   връща 2 , защото 1 го има 2 пъти в стринга

#ASCII

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


#Lists

# data_list = [10, 3.14, 'hello',{"name": 'ivan', "age": 32}, True, False]

# text = "a b c d"
#
# split_text = text.split(" ")
# print(split_text)

# my_list = ["a","b","c"]
# print("-".join(my_list))

#my_list = ["cucumber","bear","apple","Apple"]
# my_list.sort()
# print(my_list)

my_list = [2,3,4,1,5,1]
#print(my_list.index(5,2))
# popped_element = my_list.pop(3)
# print(my_list)

# my_list.extend([100,101])
# print(my_list)

#my_list = [1,2,3,4,5,6,7,8]
#print(my_list[::-2])

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

#print( 2 in my_list) - -> True - проверява дали числото 2 е в листа

#print(*my_list) принтира лист без запетаи и кавички - разкомплектова го

for num in my_list:
    print(num, end=", ")