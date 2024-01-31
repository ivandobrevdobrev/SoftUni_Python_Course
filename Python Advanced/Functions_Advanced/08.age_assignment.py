def age_assignment(*names, **ages):
    results =[]

    for letter, age in ages.items():
        for name in names:
            if name.startswith(letter):
                results.append(f"{name} is {age} years old.")
                break # breakvame - защото ако сме намерили буквата няма нужда да итерираме нататък
    return "\n".join(sorted(results))



print(age_assignment("Peter", "George", G=26, P=19))