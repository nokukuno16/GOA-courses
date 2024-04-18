user_input = input("Enter: ")
i = len(user_input)
if i > 3:
    print(user_input[0:3])
elif i < 3 or i == 3:
    print(user_input[0])