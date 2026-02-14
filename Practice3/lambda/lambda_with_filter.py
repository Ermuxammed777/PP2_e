#ex1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#ex2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#ex3
names = ["Alice", "Bob", "Charlie", "David"]
short_names = list(filter(lambda name: len(name) <= 4, names))
print(short_names)

#ex4
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
greater_than_five = list(filter(lambda x: x >5, numbers))
print(greater_than_five)

#ex5
def is_adult(age):
    return age >= 18
ages = [15, 22, 17, 30, 12]
adults = list(filter(is_adult, ages))
print(adults)

