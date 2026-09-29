correct_pin = 1234

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
else:
    print("Incorrect PIN")
