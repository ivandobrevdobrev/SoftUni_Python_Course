rows = int(input())

matrix = []
# create matrix with nums
for i in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

# flattering the matrix
flattened = []
for sublist in matrix:
    for num in sublist:
        flattened.append(num)
print(flattened)

# Solution2 for flattering
# flatten = [num for sublist in matrix for num in sublist]
# print(flatten)


# Solution 3

# flattened = []
# for i in range(rows):
#     data = [int(el) for el in input().split(", ")]
#     flattened.extend(data)  # extend взима елементите от data всеки път и ги разопакова и слага като елементи наново в flattened
# print( flattened)


# Solution 4

# rows_count = int(input())
# matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
# flattened = [num for row in matrix for num in row]
# print(flattened)

