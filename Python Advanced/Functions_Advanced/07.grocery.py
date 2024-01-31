def grocery_store(**products):   # сортираме 1во по брой продукти, после по дължина на думата на продукта и накрая по азбучен ред
    products = sorted(products.items(), key=lambda x:(-(x[1]), -len(x[0]), x[0]))

    result = []
    for product, qty in products:  # не пишем .items защото SORTED връща List ot Tuples
        result.append(f"{product}: {qty}")
    return "\n".join(result)
# solution2 with comprehension
    #return "\n".join(f'{p} {q}'for p,q in products)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
