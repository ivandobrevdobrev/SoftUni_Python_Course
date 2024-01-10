def solve(number):
    number = number >> 1
    lsb = number & 1  # we check whether the bit at position 0 is equal to 1 or not. If the bit is equal to 1 the result is 1 if the bit is not equal - the result is 0;
    print(lsb)        # lsb = least significant bit


solve(13)

"""
Write a program that prints the bit at position 1 of the given integer. We use the standard counting: from right to left, starting from 0.
"""
