employee_happines = list(map(int, input().split()))
new_happines = []
happines_improvement = int(input())
for happiness in employee_happines:
    happiness *= happines_improvement
    new_happines.append(happiness)

total = 0
happy = 0
for number in new_happines:
    total += number
average_happines = total / len(new_happines)
for number in new_happines:
    if number >= average_happines:
        happy += 1
if happy >= len(new_happines) / 2:
    print(f"Score: {happy}/{len(new_happines)}. Employees are happy!")
else:
    print(f"Score: {happy}/{len(new_happines)}. Employees are not happy!")