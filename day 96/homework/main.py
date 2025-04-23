def odd_count(n):
    result = []
    i = 1
    while i < n:
        i += 2
        result.append(i)
    return len(result)
        

def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
    return True