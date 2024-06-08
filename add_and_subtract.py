def sum_numbers(first, second):
    return first + second
def subtract_numbers(result, third):
    return result - third
def add_and_subtract(first, second, third):
    result_sum = sum_numbers(first, second)
    result = subtract_numbers(result_sum, third)
    return result
first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first, second, third))