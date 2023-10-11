def cartesian_point(num1,num2:float):
    distance = num1 ** 2 + num2 ** 2
    return distance


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

distance_1 = cartesian_point(x1,y1)
distance_2 = cartesian_point(x2,y2)
distance_3 = cartesian_point(x3,y3)
distance_4 = cartesian_point(x4,y4)

line1 = distance_1 + distance_2
line2 = distance_3 + distance_4

if line1 >= line2:
    if distance_1 <= distance_2:
        print(f'({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})')
    else:
        print(f'({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})')
else:
    if distance_3 <= distance_4:
        print(f'({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})')
    else:
        print(f'({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})')

