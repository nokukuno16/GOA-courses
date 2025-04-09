def solution(text, ending):
    # First, check if ending is longer than text (invalid case)
    if len(ending) > len(text):
        return False

    # Compare characters from the end
    for i in range(1, len(ending)+1):
        if text[-i] != ending[-i]:
            return False
    return True
