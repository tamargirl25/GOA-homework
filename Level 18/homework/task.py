#1
def multiply_numbers(a, b):
    print(a * b)

multiply_numbers(5, 3)

#2
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(4))
print(is_even_or_odd(7))

#3
def greet_name(name):
    print(f"Hello {name}")

greet_name("Giorgi")
greet_name("Nino")

#4
def concatenate_strings(str1, str2):
    return str1 + str2

result = concatenate_strings("Hello, ", "World!")
print(result)
