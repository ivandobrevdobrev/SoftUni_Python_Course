n = int(input())
commands = input().split()

matrix = []
miner_pos = [] # position of the miner
coal_collected, total_coal = 0, 0 # when these become equal we stop

direction = {
    "up": [-1, 0],  # ако се движи нагоре, намаляме реда с 1, колоната остава същата
    "down": [1, 0], # ако сме на 5,3 и искаме да отидем на горе --> 5 + (-1), 3+0 --> 4,3
    "left": [0, -1],
    "right": [0, 1],
}

# create matrix
for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[miner_pos[0]][miner_pos[1]] = "*"  # след като го намерим къде се намира сетваме мястото му с *

    total_coal += matrix[row].count("c")  # броим колко пъти се среща с и го добавяме към тотал

for command in commands:
    r, c = miner_pos[0] + direction[command][0], miner_pos[1] + direction[command][1] # coordinates where we want miner to move

    if not (0 <= r < n and 0 <= c < n): # check if indices we want to go are valid, if not skip and continue
        continue
    miner_pos = [r,c]  # after we are sure ccordinatets are valis, we set his position

    if matrix[r][c] == "c":
        coal_collected += 1

        if coal_collected == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"  # setvame * sled kato e minal ve4e i e obral kakvoto ima
else:
    print(f"{total_coal-coal_collected} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")





