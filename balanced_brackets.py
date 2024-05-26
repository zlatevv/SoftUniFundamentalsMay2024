number_of_lines = int(input())
balanced = True
open_bracked = False
for i in range(number_of_lines):
    line = input()
    if line == "(":
        if open_bracked:
            balanced = False
        else:
            open_bracked = True
    elif line == ")":
        if not open_bracked:
            balanced = False
        else:
            open_bracked = False
if open_bracked:
    balanced = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
