words = int(input())
data = {}
for _ in range(words):
    word = input()
    synonym = input()
    if word not in data:
        data[word] = [synonym]
    else:
        data[word].append(synonym)
for word, synonyms in data.items():
    print(f"{word} - {', '.join(map(str, synonyms))}")