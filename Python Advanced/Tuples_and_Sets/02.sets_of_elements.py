n,m = input().split()  #n,m = [int(x) for x in input().split()]

set_one = {int(input()) for _ in range(int(n))}
set_two = {int(input()) for _ in range(int(m))}

print(*set_one.intersection(set_two), sep= "\n")