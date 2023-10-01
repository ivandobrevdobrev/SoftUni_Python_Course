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

