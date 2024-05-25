number = int(input())
total = 0
for _ in range(number):
    symbol = input()
    total += ord(symbol)
print(f"The sum equals: {total}")