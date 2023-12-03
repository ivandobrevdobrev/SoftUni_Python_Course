words_definition = input().split(" | ")
word_info = {}
for part in words_definition:
    word, definition = part.split(": ")
    if word in word_info.keys():
        word_info[word].append(definition)
    else:
        word_info[word] = []
        word_info[word].append(definition)

test_words = input().split(" | ")
command = input()
if command == "Test":
    for word in test_words:
        if word in word_info.keys():
            print(f"{word}:")
            for definition in word_info[word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for key in word_info.keys():
        print(f"{key}",end=" " )

