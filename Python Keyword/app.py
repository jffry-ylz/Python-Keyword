# Importing necessary modules
import random

# A simple BankAccount class with multiple methods
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Setting an initial balance

    def deposit(self, amount):
        if amount <= 0:  # 'if' statement to check for valid deposit
            raise ValueError("Amount must be positive.")  # Using 'raise' to throw an exception
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:  # 'if' statement to check for valid withdrawal amount
            raise ValueError("Amount must be positive.")  # Using 'raise' again
        if amount > self.balance:  # 'if' statement to prevent overdrawing
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
    
    def show_balance(self):
        print(f"Current balance: {self.balance}")

# Define a function to simulate multiple transactions
def simulate_transactions(account):
    try:
        # Using a while loop to simulate random transactions
        for _ in range(5):  # Will loop 5 times
            transaction_type = random.choice(['deposit', 'withdraw'])
            amount = random.randint(1, 1000)

            if transaction_type == 'deposit':
                account.deposit(amount)
            elif transaction_type == 'withdraw':
                account.withdraw(amount)

    except ValueError as e:
        # Handling error if a ValueError is raised
        print(f"Error: {e}")
    finally:
        # 'finally' block will always run to show final balance
        account.show_balance()

# Main program logic
def main():
    account = BankAccount(500)  # Creating a BankAccount object with an initial balance of 500
    simulate_transactions(account)  # Simulate some transactions

# Using the 'if __name__ == "__main__"' block to allow the program to run
if __name__ == "__main__":
    main()

# Using 'with' to open a file safely for logging
with open("bank_log.txt", "w") as file:
    file.write("Bank transaction log\n")
    file.write("Transactions completed successfully.\n")

# Create a lambda function to check if an amount is even or odd
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(123))  # Example lambda usage
