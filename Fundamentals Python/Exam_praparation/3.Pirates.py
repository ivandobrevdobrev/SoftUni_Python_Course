cities = {}
events = {}
command = input().split("||")
while command[0] != "Sail":

    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}

    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")

command = input().split("=>")

while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town , gold = command[1], int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

    command = input().split("=>")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    # Итерираме през вложения Речник {Tortuga : { population: 100, gold : 200}
    for town, town_info in cities.items(): # town e Tortuga , town info e речник {population : 100, gold: 200}
        print(f'{town} -> Population: {town_info["population"]} citizens, Gold: {town_info["gold"]} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
