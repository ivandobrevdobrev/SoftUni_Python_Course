money_as_string = input().split(", ")
beggars = int(input())

money_as_digits =[]

for strings in money_as_string:
    digits = int(strings)
    money_as_digits.append(digits)
final_sums = []

starting_index = 0

while starting_index < beggars:  # moje i s FOR - for begs in range (beggars)
    current_beggar_sum = 0
    for current_index in range(starting_index,len(money_as_digits),beggars):
        current_beggar_sum += money_as_digits[current_index]
    final_sums.append(current_beggar_sum)
    starting_index += 1
print(final_sums)