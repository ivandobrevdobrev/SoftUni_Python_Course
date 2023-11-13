text = input()

number = ''
strings = ''
characters = ''

for char in text:
    if char.isalpha():
        strings += char
    elif char.isdigit():
        number += char
    else:
        characters += char

print(number)
print(strings)
print(characters)
