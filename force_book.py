force_users = {}
while True:
    data = input()
    if data == "Lumpawaroo":
        break
    if " | " in data:
        data = data.split(" | ")
        force_side = data[0]
        force_user = data[1]
        if force_side not in force_users and force_user not in force_users:
            force_users[force_side] = [force_user]
        elif force_user not in force_users:
            force_users[force_side].append(force_user)
        elif force_user in force_users.values():
            continue
    elif " -> " in data:
        data = data.split(" -> ")
        force_user = data[0]
        force_side = data[1]
        if force_user in force_users:
            current_side = force_users[force_user]
            if current_side != force_side:
                force_users[current_side].remove(force_user)
                force_users[force_side].append(force_user)
                force_users[force_user] = force_side
        elif force_user not in force_users:
            force_users[force_side].append(force_user)
        elif force_user not in force_users and force_side not in force_users:
            force_users[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")
for side, members in force_users.items():
    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
