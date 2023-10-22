total_price = 0

while True:

    command = input()

    if command == "special":
        if total_price == 0:
            print("Invalid order!")
            break
        else:

            total_price_with_tax = total_price * 1.20
            taxes = total_price_with_tax - total_price
            total_price_with_tax = total_price_with_tax * 0.90
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {total_price_with_tax:.2f}$")
            break
    if command == "regular":
        if total_price == 0:
            print("Invalid order!")
            break
        else:
            total_price_with_tax = total_price * 1.20
            taxes = total_price_with_tax - total_price
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {total_price_with_tax:.2f}$")
            break

    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue

    total_price += price
