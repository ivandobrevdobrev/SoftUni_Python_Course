numbers = list(map(int,input().split()))

while True:
    command = input()
    if command == "Finish":
        break

    action = command.split()
    digit = int(action[1])

    if action[0] == "Add":
        numbers.append(int(action[1]))

    elif action[0] == "Remove":
        if digit in numbers:
            numbers.remove(digit)

    elif action[0] == "Replace":
        replacement = int(action[2])
        if digit in numbers:
            index_digit = numbers.index(digit)
            numbers[index_digit] = replacement

    elif action[0] == "Collapse":
        numbers = [num for num in numbers if num >= digit]

print(*numbers)
#print(new_numbers)