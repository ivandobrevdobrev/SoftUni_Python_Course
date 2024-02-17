n, m = input().split()
matrix = []
position = []
touches = 0
moves = 0
opponents = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(int(n)):
    matrix.append(input().split())
    if "B" in matrix[row]:
        position = [row, matrix[row].index("B")]
    opponents += matrix[row].count("P")


command = input()

while command != "Finish":
    current_row_index, current_col_index = position
    next_row_index = position[0] + directions[command][0]
    next_col_index = position[1] + directions[command][1]

    if not(0 <= next_row_index < int(n) and 0 <= next_col_index < int(m)):
        command = input()
        continue
    element = matrix[next_row_index][next_col_index]
    if element == "O":
        command = input()
        continue
    elif element == "P":
        touches += 1
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index,next_col_index]
    moves += 1
    if touches == opponents:
        break

    command = input()

print("Game over!")
print(f"Touched opponents: {touches} Moves made: {moves}")