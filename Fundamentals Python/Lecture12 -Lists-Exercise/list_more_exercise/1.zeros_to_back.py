numbers = input().split(", ")
new_list =[]
index = 0
for num in numbers:
    if int(num) != 0:
        new_list.insert(index,int(num))
        index += 1
    else:
        new_list.append(int(num))
print(new_list)