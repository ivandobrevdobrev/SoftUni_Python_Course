
# # for i in range(1,10,2):
# #   print(i)        # printira sys stypka 2, prez 2
#
# for i in range(10):
#     print(i)   # printira ot 0 do 9

# for number in range (10,1,-1): # printira naobratno ot 10 do 2
#     print(number)

# for number in range (10,0,-1): # printira naobratno ot 10 do 1
#     print(number)

             # zadacha 1
# for number in range(1, 10):
#      print(number)

         #Zadacha 2
# number = int(input())
# for current_number in range(1, number + 1,3):
#     print(current_number)

        # 3.Четни степени на 2

# number = int(input())
# for power in range(0, number + 1,2):
#     print(2 ** power)

     #4. Числата от N до 1 в обратен ред

# number = int(input())
# for current_number in range(number, 0,-1):
#     print(current_number)

# text = "softuni"
# length = len(text)
# print(length)

                          # Obhojdane na String

#text = "softuni"
# for index in range (0,len(text)):
#     print(text[index])

# text = input()
# for index in text :          кратък вариант
#    print(index)

                   #6. Сумиране на гласните букви

# буква a e i o u

# стойност 1 2 3 4 5


# text = input()
# sum_of_vowls = 0
#
# for index in range (len(text)):         #ili 2 variant :    for index in text:
#     if text[index] == "a":              #                       if index == "a"
#         sum_of_vowls +=1                  #                       sum_of_vowls +=1
#     elif text[index] == "e":
#         sum_of_vowls +=2
#     elif text[index] == "i":
#         sum_of_vowls +=3
#     elif text[index] == "o":
#         sum_of_vowls +=4
#     elif text[index] == "u":
#         sum_of_vowls +=5
# print(sum_of_vowls)

# text ="softuni"
# for i in range(len(text)):
#  print(f" index {i}, symbol is {text[i]}")

                  # ENUMERATE - pokazva Indeksa i samiq simvol
# some_string = "Ivan"
# for index, character in enumerate(some_string):
#     print(f"index {index}, symbol is {character}")

              #7. Сумиране на числа

# numbers = int(input())
# sum = 0
# for i in range(numbers):
#     current_num = int(input())
#     sum += current_num
# print(sum)

         #8. Редица цели числа

# import sys
# count_of_numbers = int(input())
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for number in range(count_of_numbers):
#     current_num = int(input())
#     if current_num > max_number:
#         max_number = current_num
#     if current_num < min_number:
#         min_number = current_num
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

                           #9. Лява и дясна сума
                          # Solution 1
# n = int(input())
# left_sum = 0
# right_sum = 0
#
# for i in range (n):
#     left_sum += int(input())
#
# for i in range (n):
#     right_sum += int(input())
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")


             # Solution 2

# count_of_numbers = int(input())
# left_sum = 0
# right_sum = 0
# for numbers in range(count_of_numbers * 2):
#     current_number = int(input())
#     if numbers < count_of_numbers:
#         left_sum += current_number
#     else:
#         right_sum += current_number
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     difference = abs(left_sum - right_sum)
#     print(f"No, diff = {difference}")



                              #10. Четна / нечетна сума

# count_of_numbers = int(input())
# even_sum = 0
# odd_sum = 0
# for index in range(count_of_numbers):
#     current_num = int(input())
#     if index % 2 == 0:
#         even_sum += current_num
#     else:
#         odd_sum += current_num
# if even_sum == odd_sum:
#     print(f"Yes\nSum = {even_sum}")
# else:
#     diff= abs(even_sum - odd_sum)
#     print(f"No\nDiff = {diff}")

