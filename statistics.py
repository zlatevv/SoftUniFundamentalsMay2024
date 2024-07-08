stock = {}
while True:
    data = input().split(": ")
    if data[0] == "statistics":
        break
    product = data[0]
    quantity = int(data[1])
    if product not in stock.keys():
        stock[product] = quantity
    else:
        stock[product] += quantity
print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")

