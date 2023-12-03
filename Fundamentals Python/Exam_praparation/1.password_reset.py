
password = input()
new_password = ""
while True:
    command = input()
    if command == "Done":
        break
    instructions = command.split()
    action = instructions[0]
    if action == "TakeOdd":
        current_password = ""
        for index,symbol in enumerate(password):
            if index % 2 != 0:
                current_password += symbol
        password = current_password
        print(password)

    elif action == "Cut":
        length = int(instructions[2])
        index = int(instructions[1])
        substring = password[index:index+length]
        password = password.replace(substring,"",1)
        print(password)
    elif action == "Substitute":
        substring = instructions[1]
        substitute = instructions[2]
        if substring in password:
            password = password.replace(substring,substitute)
            print(password)
        else:
            print(f"Nothing to replace!")
print(f"Your password is: {password}")
