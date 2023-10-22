initial_loot = input().split("|")

while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    if action == "Loot":
        for item in command[1:]:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif action == "Drop":
        if 0 <= int(command[1]) < len(initial_loot):
            item = initial_loot[int(command[1])]
            initial_loot.remove(item)
            initial_loot.append(item)

    elif action == "Steal":
        count = int(command[1])
        stolen_items = initial_loot[-1:-(count + 1):-1]
        print(", ".join(reversed(stolen_items)))
        if count <= len(initial_loot):
            for i in range(count):
                initial_loot.pop()
        else:
            initial_loot.clear()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    length_elements = 0
    for element in initial_loot:
        length_elements += len(element)
    average = length_elements / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
