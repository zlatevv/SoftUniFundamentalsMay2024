import random
fruits = ["🍇", "🍒", "🍋", "🍍", "🍉"]
balance = float(input("Please enter your balance: "))
while balance > 0:
    bet = float(input("Enter the money you want to bet:"))
    while bet > balance:
        print("You ain't got that much money lil bro 💀")
        bet = float(input("Enter the money you want to bet (make sure it's within your balance 💀):"))
    r1 = random.choice(fruits)
    r2 = random.choice(fruits)
    r3 = random.choice(fruits)
    print(r1, r2, r3)
    if r1 == r2 == r3:
        print(f"You won the jackpot! Your new balance is {balance +  bet * 10:.2f}€")
        balance += bet * 10
    elif r1 == r2 or r2 == r3:
        print(f"You won! Your new balance is {balance + bet * 2:.2f}€")
        balance += bet * 2
    else:
        print(f"You lost 💀. Your new balance is {balance - bet:.2f}€")
        balance -= bet


