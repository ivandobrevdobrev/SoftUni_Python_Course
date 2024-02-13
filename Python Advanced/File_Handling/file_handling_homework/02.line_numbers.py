import os
from string import punctuation

path_file = os.path.join("files","file1.txt")

with open(path_file, "r") as file:
    text = file.readlines()

output_file = open("files/output.txt", "w") # create and open file for writing

for row in range(len(text)):
    letters, marks = 0, 0
    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        if symbol in punctuation:  # check for punctuation symbols and count them
            marks += 1
    output_file.write(f"Line {row +1}:{''.join(text[row][:-1])} ({letters})({marks})\n") # it is [::-1] because need to skip  the last symbol \n

output_file.close()