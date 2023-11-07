elements = input().split()

stock ={}

for i in range(0, len(elements),2):
    product = elements[i]
    quantity = elements[i+1]
    stock[product] = quantity

searched_product = input().split()

for product in searched_product:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")