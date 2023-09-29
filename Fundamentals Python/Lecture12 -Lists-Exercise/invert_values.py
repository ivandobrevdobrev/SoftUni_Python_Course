list_numbers = input().split()
opposite_numbers =[]

for num in list_numbers:
    current_number  = -int(num)
    opposite_numbers.append(current_number)


print(opposite_numbers)