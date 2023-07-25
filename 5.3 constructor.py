class Phone:
    manufructured = 'china'

    def __init__(self, owner , brand , price) :
        self.owner = owner
        self.brand = brand
        self.price = price


    def sendSms ( self , phone , sms):
        text = f'sending to : {phone} {sms}'
        print(text)

myPhone = Phone('Kalu','Oppo',34000)
print(myPhone.owner,myPhone.brand,myPhone.price)

herPhone = Phone('She ', 'iPhone',80000)
print(herPhone.owner , herPhone.brand , herPhone.price)

# myPhone.sendSms()
# herPhone.sendSms()

