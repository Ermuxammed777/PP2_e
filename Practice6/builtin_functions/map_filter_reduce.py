#Ex1
# Дан список чисел
nums = [1, 2, 3, 4, 5, 6]

# map() → возводим в квадрат
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

# filter() → только четные
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens) 


#Ex2
words = ["hello", "world", "python"]

# Сделать все слова заглавными
upper_words = list(map(str.upper, words))
print(upper_words)

# Длина каждого слова
lengths = list(map(len, words))
print(lengths)

#Ex3
nums = [12, 5, 8, 21, 30, 7]

# Оставить числа, кратные 3
div_by_3 = list(filter(lambda x: x % 3 == 0, nums))
print(div_by_3)

# Оставить числа больше 10
greater_10 = list(filter(lambda x: x > 10, nums))
print(greater_10)




nums = [1, 2, 3, 4, 5, 6]

# Берем только четные → потом умножаем на 10
result = list(map(lambda x: x * 10,
                  filter(lambda x: x % 2 == 0, nums)))

print(result) 