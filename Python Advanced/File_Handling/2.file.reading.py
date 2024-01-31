import os

path = os.path.join("my_folder_resources", "numbers.txt")
file = open(path)

total = 0

for line in file.readlines():
    total += int(line.strip()) # strip maha \n line - zashoto w momwnta e 1\n
print(total)

# 2 solution
for line in file:
    total += int(line) # strip maha \n line - zashoto w momwnta e 1\n
print(total)
