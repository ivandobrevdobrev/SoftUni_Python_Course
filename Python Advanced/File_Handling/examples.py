# import os
#
# path = os.path.join("my_folder","text.txt")
#
# file = open(path)

#file = open("my_text","w")
#file.write("hello") # ще пише във файла но ще трие предишното

# file = open("my_text","a")
# file.write("\nIvan")


                  #Reading a file

# file = open("my_text")

# 1 print(file.readlines()) - printira v List

# 2 or loop trough file and read -- printira normalno
# for line in file:
#     print(line, end="")


# 3 comprehension
# lines = file.readlines()
# [print(line, end="") for line in lines]

             #Writing  and Closing a file WITH Statement

with open("my_text") as file:  # will close teh file automatically when finished
    for line in file:
      print(line, end="")
