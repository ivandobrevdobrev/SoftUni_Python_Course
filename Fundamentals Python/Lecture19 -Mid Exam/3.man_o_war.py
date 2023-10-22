pirate_ship_status = [int(num) for num in input().split(">")]
warship_status = [int(num) for num in input().split(">")]
maximum_health_capacity = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    action = command.split()
    if action[0] == "Fire":
        index = int(action[1])
        damage = int(action[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()

    elif action[0] == "Defend":
        start_index = int(action[1])
        end_index = int(action[2])
        damage = int(action[3])
        if 0<= start_index < (len(pirate_ship_status)) and 0<= end_index <len(pirate_ship_status):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action[0] == "Repair":
        index, health = int(action[1]), int(action[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > maximum_health_capacity:
                pirate_ship_status[index] = maximum_health_capacity

    elif action[0] == "Status":
        count = 0
        for section in pirate_ship_status:
            if section < 0.2 * maximum_health_capacity:
                count += 1
        print(f"{count} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")
