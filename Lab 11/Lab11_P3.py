class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance # Initialize Balance
        self.interest_rate = interest_rate # Initialize Interest_Rate

    def deposit(self, amount):
        """Add the specified amount to the account balance"""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract a specified amount to the attribute balance if the owner's funds are sufficient, if it is availiable"""
        if self.balance >= amount:
            self.balance -= amount
            return True # Transaction successful
        else:
            return False # Insufficient funds
        
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def apply_interest(self):
        """Apply interest to the account balance."""
        self.balance *= self.interest_rate

    def __str__(self):
        """Return a string representation of the account's current balance."""
        return f"Current balance: {self.balance:.1f}"
    
# Input
input_data = input()
initial_balance, interest_rate, deposit_amount, withdrawal_amount = input_data.split()

# Convert inputs to appropriate types
initial_balance = int(initial_balance)
interest_rate = float(interest_rate)
deposit_amount = int(deposit_amount)
withdrawal_amount = int(withdrawal_amount)

# Create a BankAccount instance
account = BankAccount(initial_balance, interest_rate)

# Deposit money into the account
account.deposit(deposit_amount)

# Output balance after deposit
print(account)  # Uses __str__ method

# Attempt to withdraw money from the account
withdrawal_successful = account.withdraw(withdrawal_amount)

# Output result of withdrawal attempt and current balance
if withdrawal_successful:
    print(account)  # Uses __str__ method for current balance after withdrawal
else:
    print(False)  # Print False if withdrawal failed

# Apply interest to the account
account.apply_interest()

# Output balance after applying interest
print(account)  # Uses __str__ method
