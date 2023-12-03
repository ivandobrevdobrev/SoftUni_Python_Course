def rate(name, number):

    plants[name]['all_ratings'].append(number)



    return plants


def update(name, number):
    plants[name]['rarity'] = number
    return plants


def reset(name):
    plants[name]['all_ratings'].clear()


n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant not in plants.keys():
        plants[plant] = {'rarity': rarity, "all_ratings":[]}
    plants[plant] = {'rarity': rarity,"all_ratings":[]}

while True:
    command = input().split(': ')
    if command[0] == "Exhibition":
        break
    action = command[0]

    if action == "Rate":
        plant_name, number = command[1].split(" - ")
        number = int(number)
        if plant_name in plants.keys():
            rate(plant_name, number)
        else: print("error")

    elif action == "Update":
        plant_name, number = command[1].split(" - ")
        number = int(number)
        if plant_name in plants.keys():
            update(plant_name, number)
        else:
            print("error")
    elif action == "Reset":
        plant_name = command[1]
        if plant_name in plants.keys():
            reset(plant_name)
        else:
            print("error")

print('Plants for the exhibition:')
for plant, plant_info in plants.items():
    if plant_info['all_ratings'] != 0 and len(plant_info['all_ratings']) != 0:
        average_rating = sum(plant_info['all_ratings']) / len(plant_info['all_ratings'])
        plant_info['all_ratings'] = average_rating
    else:
        plant_info['all_ratings'] = 0
    print(f'- {plant}; Rarity: {plant_info["rarity"]}; Rating: {plant_info["all_ratings"]:.2f}')