#5
user_numbers = list(map(int, input("შეიყვანეთ 10 რიცხვი, მძიმით გამოყოფილი: ").split(',')))

print("პირველი სამი რიცხვი:", user_numbers[:3])

middle_four = user_numbers[3:7]
print("შუა ოთხი ელემენტი:", middle_four)

is_last_ten = user_numbers[-1] == 10
print("სიის ბოლო ელემენტი 10-ია?", is_last_ten)
