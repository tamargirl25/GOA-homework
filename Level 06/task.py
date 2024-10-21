# 1)მომხმარებელს შემოატანინეთ თავისი ასაკი და დაუბეჭდეთ, რამდენი წლის იქნება 10 წელში,
#  შემდეგ ეს შედეგი შეინახეთ ცვლადში და გადაიყვანეთ float მონაცემთა ტიპად, საბოლოოდ შეამოწმეთ მისი type.
age=int(input("how old are you: "))
age1=age+10
age_float=float(age1)
print(type(age_float))

# 2)მომხმარებელს შემოატანინეთ მისი გვარი და დაუბეჭდეთ ეს გვარი 100ჯერ გადაბმულად.
name=input("enter your name: ")
for _ in range(0,100):
    print(name)

#3)შექმენი რეალური 5 სიტყვა, კონკატინაციის მეშვეობით.
firstName="tamari"
lastName="nanuashvili"

fullName=firstName+" "+lastName
print(fullName)

#4)კომენტარის სახით ახსენით, რისთვის გვჭირდება და ვიყენებთ სხვადასხვა მონაცემთა ტიპებს.
#სხვადასხვა მონაცემთა ტიპები გამოიყენება მთელი ან წილადი რიცხვების სწორი ასახვისთვის.
#მთელი რიცხვი არის integer.
#წილადი რიცხვები არის float.

#5)შექმენით 4 ცვლადი და შეინახეთ განსხვავებული მონაცემთა ტიპის მქონე მნიშვნელობები, შემდეგ სათითაოდ დაბეჭდეთ მათი type.
variable1=7
variable2=4.2
variable3="მე ვსწავლობ პროგრამირებას"
variable4=5<7
print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))
