class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def chechout(self,amount):
        total =0 
        for item in self.cart:
            print (item)
            total += item['price'] * item['quantity']
        print ('total price = ' , total)

        if amount<total:
            print(f'please provide {total - amount} more ')

        else:
            extra = amount - total
            print(f'HEre is your extra money {extra}')

Shopon = shopping("Alan Shopon")
Shopon.add_to_cart("alu ", 50, 6)
Shopon.add_to_cart("dim ", 12, 12)
Shopon.add_to_cart("potol ", 50, 5)

print(Shopon.cart)
Shopon.chechout(2000)