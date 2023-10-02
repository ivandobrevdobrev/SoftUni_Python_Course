items = input().split("|")
budget = float(input())
final_budget = 0
ticket_price = 150
new_prices = []
profit = 0
sell_price = 0


for item in items:
    type,buying_price = item.split("->")
    buying_price =float(buying_price)
    price_is_valid = False

    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid =True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid :
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            new_prices.append(sell_price)


final_budget = budget + sum(new_prices)
for new_price in new_prices:
    print(f"{new_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if final_budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

          # SOLUTION 2 - по-подробно, без булева
#
# items = input().split("|")
# budget = float(input())
# final_budget = 0
# ticket_price = 150
# new_prices = []
# profit = 0
# sell_price = 0
#
#
# for item in items:
#     current_item = item.split("->")
#
#     if current_item[0] == "Clothes":
#         if float(current_item[1]) <= 50.00:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
#     elif current_item[0] == "Shoes":
#         if float(current_item[1]) <= 35.00:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
#     elif current_item[0] == "Accessories":
#         if float(current_item[1]) <= 20.50:
#             if budget >= float(current_item[1]):
#                 sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#                 profit += sell_price - float(current_item[1])
#                 new_prices.append(sell_price)
#                 budget -= float(current_item[1])
#
# final_budget = budget + sum(new_prices)
#
# for new_price in new_prices:
#     print(f"{new_price:.2f}", end=" ")
# print()
#
# print(f"Profit: {profit:.2f}")
# if final_budget >= ticket_price:
#     print("Hello, France!")
# else:
#     print("Not enough money.")


# Solution 3- almost same as 2

# items = input().split("|")
# budget = float(input())
# final_budget = 0
# ticket_price = 150
# new_prices = []
# profit = 0
# sell_price = 0
#
# for item in items:
#     current_item = item.split("->")
#     if budget < float(current_item[1]):
#         continue
#     if current_item[0] == "Clothes" and float(current_item[1]) <= 50.00:
#         sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#         profit += sell_price - float(current_item[1])
#         new_prices.append(sell_price)
#         budget -= float(current_item[1])
#
#     elif current_item[0] == "Shoes" and float(current_item[1]) <= 35.00:
#         sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#         profit += sell_price - float(current_item[1])
#         new_prices.append(sell_price)
#         budget -= float(current_item[1])
#
#     elif current_item[0] == "Accessories" and float(current_item[1]) <= 20.50:
#         sell_price = float(current_item[1]) + (float(current_item[1]) * 0.40)
#         profit += sell_price - float(current_item[1])
#         new_prices.append(sell_price)
#         budget -= float(current_item[1])
#
# final_budget = budget + sum(new_prices)
# for new_price in new_prices:
#     print(f"{new_price:.2f}", end=" ")
# print()
# print(f"Profit: {profit:.2f}")
# if final_budget >= ticket_price:
#     print("Hello, France!")
# else:
#     print("Not enough money.")