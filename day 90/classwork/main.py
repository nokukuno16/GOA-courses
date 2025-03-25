def reverse_letter(st):
    filtered_st = ""
    for char in st:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            filtered_st += char 
    reversed_st = ""
    
    
    for i in range(len(filtered_st) - 1, -1, -1):
        reversed_st += filtered_st[i]  
    
    return reversed_st