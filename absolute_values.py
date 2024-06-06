def abss(ml):
    ml_abs = []
    for num in ml:
        num  = float(num)
        ml_abs.append(abs(num))
    return(ml_abs)
data = input().split()
print(abss(data))