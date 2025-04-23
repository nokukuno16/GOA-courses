def is_vow(inp):
    result = []
    for i in inp:
        if i == ord('a'):
            result.append('a')
        elif i == ord('e'):
            result.append('e')
        elif i == ord('i'):
            result.append('i')
        elif i == ord('o'):
            result.append('o')
        elif i == ord('u'):
            result.append('u')
        else:
            result.append(i)
    return result



def who_is_paying(name):
    result = []
    if len(name) > 2:
        result.append(name)
        result.append(name[:2])
    else:
        result.append(name)
    return result


def next_id(ids):
    i = 0
    while i in ids:
        i += 1
    return i
