def pallindrome(lst: str) -> bool:
    if lst == lst[::-1]:
        return True
    
    return False



numbers = input().split(", ")
for num in numbers:
    print(pallindrome(num))