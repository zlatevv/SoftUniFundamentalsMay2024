text = input()
result = ""
last_character = ""
for letter in text:
    if letter != last_character:
        result += letter
        last_character = letter
print(result)