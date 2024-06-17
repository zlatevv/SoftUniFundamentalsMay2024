def number_sorting(numbers):
    groups = 10
    result = []
    while numbers:
        group = [number for number in numbers if number <= groups]
        numbers = [number for number in numbers if number > groups]
        result.append(f"Group of {groups}'s: {group}")
        groups += 10
    return result

numbers = list(map(int, input().split(", ")))
print(*number_sorting(numbers), sep = "\n")