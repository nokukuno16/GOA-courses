# მომხმარებლისგან სტრინგის შეყვანა
user_string = input("შეიყვანეთ სტრინგი: ")

# მომხმარებლისგან დასაწყისი ინდექსის შეყვანა
start_index = int(input("შეიყვანეთ დასაწყისი ინდექსი: "))

# Slicing-ის გამოყენება
sliced_string = user_string[start_index:]

# შედეგის გამოტანა
print("ამოჭრილი სტრინგი:", sliced_string)
