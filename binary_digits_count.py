number = int(input())
to_find = int(input())
count = 0
ml = []
while number >= 1:
    if number % 2 == 0:
        ml.append(0)
    else:
        ml.append(1)
    number = number // 2
print(ml.count(to_find))