def password_validator(some_word):
    list_of_errors = []
    if 6 > len(some_word)  or len(some_word)> 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_word.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for character in some_word:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
validated_password = password_validator(password)

if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))


# solutiuon 2    NOT Working

# def password_validator(some_word):
#     if 6 > len(some_word) or len(some_word) > 10:
#         print("Password must be between 6 and 10 characters")
#     if not some_word.isalnum():
#         print("Password must consist only of letters and digits")
#     digit_counter = 0
#     for character in some_word:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#
#
# password = input()
# password_validator(password)
#
# if not password_validator(password):  #if password_validator(password) == False:
#     print("Password is valid")
