
for num in range(1, 51):
    if num % 5 == 0:
        print(num)

for num1 in range(2, 21):
    if num1 % 2 == 0:
        print(num1)

i = 1
for num2 in range(5, 11):
    i *= num2
    print(i)


user_number = int(input("Enter your number: "))
a = 1
for b in range(1, user_number):
    a *= b

print(user_number, ": ", a)


user_number2 = int(input("Enter number: "))
if user_number2 % 2 == 0:
    user_number2 /= 2
    print(user_number2)
else:
    user_number = (user_number * 3) + 1
    print(user_number2)

num3 = 10
while num3 > 0:
    print(num3)
    num3 -= 1