def spin_words(sentence):
    words = sentence.split()  
    result = ""  

    for i in range(len(words)):
        word = words[i]
        if len(word) >= 5:
            result += word[::-1]  
        else:
            result += word
        
        if i < len(words) - 1:   
            result += " "

    return result