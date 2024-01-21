from collections import deque

bees = deque([int(bee) for bee in input().split()])
nectar_values = list(map(int, input().split()))
symbols = deque(input().split())

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "-": lambda a, b: a - b,
    "+": lambda a, b: a + b,
}
total_honey = 0

while bees and nectar_values:
    symbol = symbols[0]
    if symbol[0] == "/" and nectar_values[-1] == 0:
        bees.popleft()
        symbols.popleft()
        nectar_values.pop()
        continue
    if bees[0] < nectar_values[-1]:
        total_honey += abs(functions[symbol](bees[0], nectar_values[-1]))
        bees.popleft()
        symbols.popleft()
    nectar_values.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_values:
    print(f"Bees left: {', '.join(str(x) for x in nectar_values)}")


