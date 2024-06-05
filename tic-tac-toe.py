
field = []
for _ in range(3):
    row = list(map(int, input().strip().split()))
    field.append(row)

winner_found = False
for i in range(3):
    if field[i][0] == field[i][1] == field[i][2] != 0:
        if field[i][0] == 1:
            print("First player won")
        else:
            print("Second player won")
        winner_found = True
        break

    if field[0][i] == field[1][i] == field[2][i] != 0:
        if field[0][i] == 1:
            print("First player won")
        else:
            print("Second player won")
        winner_found = True
        break


if not winner_found:
    if field[0][0] == field[1][1] == field[2][2] != 0:
        if field[0][0] == 1:
            print("First player won")
        else:
            print("Second player won")
    elif field[0][2] == field[1][1] == field[2][0] != 0:
        if field[0][2] == 1:
            print("First player won")
        else:
            print("Second player won")
    else:
        print("Draw!")
