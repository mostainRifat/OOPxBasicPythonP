class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}
        self.total_balance = 0

    def create_account(self, name, initial_balance):
        account_number = len(self.accounts) + 100
        self.accounts[account_number] = {
            'name': name,
            'balance': initial_balance,
            'transactions': []
        }
        self.total_balance += initial_balance
        return account_number

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Invalid account number."
        self.accounts[account_number]['balance'] += amount
        self.total_balance += amount
        self.accounts[account_number]['transactions'].append(f"Deposited: {amount}")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Invalid account number."

        if self.accounts[account_number]['balance'] >= amount:
            self.accounts[account_number]['balance'] -= amount
            self.total_balance -= amount
            self.accounts[account_number]['transactions'].append(f"Withdrawn: {amount}")
        else:
            print( "You have not enough Taka")

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account not in self.accounts or receiver_account not in self.accounts:
            return "Invalid account number."

        if self.accounts[sender_account]['balance'] >= amount:
            self.accounts[sender_account]['balance'] -= amount
            self.accounts[receiver_account]['balance'] += amount
            self.accounts[sender_account]['transactions'].append(f"Transferred: {amount} to account {receiver_account}")
            self.accounts[receiver_account]['transactions'].append(f"Received: {amount} from account {sender_account}")
        else:
            return "Insufficient funds. The bank is bankrupt."
        
    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return "Invalid account number."
        return self.accounts[account_number]['balance']

    def check_transaction_history(self, account_number):
        if account_number not in self.accounts:
            return "Invalid account number."
        return self.accounts[account_number]['transactions']

    def admin_check_total_balance(self):
        return self.total_balance

    def admin_check_total_loan_amount(self):
        return sum((acc['balance'] * 2) for acc in self.accounts.values())
