from math import floor
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
sum1 = num1 + num2
sum2 = sum1 / num3
sum2 = floor(sum2)
final_sum = sum2 * num4
print(round(final_sum))