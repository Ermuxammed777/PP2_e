#ex1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#ex2
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#ex3
names = ["Alice", "Bob", "Charlie"]
uppercased = list(map(lambda name: name.upper(), names))
print(uppercased)

#ex4
numbers = [1, 2, 3, 4, 5]
incremented = list(map(lambda x: x + 1, numbers))
print(incremented)

#ex5
def add_prefix(prefix):
    return lambda name: prefix + name
add_mr = add_prefix("Mr. ")
add_ms = add_prefix("Ms. ")
print(add_mr("Smith"))
print(add_ms("Johnson"))
