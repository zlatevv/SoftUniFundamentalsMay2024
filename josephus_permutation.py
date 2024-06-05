numbers = list(map(int, input().split()))
k = int(input())
result = []
index = 0
while numbers:
    index = (index + k - 1) % len(numbers)
    result.append(numbers.pop(index))
print(f"[{','.join(map(str, result))}]")
