n = int(input())
matrix = []
position = []
hits = 0
battle_cruisers = 3
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(int(n)):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        position = [row, matrix[row].index("S")]
        matrix[row][position[1]] = "-"


while battle_cruisers > 0 and hits < 3:
    command = input()
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]
    element = matrix[row][col]
    position = [row,col]
    matrix[row][col] = "-"

    if element == "*":
        hits += 1
        if hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break
    elif element == "C":
        battle_cruisers -= 1
        if battle_cruisers == 0:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
matrix[row][col] = "S"
for row in matrix:
    print("".join(row))


