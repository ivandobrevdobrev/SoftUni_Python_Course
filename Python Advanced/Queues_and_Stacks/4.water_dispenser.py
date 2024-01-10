from collections import deque
water = int(input())
people = deque()

name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters = int(data[0])
        person = people.popleft()
        if water >= liters:
            print(f"{person} got water")
            water -= liters
        else:
            print(f"{person} must wait")

    else:
        quantity = data[0]
        litters = int(data[1])
        water += litters
    command = input()

print(f"{water} liters left")