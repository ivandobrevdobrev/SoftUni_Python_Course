def cookie_eaten(presents_left: int, nice_kids: int):
    """
    Santa is moving in all directions
    with one step.
    """
    for coordinates in directions.values():  # take all values from directions
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == "V":
                nice_kids += 1
            neighbourhood[r][c] = "-"
            presents_left -= 1
        if not presents_left:
            break
    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighbourhood = []
santa_pos = []

total_nice_kid = 0
nice_kid_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    neighbourhood.append(line)

    if "S" in line:
        santa_pos = [row, line.index("S")]
        neighbourhood[row][santa_pos[1]] = "-"
    total_nice_kid += line.count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]
    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kid_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kid_visited = cookie_eaten(presents, nice_kid_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kid_visited == total_nice_kid:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"  # отбелязваме с S последната позиция на Santa, по условие

if not presents and nice_kid_visited < total_nice_kid:
    print(f"Santa ran out of presents!")
[print(*row) for row in neighbourhood]

if nice_kid_visited == total_nice_kid:
    print(f"Good job, Santa! {total_nice_kid} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kid - nice_kid_visited} nice kid/s.")
