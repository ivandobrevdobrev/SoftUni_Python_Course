def solve(number,position):
    mask = 1 << position
    mask = ~mask
    result = number & mask
    print(result)


solve(231,2)