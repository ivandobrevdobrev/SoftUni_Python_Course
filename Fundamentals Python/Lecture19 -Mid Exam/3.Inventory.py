inventory_list = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(inventory_list))
        break
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in inventory_list:
            inventory_list.append(command[1])
    elif command[0] == "Drop":
        if command[1] in inventory_list:
            inventory_list.remove(command[1])
    elif command[0] == "Combine Items":
        old_item,new_item = command[1].split(":")
        if old_item in inventory_list:
            index_old_item = inventory_list.index(old_item)
            inventory_list.insert(index_old_item +1,new_item)
    elif command[0] == "Renew":
        if command[1] in inventory_list:
            inventory_list.remove(command[1])
            inventory_list.append(command[1])


