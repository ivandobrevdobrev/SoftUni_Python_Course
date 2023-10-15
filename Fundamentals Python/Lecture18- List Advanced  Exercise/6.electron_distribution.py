number_of_electrons = int(input())
shells =[]

for shell in range(1, number_of_electrons +1):
    current_max_electrons = 2 * shell ** 2
    if number_of_electrons >= current_max_electrons:
        shells.append(current_max_electrons)
        number_of_electrons -= current_max_electrons
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)
