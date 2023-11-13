text = input()
final_text = ""
strength = 0

for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        final_text += text[index]
        strength += int(text[index +1])
    else:
        final_text += text[index]
print(final_text)

