class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added for customer {self.name}.")

    def get_accounts(self):
        return self.accounts


class Transaction:
    @staticmethod
    def transfer(sender_account, receiver_account, amount):
        if sender_account.balance >= amount:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            print(f"Transferred {amount} from account {sender_account.account_number} to {receiver_account.account_number}.")
        else:
            print("Insufficient funds for transfer.")


# Example Usage
if __name__ == "__main__":
    # Create customers
    customer1 = Customer("Alice", "C001")
    customer2 = Customer("Bob", "C002")

    # Create accounts
    account1 = Account("A001", 1000)
    account2 = Account("A002", 500)

    # Link accounts to customers
    customer1.add_account(account1)
    customer2.add_account(account2)

    # Perform transactions
    account1.deposit(200)       # Alice deposits money
    account1.withdraw(300)      # Alice withdraws money
    account1.check_balance()    # Check Alice's balance

    # Transfer money between accounts
    Transaction.transfer(account1, account2, 400)
    account2.check_balance()    # Check Bob's balance
