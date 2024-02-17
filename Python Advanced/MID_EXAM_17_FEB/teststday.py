# for cuisine in sorted_dishes:
#     result += f"{cuisine[0]} cuisine contains {len(cuisine[1])} recipes:\n"
#     for name, ingredients in sorted(cuisine[1], key=lambda x: x[0]):
#         result += f"  * {name} -> Ingredients: {', '.join(x for x in ingredients)}\n"
# return result

# for cuisine, info in sorted_dishes:
#     result += f"{cuisine} cuisine contains {len(info)} recipes:\n"
#     for name, ingredients in sorted(info, key=lambda x: x[0]):
#         result += f"  * {name} -> Ingredients: {', '.join(x for x in ingredients)}\n"
# return result