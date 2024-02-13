size = int(input())
board = []
position = []

for row in range(size):
    board.append(input())
    if "G" in board[row]:
        position = [row, board[row].index("G")]
        #board[row][position[1]] = '-'
        print(position)
