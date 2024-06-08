def multiplication(num1, num2, num3):
    is_negative = False
    negative = []
    if num1 < 0:
        negative.append(num1)
    if num2 < 0:
        negative.append(num2)
    if num3 < 0:
        negative.append(num3)
    if len(negative) % 2 == 0:
        is_negative = False
    else:
        is_negative = True
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    

    if is_negative:
        return "negative"
    elif not is_negative:
        return "positive"
a = int(input())
b = int(input())
c = int(input())
print(multiplication(a, b, c))