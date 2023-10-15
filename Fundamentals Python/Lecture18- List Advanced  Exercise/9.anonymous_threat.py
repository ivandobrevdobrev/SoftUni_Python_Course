
# Не е довършена Лекция

text = input().split()
command = input().split()

while command[0] != "3:1":
    if command[0] == "merge":
        statr_index = int(command[1])
        end_index = int(command[2])
        if statr_index < 0:
            statr_index = 0
        if statr_index > len(text) - 1:
            end_index = len(text) -1
            merged_elements = "".join(text[statr_index:end_index -1])
            text[statr_index:end_index +1] = [merged_elements]
    elif command [0] == "divide":
        index = int(command[1])
        partition = int(command[2])
        element = text[index]
        pass
    command = input()
print("".join(text))
