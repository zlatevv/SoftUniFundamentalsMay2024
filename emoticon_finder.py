text = input()
emoticons = []
for word in range(len(text) - 1):
    if text[word] == ":" and not text[word + 1].isspace():
        emoticons.append(text[word:word + 2])
print("\n".join(map(str, emoticons)))

