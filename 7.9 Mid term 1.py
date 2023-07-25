class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


result1 = MathOperations.add(3, 5)
print(result1)

result2 = MathOperations.multiply(2, 4)
print(result2)


class Parent:
    @classmethod
    def class_method(cls):
        print("Parent class method")


class Child(Parent):
    @classmethod
    def class_method(cls):
        print("Child class method")


Parent.class_method()  # Output: Parent class method
Child.class_method()  # Output: Child class method
