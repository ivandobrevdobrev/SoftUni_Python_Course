def castspell(hero_name, points, spell_name):
    if heroes[hero_name][1] >= points:
        heroes[hero_name][1] -= points
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(hero_name, amount, attacker):
    heroes[hero_name][0] -= amount
    if heroes[hero_name][0] > 0:
        print(f"{hero_name} was hit for {amount} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
    else:
        heroes.pop(hero_name)
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(hero_name, amount):
    recovered_amount = min(200 - heroes[hero_name][1], amount)
    heroes[hero_name][1] = min((amount + heroes[hero_name][1]), 200)
    print(f"{hero_name} recharged for {recovered_amount} MP!")


def heal(hero_name, amount):
    recovered_amount = min(100 - heroes[hero_name][0], amount)
    heroes[hero_name][0] = min((amount + heroes[hero_name][0]), 100)
    print(f"{hero_name} healed for {recovered_amount} HP!")


n = int(input())
heroes = {}

for i in range(n):
    hero_name, hp_points, mp_points = input().split()
    heroes[hero_name] = [int(hp_points), int(mp_points)]
while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    action = command[0]
    if action == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        castspell(hero_name, mp_needed, spell_name)
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        take_damage(hero_name, damage, attacker)
    elif action == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        recharge(hero_name, amount)
    elif action == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        heal(hero_name,amount)
for hero, points in heroes.items():
    print(hero)
    print(f"  HP: {points[0]}")
    print(f"  MP: {points[1]}")
