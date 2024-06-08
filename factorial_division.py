def factorial_division(num1, num2):
    fact1 = 1
    fact2 = 1
    for i in range(1, num1 + 1):
        fact1 *= i
    for i in range(1, num2 + 1):
        fact2 *= i
    return f"{fact1 / fact2:.2f}"
first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))