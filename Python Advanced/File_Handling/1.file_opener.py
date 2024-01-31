import os


path = os.path.join("my_folder_resources", "text.txt")
try:
    open(path)
    print("File found")
except FileNotFoundError:
    print("File not found")