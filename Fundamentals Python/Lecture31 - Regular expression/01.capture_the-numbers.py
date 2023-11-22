import re

matches = []

while True:   # or while line:  .....text=input()
    text = input()
    pattern = r"\d+"
    matches += re.findall(pattern, text)

    if text == "":
        break
print(*matches)