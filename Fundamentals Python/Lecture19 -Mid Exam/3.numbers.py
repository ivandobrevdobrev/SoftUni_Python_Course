numbers = list(map(int,input().split()))

average_number = sum(numbers) / len(numbers)

new_numbers = [num for num in numbers if num > average_number]
new_numbers = sorted(new_numbers, reverse=True)
if len(new_numbers) == 0:
    print("No")
else:
   print(" ".join(str(num) for num in new_numbers[:5]))