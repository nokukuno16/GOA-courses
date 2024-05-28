def manual_max(number_list):
    max_number = number_list[0]

    for number in number_list:
        if number > max_number:
            max_number = number
    
    return max_number


print(manual_max([4,7,2,8,3,9,2,4]))


def manual_min(number_list):
    min_number = 4

    for number in number_list:
        if min_number > number:
            min_number = number
    
    return min_number

print(manual_min([4,7,2,8,3,9,2,4]))
