products = {}             #Nested Dictionaries

while True:
    command = input()
    if command == "buy":
        break
    product, price, quantity = command.split()   # Beer ,1.2 ,  550
    price = float(price)
    quantity = int(quantity)
    
    if product not in products:
        products[product] ={}                   #{'Beer': {}
        products[product][price] = quantity     #{'Beer': {1.2: 550}
    else:
        for key in products[product].keys(): # iterate in teh Nested dict  {1.2:550}
            if float(key) != price:   # if 1.2 not equal to the new input ( 2.4)
                current_quantity = products[product].pop(key)  #remove the key '1.2' but keep the its value to be used below
                products[product][price] = quantity + current_quantity
                break
            else:
                products[product][price] += quantity

for product_name,values in products.items():
    for single_price,quantity in values.items():
        total_price = float(single_price) * int(quantity)
        print(f"{product_name} -> {total_price:.2f}")

print(some_list)
#{'Beer': {1.2: 550}, 'Water': {1.25: 200}, 'IceTea': {0.5: 220}}