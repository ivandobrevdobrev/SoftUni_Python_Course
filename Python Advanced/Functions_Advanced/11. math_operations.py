def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())  # [a, s, d, m]  изваждаме си ключовете в лист  a=1, s=7, d=33, m=15

    for i in range(len(numbers)):
        key = keys[i % 4]  # 0, 1, 2, 3  за да може да вземем indexes na asdm, всяко число делено модулно на друго число дава другото число -1
        # i= 0 % 4 = 0 -> keys[0] - a
        # i= 1 % 4 = 1 -> keys[1] - s
        # i= 2 % 4 = 2 -> keys[2] - d
        # i= 3 % 4 = 3 -> keys[3] - m
        if key == "a":
            kwargs[key] += numbers[i]
        elif key == "s":
            kwargs[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))