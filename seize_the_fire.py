fire_cells = input().split("#")
water = int(input())
is_valid = True
efford = 0
total_fire = 0
cells_put_out = []
for fires in fire_cells:
    fires = fires.split(" = ")
    type_of_fire = fires[0]
    range_of_fire = int(fires[1])
    if type_of_fire == "High":
        if range_of_fire > 125 or range_of_fire < 81:
            is_valid = False
    elif type_of_fire == "Medium":
        if range_of_fire > 80 or range_of_fire < 51:
            is_valid = False
    elif type_of_fire == "Low":
        if range_of_fire > 50 or range_of_fire < 1:
            is_valid = False
    if is_valid:
        if range_of_fire > water:
            continue
        water -= range_of_fire
        efford += 0.25 * range_of_fire
        total_fire += range_of_fire
        cells_put_out.append(range_of_fire)
    is_valid = True
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {efford:.2f}")
print(f"Total Fire: {total_fire}")
    