numbers = list(map(int,input().split(", ")))

positive =[digit for digit in numbers if digit >= 0]
negative =[digit for digit in numbers if digit < 0]
even =[digit for digit in numbers if digit % 2 == 0]
odd =[digit for digit in numbers if digit % 2 != 0]


print(f"Positive: {', '.join(str(num) for num in positive)}")
print(f"Negative: {', '.join(str(num) for num in negative)}")
print(f"Even: {', '.join(str(num) for num in even)}")
print(f"Odd: {', '.join(str(num) for num in odd)}")