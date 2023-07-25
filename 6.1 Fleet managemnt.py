class Company:
    def __init__(self , name , address ) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter =[]
        self.manager =[]
        self.supervisors = []
        self.fair = []


class Driver :
    def __init__ (self , name , licence , age ) -> None:
        self.licence = licence
        self.name = name
        self.age = age

class Counter:
    pass

class Passanger:
    pass

class Supervison:
    pass

red_mia = Driver('a','123',32)

