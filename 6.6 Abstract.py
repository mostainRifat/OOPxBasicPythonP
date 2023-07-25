#abstract base class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #inforce all derived class to have eat method
    def eat(self):
        print("I need food ")

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name 
        self.category = 'Monkey'
        super().__init__()

    def eat(self):
        print('Eating banana')
    
    def move(self):
        print('Hanging on the road')

layka = Monkey('Lucky')
layka.eat()
layka.move()