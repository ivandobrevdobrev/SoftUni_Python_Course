row, col = [int(num) for num in input().split(", ")]

sum_elements = 0
matrix = []
for i in range(row):
    row_data =[int(el) for el in input().split(", ")]
    sum_elements += sum(row_data)
    matrix.append(row_data)
print(sum_elements)
print(matrix)