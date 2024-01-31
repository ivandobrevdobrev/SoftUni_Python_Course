size = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:  # намираме позицията на Алис
        alice_pos =[row,matrix[row].index('A')]  # сетваме позицията на Алиц
        matrix[row][alice_pos[1]] = '*'   # позицията вече е маркираме като * според условието,, щото ще тръгне да се движи из матрицата

while tea_bags < 10:   # започваме да се движим по матрицата докато нямаме 10 торбички
    direction = input()

    row = alice_pos[0] + directions[direction][0] # събираме позицията на алис 0левия индекс на direktions
    col = alice_pos[1] + directions[direction][1]

    if not(0 <= row < size and 0 <= col < size):  #проверка дали не сме излезли от матрицата
        break

    alice_pos = [row, col]
    element = matrix[row][col] # взимаме елемента , защото Алис е била вече там
    matrix[row][col] = "*"

    if element == "R":  # ако елемета е дупка R , брейк
        break
    elif element.isdigit(): # ако елемента е цифра го прибавяме към общия чай
        tea_bags += int(element)

if tea_bags < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

[print(*row) for row in matrix]





