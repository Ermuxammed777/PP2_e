#give example to super function in python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class constructor

        self.color = color
    def speak(self):
        return "Meow!"
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.color)  # Output: Tabby

print(cat.speak())  # Output: Meow!
