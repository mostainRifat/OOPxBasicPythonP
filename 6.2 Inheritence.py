#base class , parent classs , common attribute + funtionality class
#derived class , child class , uncommon attribute + functionality class

class Device:
    def __init__ (self , brand ,price , color , origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Device : {self.brand}'
    

class Laptop:
    def __init__ (self, memory,ssd) -> None:
         self.memory = memory
         self.ssd = ssd

    def coding (self):
        return f'Learning python and Practicing'
    
class Phone(Device):
    def __init__(self ,brand , price,color, origin , dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)
    
    def phone_call(self, number , text):
        return f'sending sms to: {number} with : {text}'
    
    def __repr__(self) -> str:
        return f'phone :{self.brand} {self.price} {self.price} {self.dual_sim} '
    
class Camera:
    def __init__ (self , pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass




#inheirtence 
myPhone = Phone('samsu' , 12000, 'silver' , 'china' ,True)
print(myPhone.brand)
print(myPhone)