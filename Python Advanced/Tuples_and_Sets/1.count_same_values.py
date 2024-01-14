numbers = tuple([float(x) for x in input().split()]) # четем входа и го превъщаме във float и тюпъл

same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)
for number, occ in same_values.items():
    print(f"{number} - {occ} times")
