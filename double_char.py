command = input()
while command != "End":

    text = command
    if text != "SoftUni":
        result = ""
        for character in text:
            result += character * 2
    
    
        print(result)
    command = input()