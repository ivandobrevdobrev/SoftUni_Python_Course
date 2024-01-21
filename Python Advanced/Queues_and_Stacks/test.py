from collections import deque

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack) # [3, 4, 5, 6, 7]
# stack.pop() # 7
# print(stack) # [3, 4, 5, 6]
# stack.pop() # 6
# stack.pop() # 5
# print(stack) # [3, 4]
#
# a = stack.pop()  # a will be kept in the memory for future use, See below I am printing it
# print(stack)
# stack.append(8)
# stack.append(16)
# print(stack)
# print(a)

# a = deque([3, 5, 8, 10])
# a.popleft()
# a.append(16)
# print(a)
a = 20
b = 30
functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "-": lambda a, b: a - b,
    "+": lambda a, b: a + b,
}
symbol = "+"


print(functions[symbol](a,b))
