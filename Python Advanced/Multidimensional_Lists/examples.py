# a = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
# ]
#
# print(a[1][1])
# print(a[-1][-1])


                    # [[0, 0], [0, 0], [0, 0]]

# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(2):
#         matrix[i].append(0)
# print(matrix)

#with comprehentions

#matrix = [[0 for j in range(2)] for i in range(3)]


         ## [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#         matrix[i].append(j)
# matrix = []

# for i in range(3):
#     sub_list =[]
#     for j in range(1, 4):
#         sub_list.append(j)
#     matrix.append(sub_list)
# print(matrix)
#
# #using comprehension
# matrix = [[j for j in range(1, 4)] for i in range(3)]

           #Flattening a matrix

# matrix = [[1, 2, 3], [4, 5, 6]]
# flattened = [num for sublist in matrix for num in sublist]
# print(flattened)  #--> [1, 2, 3, 4, 5, 6]
#
# flattened_matrix = []
# for sublist in matrix:
#     for el in sublist:
#         flattened_matrix.append(el)
# print(flattened_matrix)

                   # Traversing

matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]

# using indices

# for row in range(len(matrix)):
#     for column in range(len(matrix[row])):
#         print(matrix[row][column], end=" ")

# using elements

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#
# [print(num) for num in [j for j in matrix]]


                   # Changing Values

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        matrix[row][column] += 1
        print(matrix[row][column], end=" ")

matrix[1][2]= 100
print(matrix)