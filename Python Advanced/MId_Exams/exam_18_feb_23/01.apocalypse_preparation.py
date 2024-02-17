from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]
created_items = {"Patch":0,"Bandage":0,"MedKit":0}
while textile and medicaments:
    current_textile = textile.popleft()
    current_medicament = medicaments.pop()

    sum_of_both = current_medicament + current_textile

    if sum_of_both == 30:
        created_items["Patch"] += 1
    elif sum_of_both == 40:
        created_items["Bandage"] += 1
    elif sum_of_both == 100:
        created_items["MedKit"] += 1
    elif sum_of_both > 100:
        created_items["MedKit"] += 1
        diff = sum_of_both - 100
        medicaments[-1] += diff
    else:
        medicaments.append(current_medicament + 10)

sorted_items = sorted(created_items.items(),key= lambda x: (-x[1], x[0]))

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


[print(f"{item_name} - {amount_created}") for item_name,amount_created in sorted_items if amount_created > 0]

if textile:
    print(f"Textiles left: {', '.join(str(x) for x in textile)}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")

