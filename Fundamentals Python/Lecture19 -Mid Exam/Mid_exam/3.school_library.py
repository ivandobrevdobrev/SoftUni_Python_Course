books = input().split("&")

while True:
    command = input()

    if command == "Done":
        print(", ".join(books))
        break
    command = command.split(" | ")
    action = command[0]

    if action == "Add Book":
        if command[1] not in books:
            books.insert(0,command[1])
    elif action == "Take Book":
        if command[1] in books:
            books.remove(command[1])
    elif action == "Swap Books":
        if command[1] in books and command[2] in books:
            index_first_book = books.index(command[1])
            index_second_book = books.index(command[2])
            books[index_first_book],books[index_second_book] = books[index_second_book],books[index_first_book]

    elif action == "Insert Book":
        if command[1] not in books:
            books.append(command[1])

    elif action == "Check Book":
        if 0 <= int(command[1]) < len(books):
            book_name = books[int(command[1])]
            print(book_name)



