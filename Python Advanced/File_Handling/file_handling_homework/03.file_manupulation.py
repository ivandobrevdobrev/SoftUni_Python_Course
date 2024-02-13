import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        with open(f"files/{info[0]}", "w"):
            pass                         # create file only
    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file :# open teh file to append text there
            file.write(f"{info[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r+") as file: # r+ отваряме файла за чете и писане, но ако го няма да даде грешка, иначе може с
                text = file.read()
                text = text.replace(info[1], info[2])  # файла още не е презаписан, само стои в паметта

                file.seek(0) # трябва да се върнем обратно горе, защото курсора е най- долу
                file.write(text)  # презаписваме вече файла
                file.truncate()   # ако презаписания текст е по- малко от стария текст, truncate ще изреже вси  ко след новото добавено
        except FileNotFoundError:
            print("An Error occurred!")
    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An Error occurred!")

    elif command == "End":
        break

