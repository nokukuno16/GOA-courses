def matrix_sum(matrix1, matrix2):
    # ორი მატრიცის ზომა უნდა დაემთხვეს
    rows = len(matrix1)
    cols = len(matrix1[0])

    # ახალი მატრიცა ჯამის შესანახად
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # მატრიცების ელემენტების ჯამი
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# გამოყენება
matrix1 = [[1, 3], [1, 4]]
matrix2 = [[4, 1], [2, 2]]
print(matrix_sum(matrix1, matrix2))