from PersonB import User
from Bank import Bank

def main():

    bank = Bank("Brack")
    admin = User("Admin", bank)

    Kala = User("Kala", bank)
    Abul = User("Abul", bank)

    Kala.deposit(1000)
    Abul.deposit(500)

    Kala.transfer(Abul.account_number, 200)
    print("Kala's Balance:", Kala.check_balance())
    print("Abul's Balance:", Abul.check_balance())

    Kala.withdraw(1500)

    print("Total Bank Balance:", admin.bank.admin_check_total_balance())
    print("Total Loan Amount:", admin.bank.admin_check_total_loan_amount())


if __name__ == '__main__':
    main()