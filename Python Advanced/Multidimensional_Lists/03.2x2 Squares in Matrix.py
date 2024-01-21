row, col = list(map(int, input().split()))

matrix = [input().split() for _ in range(row)]
equal_symbols = 0
for row_index in range (row -1):
    for col_index in range (col -1):
        symbol = matrix[row_index][col_index]

        if symbol == matrix[row_index][col_index+1] and symbol == matrix[row_index+1][col_index] and symbol == matrix[row_index+1][col_index+1]:
            equal_symbols += 1
print(equal_symbols)