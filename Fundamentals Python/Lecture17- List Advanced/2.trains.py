
n = int(input())
wagons = [0] * n

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break
    if command[0] == "add":
        people = int(command[1])
        wagons[-1] += people
    elif command[0] == "insert":
        new_people = int(command[2])
        index = int(command[1])
        wagons[index] += new_people
    elif command[0] == "leave":
        leave_people = int(command[2])
        index = int(command[1])
        wagons[index] -= leave_people

