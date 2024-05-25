a = int(input())
b = int(input())
c = a
d = b
print(f"Before:\na = {a}\nb = {b}")
a = d
b = c
print(f"After:\na = {a}\nb = {b}")