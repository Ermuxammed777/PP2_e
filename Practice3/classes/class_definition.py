#ex1
class Cat:
    def __init__(self, name, color):
        self.name = name   # У каждого кота свое имя
        self.color = color # И свой цвет

    def say_meow(self):
        print(f"{self.name} говорит: Мяу!")

# Создаем двух РАЗНЫХ котов по одному чертежу
barsik = Cat("Барсик", "черный")
murka = Cat("Мурка", "белая")

barsik.say_meow() # Барсик говорит: Мяу!
print(murka.color) # белая

#ex2
class Hero:
    def __init__(self, nickname):
        self.nickname = nickname
        self.hp = 100  # У всех в начале 100 здоровья

    def take_damage(self, points):
        self.hp -= points
        print(f"Ой! У {self.nickname} осталось {self.hp} HP")

# Играем
steve = Hero("Steve")
steve.take_damage(20) # Ой! У Steve осталось 80 HP

#ex3
class Sandwich:
    def __init__(self, bread_type, filling):
        self.bread = bread_type
        self.filling = filling

    def show(self):
        print(f"Ваш заказ: бутерброд из {self.bread} с {self.filling}!")

# Готовим
my_lunch = Sandwich("черного хлеба", "колбасой")
my_lunch.show() # Ваш заказ: бутерброд из черного хлеба с колбасой!