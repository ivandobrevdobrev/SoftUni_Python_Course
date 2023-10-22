# gifts = ["eggs","apple","bread",5]
#
# for index in range(len(gifts)):
#     print("- " + gifts[index])
# #print(gifts)
# print("\n- ".join(gifts))

# price = 100.56
# sell_price = 0
#
# sell_price += price*.40
# print(round(sell_price))
#
# num = 2.51738
# print(round(num,2))

# new_prices = [2,3]
# budget = 10
# final_budget = budget + sum(new_prices)
# print(final_budget)

#Functions
# a=5
# b=4
# def sum_num(a:int,b:int):
#     return a+b
# print(sum_num(a,b))


# def is_even (n):
#     return n % 2 == 0   # създаваме функ, която да връща само Четни числа
#numbers = [1,2,3,4,5,6]
# even_numbers = list(filter(is_even,numbers)) #  съсздаваме нов лист, с filter казваме да се ползва Функ, с числата от Numbers
# print(even_numbers)

# numbers = list(map(int,input().split(", ")))
# print(numbers)

# def greet(name):
#     return f"Hello,{name}"
# greet("Maria")
# print(greet("Maria"))


# def print_nums_from_1_to_n(n):
#     """this some explanation
#     bla, bla , bla """
#     for num in range(1,n+1):
#         print(num,end=" ")
# #print_nums_from_1_to_n(5)
# help(print_nums_from_1_to_n)

# def calculate (a,b):
#     if b == 0:
#         return "Error"
#     else :
#         return a + b
# print(calculate(5,0))

#LAMBDA

# add = lambda a,b: a+b
# print(add(5,4))

# word = "ivan"
# new = list(word)
#
# for i in range(len(new)+1):
#     print(i)

# list =['app','ben','car']
#
# a = list.index("car")
# print(a)