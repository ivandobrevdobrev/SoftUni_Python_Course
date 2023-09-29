factor = int(input())
count= int(input())
list = []

for multiplier in range(1,count+1):
    number = multiplier * factor   # can be done : list.append(multiplier*factor)
    list.append(number)
print(list)