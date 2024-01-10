from collections import deque

names = input()
customers = deque()

while names != "End":
    if names == "Paid":
        while customers:
            print(customers.popleft())  # принтваме и директно махаме докато се изпразнни опашката
    else:
        customers.append(names)
    names = input()

print(f"{len(customers)} people remaining.")
