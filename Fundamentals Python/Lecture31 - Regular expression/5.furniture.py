import re

bought_furniture = []
total_cost = 0
command = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'  # ползваме d* за да избегнем сума 300.(точка) * е да го има 0 или повече
while command != "Purchase":
    match = re.search(pattern,command)
    if match:
        furniture, price, quantity = match.groups()  # като знаме как са наредени групите може директно да ги присвоим
        #furniture = match.group(1)
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

    command = input()

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')


# >>Sofa<<312.23!3
# >>TV<<300.!5
# >Invalid<<!5
# Purchase