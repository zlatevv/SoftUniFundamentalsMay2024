def characters(a, b):
    lst = []
    for char in range(ord(a) + 1, ord(b)):
        lst.append(chr(char))
    return f" ".join(lst)
a = input()
b = input()
print(characters(a, b))