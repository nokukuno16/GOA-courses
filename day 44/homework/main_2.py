def words_to_marks(s):
    return sum(ord(char) - ord('a') + 1 for char in s)