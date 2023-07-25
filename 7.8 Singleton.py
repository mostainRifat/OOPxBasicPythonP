# singleton --> one single instance
# if you want a new instance , you will get the old one(already created instance)

class Singletone:
    __instance = None
    def __init__(self) -> None:
        if Singletone.__instance is None:
            Singletone.__instance = self

        else:
            raise Exception('This is Singletone')

    @staticmethod
    def get_instance():
        if Singletone.__instance is None:
            Singletone()
        return Singletone.__instance

first = Singletone.get_instance()

print(first)