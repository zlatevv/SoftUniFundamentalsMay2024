letters = input().split(", ")
my_dict = {}
for i in range(0, len(letters)):
    letter = letters[i]
    value = ord(letters[i])
    my_dict[letter] = value
print(my_dict)