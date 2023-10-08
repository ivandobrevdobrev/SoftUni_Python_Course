def chars_in_between(first, second) -> list:
    char_list = []
    for char in range(ord(first) + 1, ord(second)):
        char_list.append(chr(char))
    return char_list


first_character = input()
second_character = input()

final_result = chars_in_between(first_character,second_character)
print(" ".join(final_result))