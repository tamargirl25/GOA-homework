#2
number = input("Enter a number: ")
for digit in number:
    print(digit)

#3
number = int(input("Enter a number: "))
for i in range(number, -1, -1):
    print(i)

#4
number = 1
while number <= 20:
    if number % 2 != 0:
        print(number)
    number += 1

#5
for i in range(0, 21, 2):
    print(i)

#6
#for ციკლი გამოიყენება, როცა წინასწარ ვიცით, რამდენჯერ გვინდა კოდის შესრულება ან როცა ვმუშაობთ სიის ელემენტებზე.
for i in range(5):
    print(i)
#while ციკლი მუშაობს მანამ, სანამ მოცემული პირობა არის ჭეშმარიტი.
i = 0
while i < 5:
    print(i)
    i += 1
#ცვლადი არის კონტეინერი, რომელიც ინახავს გარკვეულ მონაცემს. ცვლადის სახელის მეშვეობით ჩვენ შეგვიძლია მივუთითოთ,
#დავამუშავოთ და გამოვიყენოთ მონაცემები პროგრამაში. ცვლადი იმახსოვრებს მონაცემთს და ჩვენ შეგვიძლია გამოვიყენოთ იგი პროგრამის 
#სხვადასხვა ნაწილებში.