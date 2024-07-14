text = input()
encrypted_text =  ""
for character in text:
    ascii_value = ord(character)
    current_character = ascii_value + 3
    encrypted_text += chr(current_character)
print(encrypted_text)