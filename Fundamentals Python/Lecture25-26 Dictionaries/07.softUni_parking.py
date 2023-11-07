n = int(input())
user_data = {}

for _ in range(n):
    command = input()
    if command.startswith("register"):
        action, user, plate_num = command.split()
        if user in user_data.keys():
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            user_data[user] = plate_num
            print(f"{user} registered {plate_num} successfully")
    elif command.startswith("unregister"):
        action, user = command.split()
        if user not in user_data.keys():
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del user_data[user]

for username,license_plate_number in user_data.items():
    print(f"{username} => {license_plate_number}")


