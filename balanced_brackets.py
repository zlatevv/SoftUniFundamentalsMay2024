number_of_lines = int(input()) 
balanced = True
open_bracket = True
for _ in range(number_of_lines):
    text = input()
    if text == "(":
        if open_bracket:
            balanced = False
            break
        open_bracket = True
    elif text == ")":
        if not open_bracket:
            balanced = False
            break
        open_bracket = False
if open_bracket:
    balanced = False
if balanced:       
    print("BALANCED")
else:
    print("UNBALANCED")