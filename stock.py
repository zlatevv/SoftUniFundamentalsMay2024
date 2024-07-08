data = input().split()
stock = {}
searched_products = input().split()
for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    stock[product] = quantity
for product in searched_products:
    if product in stock.keys():
        quantity = stock[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
