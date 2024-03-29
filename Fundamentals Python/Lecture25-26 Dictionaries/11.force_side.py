force_side_dictionary = {}

command = input()

while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        is_user_there = False

        for value in force_side_dictionary.values():
            if force_user in value:
                is_user_there = True
                break
        if not is_user_there:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif " -> " in command:
        force_user,force_side = command.split(" -> ")
        for value in force_side_dictionary.values():
            if force_user in value:
                value.remove(force_user)
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side,force_user in force_side_dictionary.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for user in force_user:
            print(f"! {user}")