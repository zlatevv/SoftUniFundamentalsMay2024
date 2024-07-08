my_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
legendary_item = ""
legendary_obtained = False

while not legendary_obtained:
    items = input().split()

    for i in range(0, len(items), 2):
        value = int(items[i])
        item = items[i + 1].lower()

        if item in my_dict:
            my_dict[item] += value
            if my_dict[item] >= 250:
                legendary_obtained = True
                my_dict[item] -= 250
                if item == "shards":
                    legendary_item = "Shadowmourne"
                elif item == "fragments":
                    legendary_item = "Valanyr"
                elif item == "motes":
                    legendary_item = "Dragonwrath"
                print(f"{legendary_item} obtained!")
                break
        else:
            if item in junk_items:
                junk_items[item] += value
            else:
                junk_items[item] = value

    if legendary_obtained:
        break

# Print remaining key materials
print(f"shards: {my_dict['shards']}")
print(f"fragments: {my_dict['fragments']}")
print(f"motes: {my_dict['motes']}")

# Print junk items
for k, v in junk_items.items():
    print(f"{k}: {v}")
