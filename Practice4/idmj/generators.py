#Ex1
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for number in count_up_to(5):
    print(number)

#Ex2
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

#Ex3
gen = (i*i for i in range(5))

for x in gen:
    print(x)