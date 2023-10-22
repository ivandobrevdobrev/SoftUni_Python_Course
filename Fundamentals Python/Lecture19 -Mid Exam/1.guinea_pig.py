food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000

weight_gr = float(input()) * 1000
month = 30
is_food_enough = True

for day in range(1, month + 1):
    food_gr -= 300
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        is_food_enough = False
        break
    if day % 2 == 0:
        hay_gr -= 0.05 * food_gr
    if day % 3 == 0:
        cover_gr -= weight_gr / 3

if is_food_enough:
    print(
        f"Everything is fine! Puppy is happy! Food: {food_gr / 1000:.2f}, Hay: {hay_gr / 1000:.2f}, Cover: {cover_gr / 1000:.2f}.")
else:
    print('Merry must go to the pet store!')
