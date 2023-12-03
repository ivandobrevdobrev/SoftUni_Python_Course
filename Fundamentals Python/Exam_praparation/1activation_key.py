activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    instructions = command.split(">>>")
    if instructions[0] == "Contains":
        substring = instructions[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif instructions[0] == "Flip":
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        if instructions[1] == "Upper":
            activation_key = activation_key[:start_index] + (activation_key[start_index:end_index].upper()) + activation_key[end_index:]
        elif instructions[1] == "Lower":
            activation_key = activation_key[:start_index] + (activation_key[start_index:end_index].lower()) + activation_key[end_index:]
        print(activation_key)
    elif instructions[0] == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)


print(f"Your activation key is: {activation_key}")