input_string = input()

str1, str2 = input_string.split()

total_sum = 0

len1 = len(str1)
len2 = len(str2)
min_len = min(len1, len2)
max_len = max(len1, len2)

for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

if len1 > len2:
    for i in range(min_len, max_len):
        total_sum += ord(str1[i])
else:
    for i in range(min_len, max_len):
        total_sum += ord(str2[i])

print(total_sum)
