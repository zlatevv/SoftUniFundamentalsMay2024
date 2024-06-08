def odd_even_sum(number: str) -> str:
    even_sum = 0
    odd_sum = 0
    for num in number:
        num = int(num)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
number = input()
print(odd_even_sum(number))