import math

class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def factorial(self):
        return math.factorial(self.b)

obj = MyClass(4,5,6)

print("Sum :", obj.sum())
print("Factorial:", obj.factorial())
