odd_set = set()
even_set = set()

for row in range(1,int(input()) +1):
    ascii_sum = sum(ord(letter)for letter in input()) // row

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)
sum_odd_set,sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep= ", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep= ", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep= ", ")