def cartesian_point(num1,num2:float):
    origin = num1 ** 2 + num2 ** 2
    return origin


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


distance_1 = cartesian_point(x1,y1)
distance_2 = cartesian_point(x2,y2)

if distance_1 < distance_2:
    print(f"({int(x1)}, {int(y1)})")
elif distance_1 == distance_2:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")