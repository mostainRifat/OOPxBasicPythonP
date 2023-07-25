#encapsulation --> hide detail
# access modifier 

class Bank:
    def __init__ (self, holderName , initialDeposit) -> None:
        self.holderName = holderName #Public
        self._balance = initialDeposit #protected
        self.__balance = initialDeposit #private

    def deposit(self,amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nai '

rafsun = Bank ('choto vai',30000)

print(rafsun.holderName)
rafsun.holderName= 'Boro Vai'
rafsun.deposit(40000)
# rafsun.balance = 0
print(rafsun.getBalance())
print(rafsun.holderName)
print(rafsun._Bank__balance)