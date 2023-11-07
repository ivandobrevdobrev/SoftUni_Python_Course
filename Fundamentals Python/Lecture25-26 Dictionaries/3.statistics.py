products_all = {}

while True:
    command = input()
    if command == "statistics":
        break
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product in products_all:
        products_all[product] += quantity
    else:
        products_all[product] = quantity
product_count = len(products_all)  # броя на ключовете е равен на дължината на речника
quantity_sum = sum(products_all.values())  # сумата на всички ст-сти

print("Products in stock:")

for product,quantity in products_all.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {product_count}")
print(f"Total Quantity: {quantity_sum}")