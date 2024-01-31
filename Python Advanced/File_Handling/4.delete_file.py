import os

path = os.path.join("my_folder_resources", "just_test.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("'File already deleted!")
