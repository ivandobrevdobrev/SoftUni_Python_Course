"""
Проверяваме ходовете на Кон на шахматна дъска
като обхождаме всички него ви възможни ходове
дали атакува друг кон.
Броим кой кон има най много атаки
и трявва да го махне, за доме нукой друг да не може да атука никой останал
"""

n = int(input())

matrix = [list(input()) for _ in range(n)]  #  правим квадратна матрица

positions = (                  # сетваме възможните посзиции на които коня може да ходи
    (-2, -1), # горе 2, ляво 1
    (-2, 1), # горе 2, дясно 1
    (-1, -2),# горе 1 , ляво 2
    (-1, 2),# горе 1, дясно 2
    (2, 1),# долу 2, дясно 1
    (2, -1),# долу 2, ляво 1
    (1,-2),# долу 1, ляво 2
    (1,2),# горе 1, ляво 2
)
# positions can be generated as per below:
# pos_numbers = [-2, -1, 1, 2]
# positions = [(x, y) for x in pos_numbers for y in pos_numbers if abs(x) != abs(y)]

removed_knight = 0

while True:
    max_attacks = 0
    knight_most_attacks_position = []  #[row,col]

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K": # check where the knight (K) position is
                attacks = 0
                for pos in positions: # go through all possible position to check if can attack other knight
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:  # check if indixes are valid and if yes if there is K
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    knight_most_attacks_position = [row,col]
                    max_attacks = attacks
    if knight_most_attacks_position:
        r,c = knight_most_attacks_position
        matrix[r][c] = "0"
        removed_knight +=1
    else:
        break

print(removed_knight)
