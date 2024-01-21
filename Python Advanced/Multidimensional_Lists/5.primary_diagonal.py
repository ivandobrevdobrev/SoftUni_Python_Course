row_num = int(input())
matrix = []

#create matrix- square
for _ in range(row_num):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0

for i in range(row_num):
    diagonal_sum += matrix[i][i]  # we know it is Square, soe we need element in [0][0]+[1][1]+... until row_num
print(diagonal_sum)

# Longer solution

# for row_index in range(row_num):
#     for col_index in range(row_num): # same, 'cos it s ssquare
#         if col_index == row_index:
#             diagonal_sum += matrix[row_index][col_index]
# print(diagonal_sum)