n, m = input().split()
starting_position = []
field = []
position = []
is_delivery_failed = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(int(n)):
    field.append([el for el in input()])
    if "B" in field[row]:
        position = [row, field[row].index("B")]
        starting_position = position
        field[row][position[1]] = "-"

while True:
    command = input()
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not (0 <= row < int(n) and 0 <= col < int(m)):
        is_delivery_failed = True
        print("The delivery is late. Order is canceled.")
        break
    element = field[row][col]
    if element == "*":
        continue
    else:
        position = [row, col]
        field[row][col] = "."
        if element == "P":
            field[row][col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        elif element == "A":
            field[row][col] = "P"
            print("Pizza is delivered on time! Next order...")
            break

if not is_delivery_failed:
    field[starting_position[0]][starting_position[1]] = "B"
    [print("".join(row)) for row in field]
else:
    field[starting_position[0]][starting_position[1]] = " "
    [print("".join(row)) for row in field]
