texts = input().split()
result = 0
for text in texts:
    first_letter = text[0]
    last_letter = text[-1]
    number = int(text[1:-1])
    if first_letter.isupper():
        letter_position = ord(first_letter) - 64
        number /= letter_position
    else:
        letter_position = ord(first_letter) - 96
        number *= letter_position
    result += number
    if last_letter.isupper():
        letter_position = ord(last_letter) - 64
        result -= letter_position
    else:
        letter_position = ord(last_letter) - 96
        result += letter_position
print(f"{result:.2f}")

