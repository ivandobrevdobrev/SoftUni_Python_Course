targets = list(map(int,input().split()))

while True:
    command = input()
    if command == "End":
        print("|".join(str(num) for num in targets))
        break
    action,index,number = command.split()
    index = int(index)
    number = int(number)
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= number
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index,number)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if 0 <= index < len(targets):

            if 0<= number < targets[index] and number < len(targets[index+1:]):
                strike_target = targets[index]
                # for radius in range(len(targets[strike_target-number:strike_target + number])):
                #     targets.remove(targets[radius])
                for i in range(number):
                    targets.pop(index-1)  # remove the previous index
                    targets.pop(index) # list get trimmed so it is not the (index +1) as they moved to the left
                targets.remove(strike_target)
            else:
                print("Strike missed!")

