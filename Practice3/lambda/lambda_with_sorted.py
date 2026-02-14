#ex1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#ex2
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)

#ex3
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)   

#ex4
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)     
#ex5
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)    