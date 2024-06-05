
numbers = input().split()

text = input()

numbers = [int(num) for num in numbers]

message = ""

for number in numbers:

    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    
   
    index = digit_sum % len(text)
    
   
    message += text[index]
    
    
    text = text[:index] + text[index+1:]

print(message)