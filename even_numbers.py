numbers = list(map(int, input().split(", ")))
indexes = [index for index, number in enumerate(numbers) if number % 2 == 0]
print(indexes)