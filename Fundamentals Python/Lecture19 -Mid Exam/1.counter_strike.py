energy = int(input())

won_battles = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
    else:
        energy = 0
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break

    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles



