def disemvowel(string_):
    result = "" 
    vowels = "aeiouAEIOU"
    for i in string_:
        if i not in vowels:
            result += i
    return result