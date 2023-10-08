def calculate_factorial(number):
    for current_number in range(1,number): # ostawame da e number za da ne go vzeme. tyi kato zapochvame umnojawame number po vsi4ki ostanali
        number *= current_number
    return number


first_num = int(input())
second_num = int(input())

first_factorial = calculate_factorial(first_num)
second_factorial = calculate_factorial(second_num)

result = print(f"{first_factorial/second_factorial:.2f}")