# print ('Now I want money')5

money_1 = input("kodom Give me some money : ")
# print("here is your money : ", money)
money_2 = input("Peyara give me some money : ")
# by default the input from user will be string type 

print(type(money_2))

intMoney_1= int(money_1)
intMoney_2= int(money_2)

total = money_1 + money_2
intTotal = intMoney_1 + intMoney_2

print('total I got :', total)
print('Total money actual :', intTotal)


