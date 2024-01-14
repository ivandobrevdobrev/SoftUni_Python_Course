from collections import deque

numbers = deque(input().split()) # със сложност On защото веднъж се прочитат данните с input.split, и след това се слага в опашка всяко по отделно
for _ in range(len(numbers)):
    print(numbers.pop(),end=" ")

    #solution 2
# numbers.reverse()
# print(" ".join(numbers))