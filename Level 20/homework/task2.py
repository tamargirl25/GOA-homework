#დავალება
#1
def double_integer(i):
    return i * 2

#2
def friend(x):
    return [name for name in x if len(name) == 4]

#3
from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr)

#4
def number_to_string(num):
    return str(num)

#5
def other_angle(a, b):
    return 180 - (a + b)

#6
def solution(string, ending):
    return string.endswith(ending)

#7
def is_palindrome(s):
    return s.lower() == s[::-1].lower()

#8
def sum_cubes(n):
    return sum(i**3 for i in range(1, n + 1))
