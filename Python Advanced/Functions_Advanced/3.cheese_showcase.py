def sorting_cheeses(**kwargs):
    result = ""
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    # сортираме 1во по броя на парчетата сирене( дължината на value) на обратно (-len(kvp[1])
    # после ако има с едналва дължина , сорт по Key по азбучен ред kvp[0])
    # тоест ако Пармеза и Моцарелата бяха с еднкава дължина - 1во Моцарелата после пармезана

    for cheese, quantities in sorted_result:
        result += cheese + "\n"  # за да може после да се притне на нов ред
        for quantity in sorted(quantities, reverse=True):  # иска се да се отпечат descending
            result += f"{quantity}\n"  # put everything in result,so we can return it
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
