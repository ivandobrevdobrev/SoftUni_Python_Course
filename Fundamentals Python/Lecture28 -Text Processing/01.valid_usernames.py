def no_redundant_symbol(username):
    if " " in username:
        return  False
    return True


def characters_are_valid(username):
    for chars in username:
        if not (chars.isalnum() or chars == "-" or chars == "_"):
            return False
    return True


def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def username_is_valid(username):
    if length(username) and characters_are_valid(username) and no_redundant_symbol(username):
        return True
    return False


user_names = input().split(", ")

for username in user_names:
    if username_is_valid(username):
        print(username)
