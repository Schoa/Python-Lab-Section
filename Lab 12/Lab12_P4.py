class Account:
    def __init__(self, account_id, initial_balance=0):
        self._account_id = account_id  # Public attribute for account ID
        self.__balance = initial_balance  # Private attribute for balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful to account {self._account_id}. Updated balance: {self.__balance:.0f}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrawal successful from account {self._account_id}. Updated balance: {self.__balance:.0f}."

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance


class CheckingAccount(Account):
    def __init__(self, account_id, initial_balance=0):
        super().__init__(account_id, initial_balance)
        self.__fee = 5  # Default fee for withdrawals

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        total_withdrawal = amount + self.__fee
        if total_withdrawal > self.get_balance():
            return "Insufficient balance."
        
        # Deduct the total withdrawal (amount + fee)
        self.set_balance(self.get_balance() - total_withdrawal)
        return (f"Withdrawal successful from account {self._account_id} "
                f"(including fee of {self.__fee}). Updated balance: {self.get_balance():.0f}.")

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
            return f"Deposit successful to account {self._account_id}. Updated balance: {self.get_balance():.0f}."
        else:
            return "Invalid deposit amount."


accounts = {}
n = int(input())  # Read number of commands

for i in range(n):
    command = input().strip().split()
    
    account_id = command[0]
    
    if len(command) == 3 and command[1] == 'deposit':
        # Deposit money into the existing account
        amount = float(command[2])
        if account_id in accounts:
            print(accounts[account_id].deposit(amount))
        else:
            print("Account does not exist.")
    
    elif len(command) == 2:
        # Create an account
        if account_id not in accounts:
            a = command[1]
            accounts[account_id] = CheckingAccount(account_id, a)
            print(f"Account {account_id} created with balance: {command[1]}")
        else:
            print("Account already exists.")
    
    elif len(command) == 3 and command[1] == 'withdraw':
        # Withdraw money from the existing account
        amount = float(command[2])
        if account_id in accounts:
            print(accounts[account_id].withdraw(amount))
        else:
            print("Account does not exist.")