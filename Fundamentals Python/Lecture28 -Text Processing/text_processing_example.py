# message = 'hello I\'am'
# message1 = 'hello Ivan\\George'
#
# print(message1)
#
# print(id(message))

# text = "Hello_"
# print(text.isalnum())
#
# txt = "I like bananas"
# print(txt.replace("bananas", "apples"))

# txt = "I like bananas bananas bananas"
# x = txt.replace("bananas", "apples", 2)
# print(x)

# name = "Maria"
# new = list(name)
# new[0] = "B"
# print(new)
#
# name = name.replace("M","B")
# print(name)


# text = " ivan"
# a = text.ljust(6,"*")
# print(a)

# input_string = [string.strip() for string in input().split()]
# print(input_string)


word = '15*a@ge'
index = word.index("@")
for symbol in word[index:]:
    print(symbol)
