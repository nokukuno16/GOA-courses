def filter_even_numbers(matrix):
    even_matrix = []

    for row in matrix:  
        even_row = []  
        for num in row: 
            if num % 2 == 0:  
                even_row.append(num) 
        even_matrix.append(even_row)  

    return even_matrix


my_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


filtered_matrix = filter_even_numbers(my_matrix)
print(filtered_matrix)
