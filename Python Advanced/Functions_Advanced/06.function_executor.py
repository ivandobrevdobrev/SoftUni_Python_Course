def func_executor(*data):  # получаваме данни- вслучая 2 функции sum_numbers, (1, 2) и multiply_numbers, (2, 4)
    result = []

    for func, arguments in data:  # обхождаме всяка функция и я извикваме и апендаваме резултата
        result.append(
            f"{func.__name__} - {func(*arguments)}")  # взимаме името като стринг и изпълняваме ф-ята и взимаме резулатта
        #  името на ф-ята     #sum_numbers, (1, 2) -> 3 ( извикваме я)
    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
