n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(el) for el in x.split(",")) for x in
               input().split())  # red the input,split by space, then the input put in a tuple with integers
# 1,2  3,4  5,6 => ["1,2", "3,4", "5, 6"] => ((1, 2), (3, 4), (5, 6))

for row, col in coordinates:  # check if element is <0, then bomb will not explode, continue
    if matrix[row][col] < 0:
        continue

    bomb_value = matrix[row][col]
    for x in range(-1, 2):
        for y in range(-1, 2):
            r, c = row + x, col + y

            if 0 <= r < n and 0 <= c < n:
                matrix[r][c] -= bomb_value if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
