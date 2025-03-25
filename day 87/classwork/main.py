def elevator_distance(array):
    total_distance = 0
    for i in range(len(array) - 1):
        distance = abs(array[i] - array[i + 1])
        total_distance += distance
    return total_distance