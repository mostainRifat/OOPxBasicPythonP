class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.account_number = self.bank.create_account(name, 0)

    def deposit(self, amount):
        self.bank.deposit(self.account_number, amount)

    def withdraw(self, amount):
        return self.bank.withdraw(self.account_number, amount)

    def transfer(self, receiver_account, amount):
        return self.bank.transfer(self.account_number, receiver_account, amount)

    def check_balance(self):
        return self.bank.check_balance(self.account_number)

    def check_transaction_history(self):
        return self.bank.check_transaction_history(self.account_number)