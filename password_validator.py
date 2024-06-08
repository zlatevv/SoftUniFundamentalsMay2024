def validation(password):
    is_valid = False
    if len(password) >= 6 and len(password) <= 10:
        is_valid = True
    else:
        print("Password must be between 6 and 10 characters")
        is_valid = False
        

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    numbers = 0
    for num in password:
        if num.isdigit():
            numbers += 1
    if numbers < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")
password = input()
validation(password)
        