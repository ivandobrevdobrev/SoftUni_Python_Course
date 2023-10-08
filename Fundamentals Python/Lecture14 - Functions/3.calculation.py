operator = input()
num1 = int(input())
num2 = int(input())

#multiply", "divide", "add", "subtract
def calculator (num1, num2,operator):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return  int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
print(calculator(num1,num2,operator))