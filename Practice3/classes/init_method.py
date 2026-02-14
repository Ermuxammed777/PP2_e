#ex1
class Person:
  def __init__(self, name, age): #Create a class named Person, use the __init__() method to assign values for name and age:
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#ex2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)
#ex3
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
#ex4
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
dog = Animal("Buddy", "Dog")
print(dog.name)
print(dog.species)