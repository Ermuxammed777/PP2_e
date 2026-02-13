#ex1
def my_function():
  print("Hello from a function")

my_function()

#ex2
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#ex3
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#ex4
def my_function():
    pass

#ex5
def my_function(x , y):
   return x + y

a , b = map(int, input("Enter two numbers: ").split())
result = my_function(a, b)
print("The sum is:", result)
