numbers = list(map(int , input().split(", ")))
md = {
    "Positive":[number for number in numbers if number >= 0],
    "Negative":[number for number in numbers if number < 0],
    "Even":[number for number in numbers if number % 2 ==  0],
    "Odd":[number for number in numbers if number % 2 != 0],
}
for key, value in md.items():
    print(f"{key}: {', '.join(map(str, value))}")