n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word,synomym_list in synonyms.items():
    synomym_string = ", ".join(synomym_list)
    print(f"{word} - {synomym_string}")