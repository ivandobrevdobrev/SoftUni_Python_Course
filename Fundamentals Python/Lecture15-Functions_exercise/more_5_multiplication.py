def multiplication_sign(num1, num2, num3: int):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif num1 < 0 or num2 < 0 or num3 < 0:
        return "negative"
    else:
        return "positive"


n1 = int(input())
n2 = int(input())
n3 = int(input())

result = multiplication_sign(n1, n2, n3)
print(result)
