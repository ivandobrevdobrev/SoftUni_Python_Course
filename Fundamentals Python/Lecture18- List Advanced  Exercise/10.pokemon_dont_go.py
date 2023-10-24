pokemon = list(map(int, input().split()))
sum_removed_elements = 0
while True:

    if len(pokemon) == 0:
        print(sum_removed_elements)
        break
    index = int(input())
    if index < 0:

        removed_element = pokemon[0]
        sum_removed_elements += removed_element
        pokemon.pop(0)

        pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]
        last_element = pokemon[-1]
        pokemon.insert(0, last_element)
    elif index >= len(pokemon):

        removed_element = pokemon[-1]

        sum_removed_elements += removed_element
        pokemon.pop(-1)
        pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]
        first_element = pokemon[0]
        pokemon.append(first_element)
    else:
        removed_element = pokemon[index]
        sum_removed_elements += removed_element
        pokemon.pop(index)
        pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]



# using functions NOT working for the moment

# def index_less_0(pokemon: list):
#     sum_removed_elements = 0
#     removed_element = pokemon[0]
#     sum_removed_elements += removed_element
#     pokemon.pop(0)
#
#     pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]
#     last_element = pokemon[-1]
#     pokemon.insert(0, last_element)
#     return pokemon, sum_removed_elements
#
#
# def index_greater_0(pokemon: list):
#     sum_removed_elements = 0
#     removed_element = pokemon[-1]
#
#     sum_removed_elements += removed_element
#     pokemon.pop(-1)
#     pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]
#     first_element = pokemon[0]
#     pokemon.append(first_element)
#     return pokemon, sum_removed_elements
#
#
# def other_cases(index, pokemon):
#     sum_removed_elements = 0
#     removed_element = pokemon[index]
#     sum_removed_elements += removed_element
#     pokemon.pop(index)
#     pokemon = [el + removed_element if el <= removed_element else el - removed_element for el in pokemon]
#     return pokemon, sum_removed_elements
#
#
# pokemon = list(map(int, input().split()))
# sum_removed_elements = 0
#
# while True:
#
#     if len(pokemon) == 0:
#         print(sum_removed_elements)
#         break
#     index = int(input())
#     if index < 0:
#         index_less_0(pokemon)
#     elif index >= len(pokemon):
#         index_greater_0(pokemon)
#     else: other_cases(index,pokemon)
