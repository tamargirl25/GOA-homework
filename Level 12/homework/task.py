#1
number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")

#2
for i in range(0, 51, 2):
    print(i)

#3
result = 1

for i in range(1, 11):  
    result *= i 
print(result)

#4
numbers = [10, 23, 45, 60, 100, 7]  
sum_divisible_by_10 = sum(num for num in numbers if num % 10 == 0)  
print(sum_divisible_by_10)

#5
number = int(input("შეიყვანეთ რიცხვი: "))

names = ["გვანცა", "ბარბარე", "მარი", "ლუკა", "თამარი"]

if 0 <= number < len(names):
    print(f"სიის {number} ინდექსზე არსებული ელემენტია: {names[number]}")
else:
    print("რიცხვი სიის ინდექსის ფარგლებს გარეთაა.")