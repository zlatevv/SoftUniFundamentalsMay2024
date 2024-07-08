phonebook = {}
names = 0
while True:
    data = input().split("-")
    if not data[0].isalpha():
        names = int(data[0])
        break
    name = data[0]
    number = data[1]
    phonebook[name] = number
for _ in range(names):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
