def accommodate_new_pets(capacity: int, weight_limit: float, *pet_info):
    number_pets = len(pet_info)
    accommodated_pets = {}
    results = ""
    for pet_type, weigth in pet_info:
        if weigth > weight_limit:
            number_pets -= 1
            continue
        if pet_type not in accommodated_pets.keys():
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1

        if capacity <= 0:
            break
    if number_pets == sum(x for x in accommodated_pets.values()):
        results = f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n"
        for pet_type, number in sorted(accommodated_pets.items()):
            results += f"{pet_type}: {number}" + "\n"
    else:
        results = "You did not manage to accommodate all pets!\nAccommodated pets:\n"
        for pet_type, number in sorted(accommodated_pets.items()):
            results += f"{pet_type}: {number}" + "\n"
    return results


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))


# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))
