from collections import deque

amount_of_money = list(int(x) for x in input().split())
prices = deque(int(x) for x in input().split())

food_eaten = 0
while amount_of_money and prices:
    current_money = amount_of_money.pop()
    current_price = prices.popleft()

    if current_money == current_price:
        food_eaten += 1
    elif current_money > current_price:
        diff = current_money - current_price
        if amount_of_money:
            amount_of_money[-1] += diff
        food_eaten += 1
    else:
        continue
if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")
elif food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {food_eaten} foods.")


