trains = []
wagons = int(input())
for _ in range(wagons):
    number = 0
    trains.append(number)
command = input().split()
while "End" not in command:
    comm = command[0]
    if comm == "add":
        people = command[1]
        trains[wagons - 1] += int(people)
    elif comm == "insert":
        index = int(command[1])
        people = int(command[2])
        trains[index] += people
    elif comm == "leave":
        index = int(command[1])
        people = int(command[2])
        trains[index] -= people

    command = input().split()
print(trains)