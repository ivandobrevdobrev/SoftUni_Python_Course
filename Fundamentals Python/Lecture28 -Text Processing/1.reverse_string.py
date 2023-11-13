while True:

    word = input()
    if word =="end":
        break

    print(f"{word} = {word[::-1]}")

    # reversed_text = ''
    # for ch in reversed(word):
    #     reversed_text += ch
    # print(reversed_text)