numbers = list(map(int,input().split()))

while True:
    command = input()
    if command == "end":
        break
    action = command.split()

    if action[0] == "swap":
        index_one = int(action[1])
        index_two = int(action[2])
        numbers[index_one],numbers[index_two] = numbers[index_two],numbers[index_one]
    elif action[0] == "multiply":
        index_one = int(action[1])
        index_two = int(action[2])
        numbers[index_one] = numbers[index_one] * numbers[index_two]

    elif action[0] == "decrease":
        numbers =[num -1 for num in numbers]

print(", ".join(str(num) for num in numbers))