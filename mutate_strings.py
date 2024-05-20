string1 = input()
string2 = input()
last_word = string1
for i in range(0, len(string1)):
    left_side = string2[:i + 1]
    right_side = string1[i + 1:]
    result = left_side + right_side
    if result != last_word:
        print(result)
        last_word = result