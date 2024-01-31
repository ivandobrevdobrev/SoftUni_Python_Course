n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()
while command[0] != "END":
    type_command, row, col, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < n and 0 <= col < n):
        print(f"Invalid coordinates")
    elif type_command == "Add":
        matrix[row][col] += number
    elif type_command == "Subtract":
        matrix[row][col] -= number

    command = input().split()
[print(*row) for row in matrix]
