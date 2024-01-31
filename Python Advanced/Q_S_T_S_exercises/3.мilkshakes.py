from collections import deque

chocolate = list(int(el) for el in input().split(", "))
milk_cups = deque(int(el) for el in input().split(", "))

choco_milkshakes = 0

while chocolate and milk_cups:

    current_choco = chocolate.pop()
    current_cup = milk_cups.popleft()
    if current_choco <= 0 and current_cup <= 0:
        continue
    elif current_choco <= 0:
        milk_cups.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolate.append(current_choco)
        continue
    if current_cup == current_choco:
        choco_milkshakes += 1
    else:
        milk_cups.append(current_cup)
        chocolate.append(current_choco - 5)
    if choco_milkshakes == 5:
        print(f"Great! You made all the chocolate milkshakes needed!")
        break
if choco_milkshakes < 5:
    print(f"Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(el) for el in chocolate)}")
else:
    print(f"Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(el) for el in milk_cups)}")
else:
    print(f"Milk: empty")