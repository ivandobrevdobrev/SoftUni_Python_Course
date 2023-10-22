dungeons_room = input().split("|")
health = 100
bitcoins = 0
best_room = 0
is_killed = False

for room in dungeons_room:
    command,number = room.split()
    best_room += 1
    if command == "potion":
        temp_health = health
        health += int(number)
        if health > 100:
            health = 100
        amount = health - temp_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")
    else:
        health -= int(number)
        if health > 0 :
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            is_killed = True
            break
if not is_killed :
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


