class Person:
    def __init__(self , name, age, height, weight) -> None:
        self.name = name 
        self.age= age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mach polao dim')



class Cricketer (Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # Over Ride
    def eat(self):
        print('Vegitables')

    def exercise(self):
        print('Gym ee giye gham jhorai')
    
    # + sign operator overload
    def __add__(self,other):
        return self.age + other.age 
    
    def __mul__ (self, other):
        return self.weight * other.weight
    
    def __len__ (self):
        return self.height
    
    def __gt__ (self,other):
        return self.age> other.age

sakib  = Cricketer('Sakib' , 38 , 70 , 91 , 'BD')
mushi = Cricketer('Mushi',36, 65, 78 , 'BD')

# sakib.eat()
# sakib.exercise()


# Plus Sign Overload
print(4 + 9)
print('Sakib' + 'Rakib')
print([5,6,23] + [88 , 34 , 55])

print(sakib + mushi)
print(sakib * mushi)

print(len(sakib))
print(sakib > mushi)