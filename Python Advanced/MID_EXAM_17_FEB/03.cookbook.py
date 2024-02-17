def cookbook(*dish_info):
    dishes = {}

    result = ""
    for recipe_name, cousine, ingredients in dish_info:
        if cousine not in dishes:
            dishes[cousine] = []
        dishes[cousine].append((recipe_name, ingredients))

    sorted_dishes = sorted(dishes.items(), key=lambda x: (-len(x[1]), x[0]))

    for cuisine, info in sorted_dishes:
        result += f"{cuisine} cuisine contains {len(info)} recipes:\n"
        for name, ingredients in sorted(info, key=lambda x: x[0]):
            result += f"  * {name} -> Ingredients: {', '.join(x for x in ingredients)}\n"
    return result


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#
# ))


print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
