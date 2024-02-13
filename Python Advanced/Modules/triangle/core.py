def print_triangle(n):
    print(top(n))
    print(bottom(n))


def top(number):
    for row in range(1, number + 1):
        for num in range(1, row + 1):
            print(num, end="")
        print()


def bottom(number):
    for row in range(number, 0, -1):
        for num in range(1, row):
            print(num, end="")
        print()
