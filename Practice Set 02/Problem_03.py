account_balance = 50000

withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount < 100:
    print("Minimum withdrawal amount is 100")

elif withdrawal_amount > 25000:
    print("Maximum withdrawal amount is 25000")

elif withdrawal_amount % 100 != 0:
    print("Withdrawal amount must be a multiple of 100")

elif withdrawal_amount > account_balance:
    print("Insufficient Balance")

else:
    account_balance = account_balance - withdrawal_amount

    print("Withdrawal Successful!")
    print("Withdrawn Amount:", withdrawal_amount)
    print("Remaining Balance:", account_balance)
