vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
text = input()
no_vowels = [vowel for vowel in text if vowel not in vowels]
print(*no_vowels, sep = "")