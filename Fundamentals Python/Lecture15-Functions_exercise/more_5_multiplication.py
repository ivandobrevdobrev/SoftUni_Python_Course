# def multiplication_sign(num1, num2, num3: int):
#     if num1 == 0 or num2 == 0 or num3 == 0:
#         return "zero"
#     elif num1 < 0 or num2 < 0 or num3 < 0:
#         return "negative"
#     else:
#         return "positive"
#
#
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
# result = multiplication_sign(n1, n2, n3)
# print(result)

def find_product_sign(a, b, c):
    # Check the number of negative values
    num_negatives = sum(1 for num in (a, b, c) if num < 0)

    if num_negatives % 2 == 0:
        return "Positive"
    else:
        return "Negative"


# Input three numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

result = find_product_sign(a, b, c)
print(f"The product of {a}, {b}, and {c} is {result}.")
