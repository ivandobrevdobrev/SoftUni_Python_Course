people = int(input())

lift = list(map(int,input().split()))

for num in range(len(lift)):
    if lift[num] < 4:
        diff = 4 - lift[num]
        if people <= diff:
            lift[num] += people
        else:
            lift[num] = 4
        people -= diff
    if people <= 0:
        break
if people <= 0:
    if people == 0 and sum(lift) % 4 == 0:
        print(*lift)
    else:
        print("The lift has empty spots!")
        print(*lift)
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)


