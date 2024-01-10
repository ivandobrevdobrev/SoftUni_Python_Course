from collections import deque
names = deque(input().split())
toss_counter = int(input())

while len(names) > 1 :
    names.rotate(-(toss_counter-1)) # рутираме наляво(първия става последен), но с един път по малко от toss_countera)
    removed_kid = names.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {names.pop()}")