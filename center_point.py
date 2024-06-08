from math import floor

def first_coordinates(a, b):
    total = abs(a) + abs(b)
    return total
def second_coordinates(a, b):
    total = abs(a) + abs(b)
    return total

first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
first = first_coordinates(first_x, first_y)
second = second_coordinates(second_x, second_y)
if first < second:
    print(f"({floor(first_x)}, {floor(first_y)})")
elif first > second:
    print(f"({floor(second_x)}, {floor(second_y)})")
else:
    print(f"({floor(first_x)}, {floor(first_y)})")