

numbers_as_string = input().split()
numbers_integers = []

for numbers in numbers_as_string:
    numbers_integers.append(int(numbers))

is_even = lambda x: x % 2 == 0

result = list(filter(is_even,numbers_integers))

print(result)

#Вместо lambda  може да си напишем наша функция

# def is_even (number):
#     #return number % 2 == 0
#     # или
#     if number % 2 == 0:
#         return True
#     return False

