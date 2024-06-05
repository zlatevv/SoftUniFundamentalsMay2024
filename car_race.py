numbers = list(map(int, input().split()))
racer_one_time = 0
racer_two_time = 0

middle_index = len(numbers) // 2

left_side = numbers[:middle_index]
right_side = numbers[middle_index+1:][::-1]
for number in left_side:
    racer_one_time += number
    if number == 0:
        racer_one_time *= 0.8
for number in right_side:
    racer_two_time += number
    if number == 0:
        racer_two_time *= 0.8
if racer_one_time < racer_two_time:
    print(f"The winner is left with total time: {racer_one_time:.1f}")
else:
    print(f"The winner is right with total time: {racer_two_time:.1f}")
