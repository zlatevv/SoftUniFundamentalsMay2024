def even_numbers(lst):
    return lst % 2 == 0
numbers = list(map(int, input().split()))
print(list(filter(even_numbers, numbers)))