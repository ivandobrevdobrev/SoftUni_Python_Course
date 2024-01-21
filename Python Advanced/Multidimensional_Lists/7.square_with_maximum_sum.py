
row, col = map(int,input().split(", "))
matrix = []
for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float('-inf')
sub_matrix = []
for row_index in range(row-1):
    for col_index in range (col -1):
        left_num = matrix[row_index][col_index]
        right_num = matrix[row_index][col_index + 1]
        bottom_left  = matrix[row_index + 1][col_index]
        bottom_right = matrix[row_index + 1][col_index + 1]

        total = left_num + right_num + bottom_right + bottom_left
        if max_sum < total:
            max_sum = total
            sub_matrix = [[left_num, right_num],[bottom_left,bottom_right]]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

