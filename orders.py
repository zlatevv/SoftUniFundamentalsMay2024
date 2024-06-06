def coffee(number):
    cost = 1.50 * number
    return f"{cost:.2f}"
def water(number):
    cost = 1.00 * number
    return f"{cost:.2f}"
def coke(number):
    cost = 1.40 * number
    return f"{cost:.2f}"
name = input()
quantity = int(input())
if name == "coffee":
    print(coffee(quantity))
elif name == "water":
    print(water(quantity))
elif name == "coke":
    print(coke(quantity))
