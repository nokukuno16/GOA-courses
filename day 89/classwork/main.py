def count_letters_and_digits(s):
    count = 0
    for char in s:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
            count += 1
    return count
