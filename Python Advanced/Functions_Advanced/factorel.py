# def factorial(number):
#     if not isinstance(number, int) or number < 0:
#         return f"Sorry. 'number' is incorrect."
#     def inner_factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact = fact * i
#         return fact
#     return inner_factorial(number)
# print(factorial(5))


# Return inner function

def calculator(operator):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction


operation = calculator("+") # извикаваме основната функция, която реферира(връща) към вътрешна функция
result = operation(2, 3)    # реферираме към вътрешната функция , чрез operation
print(result)
