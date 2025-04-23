def xor(a,b):
    if a == False and b == False:
        return False
    elif a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    else:
        return False
    


def nth_even(n):
    return (n - 1) * 2




def combat(health, damage):
    if health - damage > 0:
        return health - damage
    else:
        return 0
    

def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 13:
        return n - 1
    else:
        return n - 2
