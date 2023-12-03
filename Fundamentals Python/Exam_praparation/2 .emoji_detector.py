import re

text = input()
cool_threshold_sum = 1
words_sum = 0
cool_emojies = []
pattern = r'(\*{2}|:{2})([A-Z][a-z]{2,})(\1)'
matches = re.findall(pattern,text)
digit_match = re.findall(r'\d',text)

for digit in digit_match:
    cool_threshold_sum *= int(digit)
for match_word in matches:
    words_sum += sum([ord(symbol) for symbol in match_word[1]])
    if words_sum >= cool_threshold_sum:
        cool_emojies.append("".join(match_word))
    words_sum = 0
print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojies:
    print(cool_emoji)