def tribonacci_sequence(n):  # tribinachi - sum of the prevous 3 digits
    list = [1]  # create a list to start from 1
    for i in range(n - 1):
        if len(list) < 4:  # if list is less than 4 just sum all digits there
            num = sum(list)
            list.append(num)
        else:
            num = sum(list[-3:])  # calculate the sum of ten last 3 items in the list,
            list.append(num)  # then put the num in the list
    return list


n = int(input())
print(*tribonacci_sequence(n))

# list = [1,2,3,4,5,6,8]
# print(sum(list[-2:]))
