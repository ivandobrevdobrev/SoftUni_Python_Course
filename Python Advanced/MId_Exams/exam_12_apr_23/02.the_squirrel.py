n = int(input())
hazelnuts = 0
matrix = []
position = 0, 0
is_out_of_matrix = False
is_on_trap = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

commands = input().split(", ")
for row in range(n):
    matrix.append(list(input()))
    if "s" in matrix[row]:
        position = row, matrix[row].index("s")
        matrix[row][position[1]] = "*"

for command in commands:
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not (0 <= row < n and 0 <= col < n):
        print("The squirrel is out of the field.")
        is_out_of_matrix = True
        break
    position = row, col
    element = matrix[row][col]
    matrix[row][col] = "*"

    if element == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif element == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        is_on_trap = True
        break
if hazelnuts < 3 and not(is_on_trap or is_out_of_matrix):
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
