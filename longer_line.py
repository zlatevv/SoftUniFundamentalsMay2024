from math import sqrt, floor

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closer_to_origin(x1, y1, x2, y2):
    dist1 = sqrt(x1**2 + y1**2)
    dist2 = sqrt(x2**2 + y2**2)
    if dist1 <= dist2:
        return (x1, y1, x2, y2)
    else:
        return (x2, y2, x1, y1)

def format_point(x, y):
    return f"({floor(x)}, {floor(y)})"

def long_line(a, b, c, d, e, f, g, h):
    length1 = distance(a, b, c, d)
    length2 = distance(e, f, g, h)
    
    if length1 >= length2:
        x1, y1, x2, y2 = closer_to_origin(a, b, c, d)
        result = f"{format_point(x1, y1)}{format_point(x2, y2)}"
    else:
        x3, y3, x4, y4 = closer_to_origin(e, f, g, h)
        result = f"{format_point(x3, y3)}{format_point(x4, y4)}"
    
    return result


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
fourth_x = float(input())
fourth_y = float(input())
print(long_line(first_x, first_y, second_x, second_y, third_x, third_y, fourth_x, fourth_y))