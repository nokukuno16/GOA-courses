def matrix_sum(matrix1, matrix2):
    # ვამოწმებთ, რომ ორივე მატრიცას აქვს ერთი და იგივე ზომა
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("მატრიცები უნდა იყოს ერთნაირი ზომის")

    # ვქმნით მატრიცას, რომელიც შეიცავს ჯამს
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            # თითოეული ელემენტის ჯამი
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

# გამოყენების მაგალითი
matrix1 = [
    [1, 3],
    [1, 4]
]

matrix2 = [
    [4, 1],
    [2, 2]
]

sum_matrix = matrix_sum(matrix1, matrix2)
print(sum_matrix) 