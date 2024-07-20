import re
total = 0
furniture = []
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
line = input()
while line != "Purchase":
    match = re.search(pattern, line)
    if match:
        name, price, quantity = match.groups()
        total += float(price) * int(quantity)
        furniture.append(name)
    line = input()
print("Bought furniture:")
for mebel in furniture:
    print(mebel)
print(f"Total money spend: {total:.2f}")