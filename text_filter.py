bad_words = input().split(", ")
text = input()
for word in bad_words:
    while word in text:
        text = text.replace(word, "*" * len(word))
print(text)

