text = input()
result = ""
power = 0
for index in range(len(text)):
    if text[index] == ">":
        result += ">"
        if index + 1 < len(text) and text[index + 1].isdigit():
            power += int(text[index + 1])
    elif power > 0:
        power -= 1
    else:
        result += text[index]
print(result)
