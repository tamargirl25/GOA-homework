#საკლასო დავლება
#1 
def string_to_number(s):
    return int(s)

#2
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#3
def reverse(st):
    return st[::-1]

#4
def bool_to_word(b):
    return "Yes" if b else "No"

#5
def make_negative(number):
    return -abs(number)

#6
def square_sum(numbers):
    return sum(x**2 for x in numbers)
