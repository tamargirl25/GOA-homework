#4
divisible_by_500 = list(range(1000, 10001, 500))

first_five = divisible_by_500[:5]
print("პირველი ხუთი რიცხვი:", first_five)

every_third = divisible_by_500[::3]
print("ყოველი მესამე რიცხვი:", every_third)

print("სიის ელემენტების რაოდენობა:", len(divisible_by_500))
