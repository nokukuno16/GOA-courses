s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    is_valid = s1 + s2 > s3

