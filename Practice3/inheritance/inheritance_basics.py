#ex1

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")

print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!


#ex2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

car = Car("Toyota", "Corolla")

print(car.make)  # Output: Toyota
print(car.model)  # Output: Corolla
print(car.start_engine())  # Output: Car engine started

