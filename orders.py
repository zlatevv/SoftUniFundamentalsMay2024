number_of_orders = int(input())
total = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= capsules_needed_per_day <= 2000:
        continue
    price = price_per_capsule * days * capsules_needed_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")