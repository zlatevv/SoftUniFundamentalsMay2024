students = {}
student_count = int(input())
for _ in range(student_count):
    name = input()
    grade = float(input())
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]
for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")

