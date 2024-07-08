orders = {}
while True:
    data = input().split()
    if data[0] == "buy":
        break
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if name in orders.keys():
        current_quantity= orders[name][1]
        orders[name] = [price, current_quantity + quantity]
    else:
        orders[name] = [price, quantity]
for product, cost in orders.items():
    money = cost[0] * cost[1]
    print(f"{product} -> {money:.2f}")