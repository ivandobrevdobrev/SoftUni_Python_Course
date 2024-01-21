n = int(input())
names = set()
for _ in range(n):
    names.add(input())

print(*names, sep= "\n")

#solution2

# names ={input() for _ in range(int(input()))}
# print(*names, sep= "\n")
#
#
# #solution 3
# print(*{input() for _ in range(int(input()))},sep="/n")