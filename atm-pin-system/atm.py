balance = 5000
pin = 1234

attempts = 0   # Track incorrect attempts

while attempts < 3:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        amount = int(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
        break   # exit loop after successful transaction
    else:
        attempts += 1
        print("Incorrect PIN")

        if attempts == 3:
            print("Your card is blocked! Too many incorrect attempts.")
