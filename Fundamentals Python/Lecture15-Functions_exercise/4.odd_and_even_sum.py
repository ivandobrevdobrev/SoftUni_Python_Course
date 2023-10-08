def even_odd_sum (some_number : str):
    sum_even = 0
    sum_odd = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        elif int(digit) % 2 != 0:
            sum_odd += int(digit)
    return sum_even, sum_odd

number = input() # ne go pravim s int(input()), zashtoto trqbva da go convertnem pak v string za da go obhodim..nqma smisal
sum_even,sum_odd = even_odd_sum(number)

print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")