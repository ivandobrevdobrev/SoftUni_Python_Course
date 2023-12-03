message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    instructions = command.split(":|:")
    operation = instructions[0]
    if operation == "InsertSpace":
        index = int(instructions[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif operation == "Reverse":
        substring = instructions[1]
        if substring in message:
            new_substring = substring[::-1]
            message = message.replace(substring, "", 1) + new_substring
            print(message)
        else:
            print("error")
    elif operation == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)
        print(message)
print(f"You have a new text message: {message}")