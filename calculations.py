add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: int(x / y)

operator = input()
num1 = int(input())
num2 = int(input())

if operator == "add":
    print(add(num1, num2))
elif operator == "subtract":
    print(subtract(num1, num2))
elif operator == "multiply":
    print(multiply(num1, num2))
elif operator == "divide":
    print(divide(num1, num2))

