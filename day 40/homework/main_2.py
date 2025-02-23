def solution(number):
    if number < 0:
        return 0
    
    sum_result = 0
    i = 0
    
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            sum_result += i
        i += 1
    
    return sum_result