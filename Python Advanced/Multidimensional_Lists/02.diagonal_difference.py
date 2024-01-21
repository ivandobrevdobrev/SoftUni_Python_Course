n = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(n)]

primary_sum, secondary_sum = 0, 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n-i-1]

print(abs(primary_sum - secondary_sum))

# Solution 2

# for i in range(n):
#     line = [int(x) for x in input().split()]  # не правим матрица, а директно четем входния ред и взимаме числата
#     primary_sum += line[i]
#     secondary_sum += line[n - i - 1]

"""
n = 3
matrix :
11 2  4
4  5  6
10 8 -12
"""