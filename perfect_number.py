def perfect(number):
    total = 0
    for num in range(1, number):
        if number% num == 0:
            total += num
    if total == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."



number = int(input())
print(perfect(number))