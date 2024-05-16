n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2 == 1:
        print(f"{a} is odd!")
        break
else:
    print("All numbers are even.")
