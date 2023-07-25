# poly -> many
#morph -> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def makeSound(self):
        print('Animal making some sound')

class cat(Animal):
    def __init__(self,name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('meow meow')

class dog (Animal):
    def __init__(self,name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('Ghew Ghew')

class goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('Suiiiiii')

don = cat('Real Don')
don.makeSound()

shepard = dog('local shepard')
shepard.makeSound()

ron = goat('CR7')
ron.makeSound()

less = goat('mess')

animals = [don,shepard,ron,less]
for animal in animals:
    animal.makeSound()