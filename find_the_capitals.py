word = input()
ml = []
for index, letter in enumerate(word):
    if letter.isupper():
        ml.append(index)
print(ml)