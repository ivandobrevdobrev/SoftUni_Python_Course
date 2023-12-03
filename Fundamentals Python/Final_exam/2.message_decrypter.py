import re
decrypted_message = []
n = int(input())
pattern = r'^(\$|\%)([A-Z][a-z]{2,})\1(: )(\[\d+\])\|(\[\d+\])\|(\[\d+\])\|$'
for _ in range(n):
    message = input()
    matches = re.findall(pattern,message)

    if matches:
        for tokens in matches:
            word = tokens[1]
            symbol = tokens[2]
            decrypted_message.append(word)
            decrypted_message.append(symbol)
        numbers = re.finditer(r'\d+', message)
        for num in numbers:
            first_num = num.group()
            ascii_symbol = chr(int(first_num))
            decrypted_message.append(ascii_symbol)
        print("".join(decrypted_message))
        decrypted_message.clear()
    else:
        print("Valid message not found!")


