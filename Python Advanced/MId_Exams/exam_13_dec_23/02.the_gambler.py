size = int(input())
board = []
position = []
cash = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    board.append([el for el in input()]) # list(input)
    if "G" in board[row]:
        position = [row, board[row].index("G")]
        board[row][position[1]] = "-"

command = input()

while command != "end":

    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        print(f"Game over! You lost everything!")
        break
    position = [row, col]
    element = board[row][col]
    board[row][col] = "-"
    if element == "W":
        cash += 100
    elif element == "P":
        cash -= 200
    elif element == "J":
        cash += 100_000
        board[row][col] = "G"
        print(f"You win the Jackpot!")
        print(f"End of the game. Total amount: {cash}$")

        [print ("".join(row)) for row in board]
        break
    if cash <= 0:
        print(f"Game over! You lost everything!")
        break

    command = input()
if command == "end":
    board[row][col] = "G"
    print(f"End of the game. Total amount: {cash}$")
    [print ("".join(row)) for row in board]
