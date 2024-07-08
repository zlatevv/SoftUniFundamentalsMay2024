elements = input().split()
my_dict = {}
for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = int(elements[i + 1])
    my_dict[product] = quantity
print(my_dict)