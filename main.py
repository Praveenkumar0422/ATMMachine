from atm import balance, withdraw, deposit, validate_account

def main():
    userdetails = {
        "user_1": {"name": "Praveen", "account_number": "1234", "pin": "1234", "balance": 1000},
        "user_2": {"name": "hari", "account_number": "5678", "pin": "5678", "balance": 500}
    }
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    is_valid, user_info = validate_account(account_number, pin, userdetails)
    if not is_valid:
        return
    current_balance = user_info["balance"]
    while True:
        print("Choose the Transaction you want to perform:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1" or choice == "b":
            balance(current_balance)
        elif choice == "2" or choice == "w":
            amount = float(input("Enter the amount you want to withdraw: "))
            current_balance = withdraw(current_balance, amount)
        elif choice == "3" or choice == "d":
            amount = float(input("Enter the amount you want to deposit: "))
            current_balance = deposit(current_balance, amount)
        elif choice == "4" or choice == "e":
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()