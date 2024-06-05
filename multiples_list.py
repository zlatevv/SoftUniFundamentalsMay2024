factor = int(input())
count = int(input())
number = 0
ml = []
for _ in range(count):
    number += factor
    ml.append(number)
print(ml)