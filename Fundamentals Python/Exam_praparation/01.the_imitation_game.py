def operation_move(message, number):
    message = message[number:] + message[:number]
    new_message = message
    return new_message


def operation_insert(message, index, value):
    message = message[:index] + value + message[index:]
    new_message = message
    return new_message


def opration_changeAll(new_message, substring, replacement):
    new_message = new_message.replace(substring, replacement)
    return new_message


def main_function():
    new_message = encrypted_message
    while True:
        command = input().split("|")

        if command[0] == "Decode":
            break
        elif command[0] == "Move":
            n = int(command[1])
            new_message = operation_move(new_message, n)
        elif command[0] == "Insert":
            index = int(command[1])
            value = command[2]
            new_message = operation_insert(new_message, index, value)
        elif command[0] == 'ChangeAll':
            substring = command[1]
            replacement = command[2]
            new_message = opration_changeAll(new_message, substring, replacement)
    print(f'The decrypted message is: {new_message}')


encrypted_message = input()
main_function()
