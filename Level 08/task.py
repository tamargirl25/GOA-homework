#1)გააკეთეთ ყველა იმ შედარების ოპერატორზე 3-3 მაგალითი რაც ვისწავლეთ.
#and ოპერატორის შემთხვევაში უნდა კმაყოფილდეს ყველა პირობა.
print(True and False) #F
print(False and True) #F
print(False and False) #F
print(True and True) #T

#or ოპერატორის დროს თუ კმაყოფილდება ერთერთი პირობა, მაშინ მთლიანი გამოსახულების შედეგი = true
print(True or False) #T
print(False or True) #T
print(True or True) #T
print(False or False) #F

#2)მომხმარებელს შემოატანინეთ მისი საყვარელი რიცხვი და გაიგეთ უდრის თუ არა მისი საყვარელი რიცხვი თქვენს საყვარელ რიცხვს.
userNumber=int(input("enter your fovrite number: "))
myNumber=7
result=userNumber == myNumber
print(result)

#3)True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <--- გაიგეთ რას გამოიტანს ეს კოდი და ახსენით რატომ.
print(True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)
#"ლოგიკური გამოთვლების შედეგად, ერთ-ერთი ნაწილში True-ის არსებობა იძლევა მთლიანი 
#გამოსახულების True-ს, რადგან or ოპერატორი მხოლოდ ერთი True-ს არსებობას საჭიროებს."

#4)მომხმარებელს შემოატანინეთ მისი ასაკი და მისი გვარი და შეამოწმეთ
#თუ ასაკი მეტი ან ტოლი იქნება 18ის ან მისი გვარი ტოლი იქნება თქვენი გვარის.
age = int(input("Please enter your age: "))
last_name = input("Please enter your last name: ")

if age >= 18 or last_name == "YourLastName":
    print("Condition met.")
else:
    print("Condition not met.")

#5)ახსენით რა არის ალგორითმი (მოიყვანეთ რეალური ცხოვრების 3 მაგალითი).
#ალგორითმი არის პროცესი ან მოქმედებების თანმიმდევრობა, რომელიც გამოყენებულია კონკრეტული პრობლემის გადაჭრისთვის ან მიზნის 
#მისაღწევად. ალგორითმები სისტემატურად გვთავაზობენ, რა ნაბიჯებით მივაღწიოთ სასურველ შედეგს.

#6)ახსენით თითოეული ის ალგორითმის გამოსახვის ტექნიკა რაც ვისწავლეთ.
#ფოტოთი ალგორითმის გამოსახვა არის flowchart-ი.
#ფსევდო კოდი არის ალგორითმის გამოსახვა, რომელიც იყენებს ნატურალური ენას და პროგრამირების ელემენტებს.

#7)ახსენით control flow-ს ის სამი ტექტინა რომელიც გავიარეთ.
#control flow არის რიგი, რომლითაც სრულდება ან ფასდება ინდივიდუალური 
#განცხადებები , ინსტრუქციები ან ფუნქციის გამოძახებები იმპერატიული პროგრამისა .

#8)მომხმარებელს შემოატანინეთ 5 რიცხვი, დაითვალეთ მათი საშუალო არითმეტიკული
#და გაიგეთ თუ მათი საშუალო არითმეტიკული ნაკლები იქენება პირველი და ბოლო რიცხვის ნამრავლზე.