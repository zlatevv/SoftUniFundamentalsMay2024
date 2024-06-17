def decipher_word(word):
    i = 0
    while i < len(word) and word[i].isdigit():
        i += 1

    char_code = int(word[:i])
    first_letter = chr(char_code)
    
    rest_of_word = word[i:]
    
    if len(rest_of_word) < 2:
        return first_letter + rest_of_word

    char_list = list(rest_of_word)

    char_list[0], char_list[-1] = char_list[-1], char_list[0]
    
    return first_letter + ''.join(char_list)

def decipher_message(message):
    words = message.split()
    deciphered_words = [decipher_word(word) for word in words]
    return ' '.join(deciphered_words)


secret_message = input()
print(decipher_message(secret_message))  
