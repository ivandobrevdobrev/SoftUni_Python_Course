# coffee", "coke", "water", or "snacks", and a quantity

product = input()
quantity = int(input())


def total_cost(a, b):
    if a == "coffee":
        return f"{1.50 * b:.2f}"
    elif a == "water":
        return f"{1.00 * b:.2f}"
    elif a == "snacks":
        return f"{2.00 * b:.2f}"
    elif a == "coke":
        return f"{1.40 * b:.2f}"


print(total_cost(product, quantity))
