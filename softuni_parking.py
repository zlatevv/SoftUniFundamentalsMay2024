parking_place = {}
commands = int(input())
for _ in range(commands):
    command = input().split()
    tip = command[0]
    name = command[1]
    if tip == "register":
        plate_number = command[2]
        if name in parking_place:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking_place[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
    elif tip == "unregister":
        if name not in parking_place:
            print(f"ERROR: user {name} not found")
        else:
            del parking_place[name]
            print(f"{name} unregistered successfully")
for name, plating_number in parking_place.items():
    print(f"{name} => {plating_number}")

