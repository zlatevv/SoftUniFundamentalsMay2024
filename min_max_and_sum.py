def smallest(lst):
    return "The minimum number is" + " " + str(min(lst))
def biggest(lst):
    return "The maximum number is" + " " + str(max(lst))
def total(lst):
    return "The total is:" + " " + str(sum(lst))  



numbers = list(map(int, input().split()))
print(smallest(numbers))
print(biggest(numbers))
print(total(numbers))