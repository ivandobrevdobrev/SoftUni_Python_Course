n = int(input())
pieces ={}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]
while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    action = command[0]
    if action == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces.keys():
            pieces[piece] = [composer,key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece in pieces.keys():
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces.keys():
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, piece_info in pieces.items():
    print(f"{piece} -> Composer: {piece_info[0]}, Key: {piece_info[1]}")
