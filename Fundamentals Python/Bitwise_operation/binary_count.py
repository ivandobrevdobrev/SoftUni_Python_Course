def binary_count(number, digit):  # колко 0 или 1 ( digit) се съдържат в бинарното число на number
    count = 0
    while number > 0:
        remainder = number % 2
        number = int(number / 2)
        if remainder == digit:
            count += 1
    print(count)


binary_count(10, 1)

num = 60
print(bin(num))  #  превръщане на Десетично в Двоични с bin() метода