import re
line = input()
pattern = r"\b(www\.([a-zA-Z-0-9\-]+)\.([a-z]+(\.?[a-z]+)+))\b"
while line:
    match = re.search(pattern, line)
    if match:
        print(match.group(1))
    line = input()
