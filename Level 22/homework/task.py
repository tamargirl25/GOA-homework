#1
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(4))  
print(even_or_odd(7))  

#2
def greet(name):
    print(f"Hello {name}")

greet("Giorgi")
greet("Mariam")

#3
def concatenate_strings(str1, str2):
    return str1 + str2

print(concatenate_strings("Hello, ", "World!"))