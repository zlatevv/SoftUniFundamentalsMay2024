key = int(input())

n = int(input())

decrypted_message = ""

for _ in range(n):
    char = input()
    
    decrypted_message += chr(ord(char) + key)

print(decrypted_message)