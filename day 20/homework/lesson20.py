words_list = []

for i in range(5):
    word = input("Please enter word: ")
    words_list.append(word)

result = ""

for word in words_list:
    result += word[0]

print(result)