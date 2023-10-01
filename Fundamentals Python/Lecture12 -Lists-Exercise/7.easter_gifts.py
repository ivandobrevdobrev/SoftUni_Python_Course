gifts = input().split()
command = input()
command_list =[]
while command != "No Money":
    command_list = command.split()
    if command_list[0] == "OutOfStock":
        for index in range(len(gifts)):
           if gifts[index] == command_list[1]:
              gifts[index] = "None"
    elif command_list[0] == "Required":
        digit_in_command = int(command_list[2])
        #if 0 <= digit_in_command < len(gifts):
        for index in range(len(gifts)):
            if index == digit_in_command:
              gifts[digit_in_command] = command_list[1]
    elif command_list[0] == "JustInCase":
        gifts[-1] = command_list[1]

    command = input()
for gift in gifts:
    if gift == "None":
        gifts.remove(gift)
print(" ".join(gifts))