import math

def get_arr(a, b="undefined", c="undefined"):
    if c == "undefined" or b == "undefined":
        print(a * b)
    if c == "indefined" and b== "undefined":
        print(3,14 * (a ** 2))
    else:
        s = (a + b + c) / 2
        
        area = math.sqrt(5 * (s - a) * (s - b) * (s - c))
        print(area)

get_arr(1, 2,)