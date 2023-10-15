#Print the indices of all even numbers from the given list

numbers= list(map(int,input().split(", ")))

even_nums_indices = [index for index,digit in enumerate(numbers) if digit % 2 == 0 ]
print(even_nums_indices)

#solution 2

#Use a map function to iterate over the list to find all the even numbers, and add their indices:
found_indices_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
# checking if digit in position x is Even, if yes -> return it

#Use the filter function to filter only the indices and print the result:
even_indices = list(filter(lambda a:a != "no", found_indices_or_no))  # lamda here will skip "NO" and psick even, while iterating in found_indices or no
print(even_indices)