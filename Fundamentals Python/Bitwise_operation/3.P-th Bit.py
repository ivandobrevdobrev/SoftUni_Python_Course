def solve(number,position):
    number = number >> position # Shift the number p times to the right (where p is the position) by using the >> operator. In that way the bit we want to check will be at position 0
    lsb = number & 1
    print(lsb)


solve(2145,5)

"""
Write a program that prints the bit at position p of the given integer. We use the standard counting: from right to left, starting from 0.
"""