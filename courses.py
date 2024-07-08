courses = {}
while True:
    data = input().split(" : ")
    if data[0] == "end":
        break
    name = data[0]
    student = data[1]
    if name not in courses:
        courses[name] = [student]
    else:
        courses[name].append(student)
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
