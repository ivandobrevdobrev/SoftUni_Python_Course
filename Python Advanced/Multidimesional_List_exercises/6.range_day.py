def move(direction: str, steps: int):
    """
    Returns new position if possible,
   otherwise return old position
    """
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position  # ако не може да се преместим , си оставаме на старат позиция
    if field[r][
        c] == "x":  # ако посзицията на която искаме да отидем е х, се върни на настоящата позиция, не може да стъпим на мишена
        return my_position
    return [r, c]


def shoot(direction: str):
    """
    returns coordinates of target, if the target exists
    otherwise return None
    """
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":  # ако уцели мишена, сетваме позицията й ка то точка
            field[r][c] = "."
            return [r, c]
        r += directions[direction][0]  # продължаваме движението на по матрицата ако не е свалил мишена
        c += directions[direction][1]


SIZE = 5  # условие матрицата е 5х5
field = []  # the matrix

targets = 0
targets_hit = 0

targets_hit_positions = []  # списък да пазим позициите на сваленте мишени
my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(SIZE):
    field.append(input().split()) # съсдаваме матрица field

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]
    targets += field[row].count("x")  # обхождайки редовете на матрицата преброяваме колко мишени има за сваляне. те са отбелязани с х

for _ in range(int(input())):  # за броя на командите прочитаме самоте команди
    command_info = input().split()

    if command_info[0] == "move":
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_poss = shoot(command_info[1])  # will return coordintes for any shot target, else None
        if target_down_poss:
            targets_hit_positions.append(target_down_poss)
            targets_hit += 1
        if targets_hit == targets:
            print(f"Training completed! All {targets_hit} targets hit.")
            break
if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")
print(*targets_hit_positions, sep="\n")
