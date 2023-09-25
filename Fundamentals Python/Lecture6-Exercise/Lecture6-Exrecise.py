# 1. Jenny's Secret Message

# name = input()
#
# if name == "Johnny":
#     print(f"Hello, my love!")
# else:
#     print(f"Hello, {name}!")


# 2. Drink Something

# age = int(input())
#
# if age <= 14:
#     print("drink toddy")
# elif age > 14 and age <= 18 :
#     print("drink coke")
# elif age > 18 and age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")

# 3. Chat Codes

# number = int(input())
#
# for _ in range(number):
#     new_number = int(input())
#     if new_number == 88:
#         print("Hello")
#     elif new_number == 86:
#         print("How are you?")
#     elif new_number < 88:
#         print("GREAT!")
#     else:
#         print("Bye.")


# 4. Maximum Multiple

# divisor = int(input())
# boundary = int(input())
#
# for largest_n in range(boundary, 1, -1):
#     if largest_n % divisor == 0:
#         break
# print(largest_n)

# 5.Orders
# •	Price per capsule - a floating-point number in the range [0.01…100.00]
# •	Days - integer in the range [1…31]
# •	Capsules, needed per day - integer in the range [1…2000]


# number_of_orders = int(input())
# total_price = 0
# for i in range(number_of_orders):
#     price_per_capsule = float(input())
#     days = int(input())
#     daily_capsules_needed = int(input())
#     if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1<= daily_capsules_needed <= 2000:
#         price = price_per_capsule * days * daily_capsules_needed
#         total_price += price
#         print(f"The price for the coffee is: ${price:.2f}")
#     else:
#        continue
#
# print(f"Total: ${total_price:.2f}")

# 6.	String Pureness

# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"

# num = int(input())
#
# for _ in range(num):
#     word = input()
#     if "," in word or "." in word or "_" in word:
#             print(f"{word} is not pure!")
#     else:
#             print(f"{word} is pure.")


# 7.	Double Char
# command = input()
#
# while command != "End":
#     string_name = command
#     if string_name != "SoftUni":
#       new_string = ""
#       for char in string_name:
#         new_string += char * 2
#       print(new_string)
#
#     command = input()


# 8.	How Much Coffee Do You Need?

# Solution1

# event = input()
# coffies = 0
#
# while event != "END":
#     if event.isupper():
#         if event == "CODING":
#             coffies += 2
#         elif event == "DOG":
#             coffies += 2
#         elif event == "CAT":
#             coffies += 2
#         elif event == "MOVIE":
#             coffies += 2
#     else:
#         if event == "coding":
#             coffies += 1
#         elif event == "dog":
#             coffies += 1
#         elif event == "cat":
#             coffies += 1
#         elif event == "movie":
#             coffies += 1
#
#     event = input()
#
# if coffies > 5:
#     print("You need extra sleep")
# else:
#     print(coffies)


# Solution2
# coffies = 0
# event = input()
# while event != "END":
#     if event.lower() == "coding" \
#             or event.lower() == "dog" \
#             or event.lower() == "cat" \
#             or event.lower() == "movie":
#         if event.islower():
#             coffies += 1
#         else:
#             coffies += 2
#     event = input()
#
# if coffies > 5:
#     print("You need extra sleep")
# else:
#     print(coffies)


                          #9.	Sorting Hat

# name = input()
#
# while name != "Welcome!":
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif len(name) > 6:
#         print(f"{name} goes to Hufflepuff.")
#
#     name = input()
#
# if name == "Welcome!":
#     print("Welcome to Hogwarts.")

                                #10.	* Mutate Strings
#kitty
#doggy
# first_string = input()
# second_string = input()
# last_printed_string = first_string
# for character in range(len(first_string)):
#     left_part = second_string[0:character + 1] # second_string[:character +1]....отначало докъдето сме му казали
#     right_part = first_string[character + 1:] # от където сме му казали до края
#     new_string = left_part +right_part
#     if new_string != last_printed_string:
#         print(new_string)
#         last_printed_string =new_string


                          #11.* Easter Bread
# Sollution 1 - dava 60%

# budget = float(input())
# flour_price_kg = float(input())
#
# eggs_pack_price = 0.75 * flour_price_kg
# milk_liter_price = 1.25 * flour_price_kg
#
# loaf_cost =  flour_price_kg + eggs_pack_price + (milk_liter_price / 4)
# loaves_cost = loaf_cost
# loaves_count = 0
# colored_eggs = 0
# money_left = 0
# while budget > loaves_cost:
#     colored_eggs += 3
#     if loaves_count != 0 and loaves_count % 3 == 0:
#         colored_eggs -= (loaves_count - 2)
#
#     money_left = budget - loaves_cost
#     loaves_count += 1
#     loaves_cost += loaf_cost
#
# print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
#
#                      #solution 2 - 100%
#
# budget = float(input())
# flour_price_kg = float(input())
#
# eggs_pack_price = 0.75 * flour_price_kg
# milk_liter_price = 1.25 * flour_price_kg
#
# loaf_cost =  flour_price_kg + eggs_pack_price + (milk_liter_price / 4)
#
# loaf_counter = 0
# colored_eggs = 0
#
# while budget > loaf_cost:
#
#     loaf_counter += 1
#     colored_eggs += 3
#     budget -= loaf_cost
#
#     if loaf_counter % 3 == 0:
#         colored_eggs -= loaf_counter - 2
#
# money_left = budget
#
# print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")




                          #12.	* Christmas Spirit

# quantity_of_decorations = int(input())
# remaning_days = int(input())
#
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price= 15
#
# total_spirit = 0
# total_cost = 0
#
# for current_day in range(1,remaning_days+1):
#     if current_day % 11 == 0:
#         quantity_of_decorations += 2
#     if current_day % 2 ==0:
#         total_cost += quantity_of_decorations * ornament_set_price
#         total_spirit +=5
#     if current_day % 3 == 0:
#         total_cost += quantity_of_decorations*(tree_garland_price + tree_skirt_price)
#         total_spirit += 10+3
#     if current_day % 5 == 0:
#         total_cost += quantity_of_decorations * tree_lights_price
#         total_spirit += 17
#         if current_day % 3 == 0:
#             total_spirit += 30
#     if current_day % 10 == 0:
#         total_spirit -= 20
#         total_cost+= tree_skirt_price + tree_lights_price + tree_garland_price
# if remaning_days % 10 == 0 :
#     total_spirit -= 30
# print(f"Total cost: {total_cost}")
# print((f"Total spirit: {total_spirit}"))


