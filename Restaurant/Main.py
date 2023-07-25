from Menu import Pizza , Burger, Drinks, Menu
from Restaurant import Restauraant
from User import Chef,Customer,Server,Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki Pizza',600, 'large',['Shutki', 'Peyaj' ] )
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alu Vorta',500, 'large',['Potato' , 'Onion' , 'Oil'] )
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Shutki Pizza',700, 'large',['dal', 'oil'] )
    menu.add_menu_item('pizza', pizza_3)

    #Add burger to the menu
    burger_1 = Burger('Naga Burger',240,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',440,'beef',['goru','oil'])
    menu.add_menu_item('burger',burger_2)

    #add drinks to the menu
    coke = Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha Coffee',160,False)
    menu.add_menu_item('drinks',coffee)

    #shoe menu
    menu.show_menu()

    restaurent = Restauraant('Sai Baba',500,menu)

    #add employees
    manager = Manager('Kalu Manager ', 2423,'kala@sada.com', 'kaliapur', 1500 , 'January 1 2020','Core')
    restaurent.add_employee('manager',manager)
    chef = Chef('Rustom baburchi',6,'chupa@rustom.com','rustomnagar',3500, 'Feb 1 2020','Chef','Everything')
    restaurent.add_employee('chef',chef)
    server = Server('Chotu', 238 , 'Nai', 'Restaurent',400,'March 20' ,'server')
    restaurent.add_employee('server',server)

    #show employees
    restaurent.show_employees()

    #Customer 1 placing an order
    customer_1= Customer('Shakib',6,'king@khan.com','Bonani',100000)
    order_1 = Order(customer_1, [pizza_3,coke, coffee])
    customer_1.pay_for_order(order_1)
    restaurent.add_order(order_1)

    #customer 1 paying for order 1
    restaurent.receive_payment(order_1 , 2000 , customer_1 )

    print('After 1st Customer , Revenue:',restaurent.revenue,'Balance :' ,restaurent.balance);


    #Customer 2 placing an order
    customer_2= Customer('Shakib Hasan',6,'king@khan.com','Bonani',100000)
    order_2 = Order(customer_2, [pizza_1,burger_2, coffee])
    customer_2.pay_for_order(order_2)
    restaurent.add_order(order_2)

    #customer 1 paying for order 1
    restaurent.receive_payment(order_2 , 2500 , customer_2 )

    print('After 2nd Customer , Revenue:',restaurent.revenue,'Balance :' ,restaurent.balance);

    #pay rent
    restaurent.pay_expense(restaurent.rent , 'Rent')
    print('After rent',restaurent.revenue , restaurent.balance , restaurent.expense)

    restaurent.pay_salary(server)
    print('After salary',restaurent.revenue , restaurent.balance , restaurent.expense)




#call the main
if __name__ == '__main__':
    main()