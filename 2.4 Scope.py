balance = 3000

def buy_things(item, price):
    global balance
    print(f'previous balance value',balance)
    balance = balance - price
    print ( f'Balance after Buying{item} :', balance)

buy_things('SunGlass ', 1000)

#we can acces a global variable without using the global key word 
#but we cann't modify the value
