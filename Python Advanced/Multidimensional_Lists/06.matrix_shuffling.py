def indices_validation(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(some_command, indices):
    if len(indices) == 4 and indices_validation(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)
while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]
    # ако инпута е цифра да върне цифра, ако не да върне просто инпута... цифрите директно опаковани

    if command == "END":
        break
    swap_elements(command, coordinates)
