from collections import deque

initial_fuel = list(int(x) for x in input().split())
additional_comsumption_index = deque(int(x) for x in input().split())
quantities_needed = deque(int(x) for x in input().split())
altitudes = 0
while initial_fuel and additional_comsumption_index:
    current_fuel = initial_fuel[-1]
    current_consumption_index = additional_comsumption_index[0]
    current_quantity_needed = quantities_needed[0]

    if current_fuel - current_consumption_index >= current_quantity_needed:
        altitudes += 1
        initial_fuel.pop()
        additional_comsumption_index.popleft()
        quantities_needed.popleft()
        print(f"John has reached: Altitude {altitudes}")
    else:
        print(f"John did not reach: Altitude {altitudes + 1}")
        break

if quantities_needed and altitudes > 0:
    print(f"John failed to reach the top.\n"
          f"Reached altitudes: {', '.join(f'Altitude {x}' for x in range(1, altitudes + 1))}")
elif altitudes == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if not quantities_needed:
    print("John has reached all the altitudes and managed to reach the top!")
