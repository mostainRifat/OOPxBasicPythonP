class Shop:
    shopping_mall = 'jamuna'
    
    def __init__(self , buyer):
        self.buyer = buyer
        self.cart= [] #cart is an instance attribute
    
    def add_to_cart (self,item):
        self.cart.append(item)
        
mehjab = Shop('meh jabeen')
mehjab.add_to_cart('shoes')
mehjab.add_to_cart('phone')
print(mehjab.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)