#ex1
class Robot:
    population = 0  # Переменная класса (общая для всех)

    def __init__(self, name):
        self.name = name  # Переменная объекта (у каждого своя)
        Robot.population += 1  # При создании каждого робота увеличиваем общий счетчик
        print(f"Робот {self.name} создан!")

# Создаем роботов
r1 = Robot("R2-D2")
r2 = Robot("C-3PO")

print(f"Всего роботов: {Robot.population}") # Выведет: 2

#ex2
class Enemy:
    difficulty = "Easy"  # Общая настройка для всех врагов

    def __init__(self, type):
        self.type = type

# Создаем двух врагов
orc = Enemy("Орк")
goblin = Enemy("Гоблин")

print(orc.difficulty)    # Easy
print(goblin.difficulty) # Easy

# Меняем сложность ОДИН раз для всего класса
Enemy.difficulty = "Hard"

print(orc.difficulty)    # Стал Hard!
print(goblin.difficulty) # Тоже стал Hard!

#ex3
class Circle:
    PI = 3.14159  # Константа, общая для всех кругов

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Используем общую переменную класса PI
        return Circle.PI * (self.radius ** 2)

c1 = Circle(10)
print(c1.area()) # 314.159