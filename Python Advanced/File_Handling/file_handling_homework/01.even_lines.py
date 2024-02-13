import os
symbols = ("-", ",", ".", "!", "?")


with open("files/file1.txt", "r") as file:
    text = file.readlines()

for row in range(0,len(text),2): # with step 2 , 'cos we need the even rows only

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")  # replace all symbols with @
    print(*text[row].split()[::-1])                 # unpack the list , split by space, but in reverse

