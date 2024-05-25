n = int(input())
total_capacity = 255
used_capacity = 0
for _ in range(0, n):
    litters_to_fill = int(input())
    if used_capacity + litters_to_fill <= total_capacity:
        used_capacity += litters_to_fill
    else:
        print("Insufficient capacity!")
print(used_capacity)
