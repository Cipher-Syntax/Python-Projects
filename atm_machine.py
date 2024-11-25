import sys
import os
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

balance = 0 
while True:
    print("================================================================")
    print(f"{'ATM Machine':^60}")
    print("================================================================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("================================================================")
    try:  
        user_choice = int(input("Enter your choice: "))
        clear_screen()

        if user_choice == 1:
            print("================================================================")
            print(f"{'Check Balance':^60}")
            print("================================================================")
            print(f"Your current balance is: ${balance}\n")

        elif user_choice == 2:
            print("================================================================")
            print(f"{'Deposit Money':^60}")
            print("================================================================")
            try:
                deposit_amount = float(input("Enter the amount to deposit: $"))
                balance += deposit_amount
                print(f"\nDeposit successful....Your new balance is: ${balance}")
            except ValueError:
                print("\nInvalid input....Please enter a valid amount.")

        elif user_choice == 3:
            print("================================================================")
            print(f"{'Withdraw Money':^60}")
            print("================================================================")
            try:
                withdraw_amount = float(input("Enter the amount to withdraw: $"))
                if withdraw_amount > balance:
                    print("\nInsufficient funds....")
                else:
                    balance -= withdraw_amount
                    print(f"\nWithdrawal successful....Your new balance is: ${balance}")
            except ValueError:
                print("Invalid input....Please enter a valid amount.")

        elif user_choice == 4:
            print("\nThanks for the transaction...Have a nice day")
            sys.exit(0)
    except ValueError:
        print("\nInvalid choice....Please enter a number.")