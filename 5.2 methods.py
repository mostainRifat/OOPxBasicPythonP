def call():
    print('Calling someone')
    return 'call done'

class phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'flash']

    def call(self):
        print('calling one person')

    def sendSms(self, phone, sms):
        text = f'sending sms to : {phone} and message : {sms}'
        return text

myPhone = phone()
print(myPhone.features)
myPhone.call()
result = myPhone.sendSms(20392 , ' I miss you ')
print(result)