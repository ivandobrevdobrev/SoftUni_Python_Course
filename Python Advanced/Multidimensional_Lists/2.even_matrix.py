rows = int(input())

matrix = []

for i in range(rows):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)
print(matrix)

#Solution 2

# rows = int(input())
# matrix = []
# for i in range(rows):
# row = input().split(", ")
# matrix.append(list(map(int, row)))
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
# print(evens)