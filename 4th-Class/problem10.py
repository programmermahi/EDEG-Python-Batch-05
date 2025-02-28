# Initial balance
balance = 1000.0

# Function to display the menu and handle user actions
def banking_system():
    global balance
    while True:
        print("\nSimple Banking System")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-4): ")
        
        # Use match-case to handle different actions
        match choice:
            case '1':
                print(f"Your current balance is: ${balance:.2f}")
            
            case '2':
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    print(f"${amount:.2f} deposited successfully.")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Invalid amount. Please enter a positive number.")
            
            case '3':
                amount = float(input("Enter amount to withdraw: $"))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"${amount:.2f} withdrawn successfully.")
                    print(f"New balance: ${balance:.2f}")
                elif amount > balance:
                    print("Insufficient balance. Please enter a valid amount.")
                else:
                    print("Invalid amount. Please enter a positive number.")
            
            case '4':
                print("Thank you for using the Simple Banking System. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Run the banking system
banking_system()
