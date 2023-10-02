list = input().split()
n = int(input())
list_intergers = []

for num in list:
    digit = int(num)
    list_intergers.append(digit)

for _ in range (n):
    smallest = min(list_intergers)
    list_intergers.remove(smallest)

new = []
for number in list_intergers:
    string = str(number)
    new.append(string)

print(", ".join(new))

#Solution 2

# sorted_nums = sorted(list_intergers)   сортираме от малко- голямо  (1,2,3,4,5)
# for i in range (n):
#     list_intergers.remove(sorted_nums[i])  от листа( махаме числото на индекц 0 от сортирания лист( тоест 1) и така нататък
# print(list_intergers)