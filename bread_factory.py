energy = 100
coins = 100
closed = False
all_events = input().split("|")
for events in all_events:
    events = events.split("-")
    event = events[0]
    number = int(events[1])
    if event == "rest":
        
        gained_energy = min(100 - energy, number)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        ingredient = events[0]
        if coins >= number:
            print(f"You bought {ingredient}.")
            coins -= number
        else:
            closed = True
            print(f"Closed! Cannot afford {ingredient}.")
            break
if not closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
    