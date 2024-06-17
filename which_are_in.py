def find_substrings(substrings, strings):
    result = []
    for substring in substrings:
        for string in strings:
            if substring in string:
                result.append(substring)
                break
    return result




substrings = input().split(", ")
strings = input().split(", ")
print(find_substrings(substrings, strings))