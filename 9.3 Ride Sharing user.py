from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with Riders:{len(self.riders)} and Drivers : {len(self.drivers)}'
        


class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email

        # to do : set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0


@abstractmethod
def display_profile(self):
    raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Rider: {self.name} and eMail: {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self,ride_sharing, destination ):
        if not self.current_ride:
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print('Got the ride' ,ride)
            self.current_ride = ride

    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver Name : {self.name} eMail : {self.email}")

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details . Started : {self.start_location} to {self.end_location} '

class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            # ToDo : find the closest driver of the rider
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride


class Vehicle(ABC):
    speed = {"car": 50, "bike": 60, "cng": 25}

    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        self.vahicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.rate = rate
        self.status = 'Available'

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)

    def start_drive(self):
        self.status = 'UnAvailable'


class Bike(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)
    
    def start_drive(self):
        self.status = 'UnAvailable'


#check the class integration

niye_jao = Ride_Sharing('Niye Jao')
sakib = Rider("sakib khan" , 'sakib@khan.com' , 1254, 'Mohakhani',1200)
niye_jao.add_rider(sakib)
kalu = Driver('Kalu', 'kala@sada.com', 5634 , 'Gulshan 1' )
niye_jao.add_driver(kalu)
print(niye_jao)
sakib.request_ride(niye_jao,'Uttara')
sakib.show_current_ride()