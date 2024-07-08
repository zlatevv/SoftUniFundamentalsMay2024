text = input()
letters = {}
for letter in text:
    if letter == " ":
        continue
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
for letter, occurrences in letters.items():
    print(f"{letter} -> {occurrences}")