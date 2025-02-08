def points(games):
    points = 0
    for i in games:
        if i[0] > i[2]:
            points += 3
        elif i[0] == i[2]:
            points += 1
        elif i[0] < i[2]:
            points += 0
        
    return points