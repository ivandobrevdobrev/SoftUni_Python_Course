from collections import deque

monster = deque(int(x) for x in input().split(","))
soldier = [int(y) for y in input().split(",")]
monsters_killed = 0

while monster and soldier:
    current_monster = monster.popleft()
    current_soldier = soldier.pop()

    if current_soldier >= current_monster:
        monsters_killed += 1
        remaining_strike = current_soldier - current_monster
        if soldier:
            soldier[-1] += remaining_strike
        else:
            if remaining_strike > 0:
                soldier.append(remaining_strike)
    elif current_monster > current_soldier:
        remaining_armour = current_monster - current_soldier
        monster.append(remaining_armour)
if not monster:
    print("All monsters have been killed!")
if not soldier:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")

