password = "nikolas123"
password1 = input("Enter password: ")

i = 1

while password1 != password:
    password1 = input("Enter correct password: ")   
    print("i sed you enter correct password ", i, "times")
    if password1 == password:
        print("password vas correct")
    i += 1
    if i == 5:
        print("sistem blocked")


