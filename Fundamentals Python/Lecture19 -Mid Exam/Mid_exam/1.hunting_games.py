days = int(input())
people = int(input())
total_energy = float(input())
water_daily_person = float(input())
food_daily_person = float(input())

total_water = days * people * water_daily_person
total_food = days * people * food_daily_person

for day in range(1, days + 1):
    energy_loss = float(input())
    total_energy -= energy_loss
    if total_energy <= 0:
        break
    if day % 2 == 0:
        total_energy += 0.05 * total_energy
        total_water -= 0.30 * total_water
    if day % 3 == 0:
        total_energy += 0.10 * total_energy
        total_food -= total_food / people
if total_energy > 0:
    print(f"You are ready for the quest. You will be left with - {total_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
