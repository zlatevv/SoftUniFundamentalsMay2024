animals = input().split(", ")
wolf_position = animals.index("wolf")
if wolf_position == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(animals) - wolf_position - 1}! You are about to be eaten by a wolf!")
        