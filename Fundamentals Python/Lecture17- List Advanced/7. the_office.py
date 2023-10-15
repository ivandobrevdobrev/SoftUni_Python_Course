employees = input().split()
happiness_facttor = int(input())

improved_happiness_employees= list(map(lambda x: int(x) * happiness_facttor,employees))

#Now, it is time to filter the elements that are greater than the average:

filtered_employees = list(filter(lambda x:x >= (sum(improved_happiness_employees)/len(improved_happiness_employees)),improved_happiness_employees))

if len(filtered_employees) >= len(improved_happiness_employees)/2:
    print(f"Score: {len(filtered_employees)}/{len(improved_happiness_employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(improved_happiness_employees)}. Employees are not happy!")
