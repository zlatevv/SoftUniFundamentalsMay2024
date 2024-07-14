text = input()
numbers = ""
letters = ""
special = ""
for character in text:
    if character.isdigit():
        numbers += character
    elif character.isalpha():
        letters += character
    else:
        special += character
print(numbers)
print(letters)
print(special)