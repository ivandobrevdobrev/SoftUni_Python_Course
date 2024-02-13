n, m = input().split(",")
matrix = []
position = []
cheese_count = 0
for row in range(int(n)):
    matrix.append(list(input()))
    if "M" in matrix[row]:
        position = [row, matrix[row].index("M")]
    if "C" in matrix[row]:
        cheese_count += matrix[row].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()

while command != "danger":
    current_row_index, current_col_index = position
    next_row_index = position[0] + directions[command][0]
    next_col_index = position[1] + directions[command][1]

    if not (0 <= next_row_index < int(n) and 0 <= next_col_index < int(m)):
        print(f"No more cheese for tonight!")
        break

    element = matrix[next_row_index][next_col_index]
    if element == "@":
        command = input()
        continue
    matrix[current_row_index][current_col_index] = "*"
    matrix[next_row_index][next_col_index] = "M"
    position = [next_row_index, next_col_index]

    if element == "C":
        cheese_count -= 1
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif element == "T":
        print("Mouse is trapped!")
        break

    command = input()

if command == "danger" and cheese_count > 0:
    print("Mouse will come back later!")

for row in matrix:
    print(f"{''.join(row)}")
