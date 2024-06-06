def round_num(ml):
    rounded = []
    for num in ml:
        rounded.append(round(num))
    return(rounded)
data = list(map(float, input().split()))
print(round_num(data))