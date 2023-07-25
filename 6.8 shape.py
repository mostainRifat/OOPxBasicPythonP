from math import pi

class shape:
    def __init__(self, name) -> None:
        self.name = name


class Rectangle(shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.area * self.width


class circle(shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
