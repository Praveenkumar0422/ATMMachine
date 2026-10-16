def balance(current_balance):
    print(f"Your current balance is: ${current_balance}")

def withdraw(current_balance, amount):
    if amount > current_balance:
        print("Insufficient funds.")
        return current_balance
    else:
        current_balance -= amount
        print(f"You have withdrawn ${amount}. Your new balance is: ${current_balance}")
        return current_balance

def deposit(current_balance, amount):
    current_balance += amount
    print(f"You have deposited ${amount}. Your new balance is: ${current_balance}")
    return current_balance

def validate_account(account_number, pin, userdetails):
    
    for user in userdetails.values():
        if user['account_number'] == account_number and user['pin'] == pin:
            print(f"Welcome To ATM {user['name']}!")
            return True, {"balance": user['balance']}
    else:
        print("Invalid account number.")
        return False, {"balance": 0}


