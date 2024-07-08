elements = input().split()
md = {}
for i in range(0, len(elements)):
    element = elements[i]
    element = element.lower()
    if element not in md:
        md[element] = 1
    else:
        md[element] += 1
for element, occurrences in md.items():
    if occurrences % 2 != 0:
        print(element, end = " ")
