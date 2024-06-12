words = input().split()
pallindrome = input()
pallindromes = []
for word in words:
    if word == word[::-1]:
        pallindromes.append(word)
count = pallindromes.count(pallindrome)
print(pallindromes)
print(f"Found palindrome {count} times")