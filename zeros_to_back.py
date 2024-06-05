numbers = list(map(int, input().split(", ")))
zeros = []
no_zeros = []
for number in numbers:
    if number != 0:
        no_zeros.append(number)
    else:
        zeros.append(number)
result = no_zeros + zeros
print(result)