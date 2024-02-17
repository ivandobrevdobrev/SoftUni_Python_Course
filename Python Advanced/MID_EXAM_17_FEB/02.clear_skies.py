size = int(input())
board = []
position = []
armour = 300
enemies = 4
last_coordinates = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    board.append([el for el in input()]) # list(input)
    if "J" in board[row]:
        position = [row, board[row].index("J")]
        board[row][position[1]] = "-"

while True:
    if enemies == 0 or armour <= 0:
        board[row][col] = "J"
        break

    command = input()
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]
    element = board[row][col]

    if element == "E":
        armour -= 100
        enemies -= 1
    elif element == "R":
        armour = 300
    board[row][col] = "-"
    position = [row, col]

if enemies == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
elif enemies == 1:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")

[print ("".join(row)) for row in board]




