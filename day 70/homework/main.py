def create_sorted_2d_array(rows, cols):

    array = [[0 for _ in range(cols)] for _ in range(rows)]
    

    value = 1  
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                array[i][j] = value
            else:
                array[i][j] = array[i - 1][j] + 1
            value += 1
    

    for i in range(1, rows):
        for j in range(1, cols):
            array[i][j] = max(array[i][j], array[i][j - 1] + 1)

    return array

rows = 4
cols = 5
sorted_array = create_sorted_2d_array(rows, cols)
for row in sorted_array:
    print(row)
