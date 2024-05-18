def check_int(num):
    if num % 2 == 0:
        return str(num) + " is Even"
    else:
        return str(num) + " is Odd"


print(check_int(6))