quantity_of_decorations = int(input())
days_until_christmas = int(input())
ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17
total_cost = 0
total_spirit = 0
for i in range(1, days_until_christmas + 1):
    if i % 11 == 0:
        quantity_of_decorations += 2
    if i % 2 == 0:
        total_cost += ornament_price * quantity_of_decorations
        total_spirit += ornament_points
    if i % 3 == 0:
        total_cost += tree_skirt_price * quantity_of_decorations + tree_garland_price * quantity_of_decorations
        total_spirit += tree_skirt_points + tree_garland_points
    if i % 5 == 0:
        if i % 15 == 0:
            total_spirit += 30
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if i % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")