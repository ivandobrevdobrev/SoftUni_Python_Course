from collections import deque

worms = [int(el) for el in input().split()]
holes = deque(int(x) for x in input().split())

matches_count = 0
no_fits_hole = 0
while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches_count += 1
        continue
    else:
        worms.append(current_worm - 3)
        if worms[-1] <= 0:
            no_fits_hole += 1
            worms.pop()


if matches_count > 0:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")
if not worms and no_fits_hole == 0:
    print("Every worm found a suitable hole!")
elif not worms and no_fits_hole > 0:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
# 9 5 8 13
# 13 8 5 6
