grour_size = int(input())
days_of_adventure = int(input())
coins = 0
for day in range(1,days_of_adventure +1):
    coins += 50
    coins -= grour_size * 2
    if day % 10 == 0:
        grour_size -= 2
    if day % 15 == 0:
        grour_size += 5
    if day % 3 == 0:
        coins -= grour_size * 3
    if day % 5 == 0:
        coins += grour_size * 20
        if day % 3 == 0:
            coins -= grour_size * 2

coins_per_companion = coins // grour_size #  int(coins / group size)

print(f"{grour_size} companions received {coins_per_companion} coins each.")


