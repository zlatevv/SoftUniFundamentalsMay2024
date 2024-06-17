schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    commands = command.split(":")
    comm = commands[0]
    lesson = commands[1]
    if comm == "Add":
        if lesson not in schedule:
            schedule.append(lesson)
    elif comm == "Insert":
        index = int(commands[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)
    elif comm == "Remove":
        if lesson in schedule:
            schedule.remove(lesson)
        if lesson + "-Exercise" in schedule:
            schedule.remove(lesson + "-Exercise")
    elif comm == "Swap":
        lesson1 = commands[1]
        lesson2 = commands[2]
        index1 = schedule.index(lesson1)
        index2 = schedule.index(lesson2)
        schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
        if lesson1 + "-Exercise" in schedule:
            exercise1_index = index1 + 1
            exercise2_index = index2 + 1
            schedule[exercise1_index], schedule[exercise2_index] = schedule[exercise2_index], schedule[exercise1_index]
    elif comm == "Exercise":
        if lesson in schedule and lesson_exercise not in schedule:
            lesson_exercise = lesson + "-Exercise"
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index + 1, lesson_exercise)
        if lesson not in schedule:
            lesson_exercise = lesson + "-Exercise"
            schedule.append(lesson)
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index - 1, lesson_exercise)
for index, lesson in enumerate(schedule):
    print(f"{index + 1}.{lesson}")