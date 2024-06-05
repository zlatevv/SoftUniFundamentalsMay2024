data = input().split("|")
budget = int(input())
is_valid = True
old_total = 0
new_total = 0
new_prices = []
for items in data:
    items = items.split("->")
    type = items[0]
    price = float(items[1])
    if type == "Clothes" and price <= 50:
        
        if budget >= price:
            
            old_total += price
            budget -= price
            new_price = price * 1.4
            new_prices.append(f"{new_price:.2f}")
            new_total += new_price
    elif type == "Shoes" and price <= 35:
       
        if budget >= price:
            old_total += price
            budget -= price
            new_price = price * 1.4
            new_prices.append(f"{new_price:.2f}")
            new_total += new_price
    elif type == "Accessories" and price <= 20.50:
        
        if budget >= price:
            old_total += price
            budget -= price
            new_price = price * 1.4
            new_prices.append(f"{new_price:.2f}")
            new_total += new_price
profit = new_total - old_total
new_budget = budget + new_total
    
            
print(*new_prices)
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

