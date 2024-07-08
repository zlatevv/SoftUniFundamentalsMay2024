materials = {}
while True:
    material = input()
    if material == "stop":
        break
    quantity = int(input())
    if material not in materials:
        materials[material] = quantity
    else:
        materials[material] += quantity
for material, quantity in materials.items():
    print(f"{material} -> {quantity}")