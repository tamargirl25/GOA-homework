#1
print(5 == 5)
print("hello" == "world")
print(True == False)

print(10 != 5)
print("apple" != "banana")
print(4 != 4)

print(7 > 3)
print(100 > 50)
print(-5 > -10)

print(3 < 7)
print(0 < 10)
print(-1 < 5)

print(10 >= 10)
print(15 >= 10)
print(-5 >= -10)

print(5 <= 5)
print(3 <= 7)
print(0 <= 5)

#2
my_favorite_number = 7
user_favorite_number = int(input("Enter your favorite number: "))
print(user_favorite_number == my_favorite_number)

#3
print(True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)
#"ლოგიკური გამოთვლების შედეგად, ერთ-ერთი ნაწილში True-ის არსებობა იძლევა მთლიანი 
#გამოსახულების True-ს, რადგან or ოპერატორი მხოლოდ ერთი True-ს არსებობას საჭიროებს."

#4
my_last_name = "nanuashvili"
user_age = int(input("Enter your age: "))
user_last_name = input("Enter your last name: ")
print(user_age >= 18 or user_last_name == my_last_name)

#5
#ალგორითმი არის პროცესი ან მოქმედებების თანმიმდევრობა, რომელიც გამოყენებულია კონკრეტული პრობლემის გადაჭრისთვის ან მიზნის 
#მისაღწევად. ალგორითმები სისტემატურად გვთავაზობენ, რა ნაბიჯებით მივაღწიოთ სასურველ შედეგს.

#6
#ფოტოთი ალგორითმის გამოსახვა არის flowchart-ი.
#ფსევდო კოდი არის ალგორითმის გამოსახვა, რომელიც იყენებს ნატურალური ენას და პროგრამირების ელემენტებს.

#7
#control flow არის რიგი, რომლითაც სრულდება ან ფასდება ინდივიდუალური 
#განცხადებები , ინსტრუქციები ან ფუნქციის გამოძახებები იმპერატიული პროგრამისა .

#8
numbers = [int(input("Enter number: ")) for _ in range(5)]
average = sum(numbers) / 5
print(average < (numbers[0] * numbers[-1]))