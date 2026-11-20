# Example 7 (Hard) MINI PROJECT 2: ATM menu system
balance = 5000.00

print("=== WELCOME TO THE PYTHON BANK ===")

running = True
while running:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print(f"Your balance is PHP {balance:,.2f}")

    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        if amount <= 0:
            print("Amount must be more than zero.")
        else:
            balance += amount
            print(f"Deposited PHP {amount:,.2f}. New balance: PHP {balance:,.2f}")

    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Amount must be more than zero.")
        elif amount > balance:
            print(f"Insufficient funds. You only have PHP {balance:,.2f}.")
        else:
            balance -= amount
            print(f"Withdrew PHP {amount:,.2f}. New balance: PHP {balance:,.2f}")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please pick 1 to 4.")
