text = input()

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]
    if action == "Translate":
        char = command[1]
        replacement = command[2]
        text = text.replace(char,replacement)
        print(text)
    elif action == "Includes":
        substring = command[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif action == "Start":
        substring = command[1]
        if text.startswith(substring):
            print(True)
        else:print(False)
    elif action == "Lowercase":
        text = text.lower()
        print(text)
    elif action == "FindIndex":
        char = command[1]
        index = text.rindex(char)
        print(index)
    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        text = text[:start_index] + text[count+start_index:]
        print(text)
