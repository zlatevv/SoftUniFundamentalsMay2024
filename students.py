students = {}
command = ''
while True:
    student_info = input()
    if ":" not in student_info:
        command = student_info
        break
    student_information = student_info.split(":")
    name = student_information[0]
    id = int(student_information[1])
    course = student_information[2]
    students[name] = [id, course]
for name, data in students.items():
    if command.startswith(data[1][0:3]):
        print(f"{name} - {data[0]}")