import re
data = input()
pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern, data)

count_pairs = len(result)
mirror_word = []

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_word.append(f'{pair[1]} <=> {pair[3]}')

if count_pairs > 0:
    print(f"{count_pairs} word pairs found!")
    if not mirror_word:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_word))
else:
    print(f"No word pairs found!")
    print("No mirror words!")