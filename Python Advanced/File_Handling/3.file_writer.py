import os.path

with open("my_first_file.txt","a") as file:
    file.write("I just created my first file!")

path = os.path.join("my_folder_resources", "just_test.txt")

with open(path,"a") as file:
    file.write("created it , to test how i can create and a path and write into teh file using WITH")