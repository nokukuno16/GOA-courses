def char_concat(word):
    n = len(word)
    if n % 2 == 1:  # If length is odd, remove the middle character
        word = word[:n//2] + word[n//2+1:]

    result = []
    half = len(word) // 2  # New length after removing middle if necessary

    for i in range(half):
        left = word[i]
        right = word[-(i+1)]
        result.append(f"{left}{right}{i+1}")

    return "".join(result)