usernames = input().split(", ")
valid = []
is_valid = False
for username in usernames:
    if 3 <= len(username) <= 16:
        is_valid = True
    else:
        is_valid = False
        continue
    for char in username:
        if not char.isalnum() or char == "-" or char == "_":
            is_valid = False
            continue
        else:
            is_valid = True
    if "!" not in username and "." not in username and "?" not in username:
        is_valid = True
    else:
        is_valid = False
        continue
    if "@" in username:
        is_valid = False
        continue
    if is_valid:
        valid.append(username)
print("\n".join(map(str, valid)))