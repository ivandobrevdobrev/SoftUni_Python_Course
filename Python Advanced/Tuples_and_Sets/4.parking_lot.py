n = int(input())

cars =set()

for _ in range(n):
    direction, car_num = input().split(", ")

    if direction == "IN":
        cars.add(car_num)
    elif direction == "OUT":
        cars.remove(car_num)

if cars:
    for car in cars:
        print(car)
else:
    print(f"Parking Lot is Empty")