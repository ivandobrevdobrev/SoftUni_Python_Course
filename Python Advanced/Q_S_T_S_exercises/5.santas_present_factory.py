from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = []
presents_dict = {}

craft_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic:

    # material = materials.pop() if magic[0] or not materials[-1] else 0  #  shorter version of the conditions below
    # magic_num = magic.popleft() if material or not magic[0] else 0  # 0
    #
    # if not magic_num:
    #     continue

    material = materials.pop()
    magic_num = magic.popleft()

    if material == 0 and magic_num == 0:
        continue
    if magic_num == 0:
        materials.append(material)
        continue
    if material == 0:
        magic.appendleft(magic_num)
        continue

    mix = material * magic_num

    if mix < 0:
        sum_elements = material + magic_num
        materials.append(sum_elements)

    elif mix > 0 and mix not in craft_presents.keys():
        materials.append(material + 15)
    else:
        presents.append(craft_presents[mix])

if {"Wooden train", "Doll"}.issubset(presents) or {"Teddy bear", "Bicycle"}.issubset(presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

#Sorting and counting elements

for toy in presents:
    if toy not in presents_dict:
        presents_dict[toy] = presents.count(toy)
for toy, occ in sorted(presents_dict.items()):
    print(f"{toy}: {occ}")

# version2 of sorting
# [print(f"{toy}: {presents.count(toy)}") for toy in sorted(set(presents))]
