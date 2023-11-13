def addition(number_one, number_two):
    return f"Result is {number_one + number_two}"


def subtraction(number_one, number_two):
    return f"Result is {number_one - number_two}"


def multiplication(number_one, number_two):
    return f"Result is {number_one * number_two}"


def division(number_one, number_two):
    return f"Result is {number_one / number_two}"


def valid_option_chosen():
    operation = int(
        input('choose operation :\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division  '))
    if operation not in range(1, 5):
        operation = int(input('choose one of the four options'))
    first_number = int(input("enter first number:  "))
    second_number = int(input("enter second number:  "))
    calculator(first_number, second_number, operation)


def calculator(first_number, second_number, operation):
    if operation == 1:
        print(addition(first_number, second_number))
    elif operation == 2:
        print(subtraction(first_number, second_number))
    elif operation == 3:
        print(multiplication(first_number, second_number))
    elif operation == 4:
        print(division(first_number, second_number))

valid_option_chosen()


