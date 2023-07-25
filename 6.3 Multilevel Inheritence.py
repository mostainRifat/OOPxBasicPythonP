class vehicles : 
    def __init__(self,name,price)-> None:
        self.name = name 
        self.price = price

    def move(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

class bus(vehicles):
    def __init__(self,name,price,seat )-> None:
        self.seat = seat
        super(). __init__(name , price)

    def __repr__(self) -> str:
        return super().__repr__()

class truck(vehicles):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight 
        super().__init__(name, price)

class pickUp(truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class acbus(bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()

greenLine = acbus('green',5000000,34,24)
print(greenLine)