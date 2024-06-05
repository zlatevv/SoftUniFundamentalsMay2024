numbers = input().split()
to_remove = int(input())
numbers = [int(x) for x in numbers]
for _ in range(to_remove):
    numbers.remove(min(numbers))
print(", ".join(map(str, numbers)))

