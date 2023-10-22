initial_list = input().split("!")

while True:
    command = input()

    if command == 'Go Shopping!':
        break
    command = command.split()
    action = command[0]
    item = command[1]

    if action == 'Urgent':
        if item not in initial_list:
            initial_list.insert(0,item)
    elif action == 'Unnecessary':
        if item in initial_list:
            initial_list.remove(item)
    elif action == 'Correct':
        new_item = command[2]
        if item in initial_list:
            idx = initial_list.index(item)
            initial_list[idx] = new_item

    elif action == 'Rearrange':
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))