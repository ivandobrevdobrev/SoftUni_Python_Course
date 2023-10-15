# #72olle 103doo 100ya	Hello good day
#
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)
def decipher_word(word):
    digits = []
    new_word = []
    for symbol in word:
        if symbol.isdigit():
            digits.append(symbol)
        else:
            new_word.append(symbol)
    ascii_symbol = int("".join(digits))
    new_word.insert(0, (chr(ascii_symbol)))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return  "".join(new_word)


secret_message = input().split()
decipher_message = [decipher_word(word) for word in secret_message]
print(" ".join(decipher_message))
