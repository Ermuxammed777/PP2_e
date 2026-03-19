# enumerate()
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip()
names = ["Ali", "John", "Sara"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)


students = ["Ali", "Sara", "John", "Aruzhan"]

# Найти индексы имен длиной > 4
for i, name in enumerate(students):
    if len(name) > 4:
        print(i, name)



names = ["Ali", "Sara", "John"]
scores_math = [90, 85, 88]
scores_eng = [80, 95, 70]

# Соединяем 3 списка
for name, m, e in zip(names, scores_math, scores_eng):
    print(f"{name}: Math={m}, Eng={e}")



keys = ["name", "age", "city"]
values = ["Ali", 18, "Almaty"]

d = dict(zip(keys, values))
print(d)