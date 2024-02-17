size = int(input())
car_num = input()
kilometers = 0
position = [0,0]
matrix = []
count_T = 0
tunel_1 = []
tunel_2 = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())
    if "T" in matrix[row]:
        if count_T == 0:
            tunel_1 =[row,matrix[row].index("T")]
            count_T +=1
        else: tunel_2 = [row,matrix[row].index("T")]

command = input()

while command != "End":
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    element = matrix[row][col]
    position = [row, col]

    if element == ".":
        kilometers += 10
    elif element == "T":
        if position == tunel_1:
            position = tunel_2
            matrix[row][col] = "."
            matrix[position[0]][position[1]] = "."
            kilometers += 30
        elif position == tunel_2:
            position = tunel_1
            matrix[row][col] = "."
            matrix[position[0]][position[1]] = "."
            kilometers += 30
    elif element == "F":
        kilometers += 10

        print(f"Racing car {car_num} finished the stage!")
        break

    command = input()
matrix[position[0]][position[1]] = "C"
if command == "End":
    print(f"Racing car {car_num} DNF.")
print(f"Distance covered {kilometers} km.")
[print("".join(row)) for row in matrix]