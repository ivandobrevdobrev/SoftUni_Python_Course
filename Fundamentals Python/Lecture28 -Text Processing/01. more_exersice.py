name = ""
age = ""
number = int(input())


for _ in range(number):
    text = input().split()
    for word in text:
        if "@" in word:
            index = word.index("@")
            index_two = word.index("|")
            for symbol in word[index+1:index_two]:
                name += symbol

        if "#" in word:
            index = word.index("#")
            index_two = word.index("*")
            for symbol in word[index+1:index_two]:
                age += symbol

    print(f"{name} is {(age)} years old.")
    name =""
    age = ""


# Second version
#
# number_of_lines = int(input())

# for index in range(number_of_lines):
#     line = input()
#     name = ""
#     age = ""
#     name_found = False
#     age_found = False
#     for char in line:
#         if char == "@":
#             name_found = True
#             continue
#         if char == "|":
#             name_found = False
#         if name_found:
#             name += char
#         if char == "#":
#             age_found = True
#             continue
#         if char == "*":
#             age_found = False
#         if age_found:
#             age += char
#     print(f"{name} is {age} years old.")