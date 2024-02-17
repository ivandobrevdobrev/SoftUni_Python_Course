def cookbook(*args):
    cookbook_dict = {}
    res = ''

    for recipe, cuisine, ingredients in args:
        if cuisine not in cookbook_dict.keys():
            cookbook_dict[cuisine] = {}

        cookbook_dict[cuisine].update({recipe: ingredients})

    sorted_cookbook = sorted(cookbook_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    sorted_dict = dict(sorted_cookbook)

    for cuisine, recipes in sorted_dict.items():
        res += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for reci, ingredient in sorted(recipes.items()):
            res += f"  * {reci} -> "
            res += f"Ingredients: {', '.join(va for va in ingredient)}\n"

    return res

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
