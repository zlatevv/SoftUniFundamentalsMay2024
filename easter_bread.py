budget = float(input())
price_for_flour_per_kilo = float(input())
price_per_pack_of_eggs = price_for_flour_per_kilo * 0.75
price_of_milk_per_litter = price_for_flour_per_kilo * 0.25 + price_for_flour_per_kilo
egg_count = 0
bread = 0
money_for_bread = price_per_pack_of_eggs + price_of_milk_per_litter * 0.25 + price_for_flour_per_kilo
while budget >= money_for_bread:
    budget -= money_for_bread
    egg_count += 3
    bread += 1
    if bread % 3 == 0:
        lost_eggs = bread - 2
        egg_count -= lost_eggs
print(f"You made {bread} loaves of Easter bread! Now you have {egg_count} eggs and {budget:.2f}BGN left.")