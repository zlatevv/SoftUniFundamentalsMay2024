gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        gift = command[1]
        while gift in gifts:
            gifts[gifts.index(gift)] = None
            
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index <= len(gifts) - 1:
            gifts[index] = gift
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts[-1] = gift
    command = input()
while None in gifts:
    gifts.remove(None)
print(*gifts)