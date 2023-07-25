# static atribute  (class atribute)
# static method @staticmethod
# class method @classmethod
# difference between static and class method

class Shopping:
    cart = [] # class/static atribute
    origin = 'China'

    def __init__(self, name , location) -> None:
        self.name = name #instance atributr
        self.location = location #instance atribute

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price {price} and Remaining {remaining}')
    
    @staticmethod
    def multiply(a,b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self,item):
        print('HUdai dekhte ashchi', item)

basundhara = Shopping('Boshundhara ', 'Panthopath')
# basundhara.purchase('Lungi' , 500 , 1000)
basundhara.hudai_dekhi('Lungi')
# Shopping.purchase('af' , 2,3,4)
Shopping.hudai_dekhi('lungi Pajama')

Shopping.multiply(4,3)
basundhara.multiply(6,4)