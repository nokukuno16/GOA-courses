def list_converter(first_list, second_list):
    new_list = []
    for i in first_list:
        for j in second_list:
            if i != j:
                new_list += i
                new_list += j
                print(new_list)
            else:
                first_list.remove(j)
                second_list.remove(i)
            

list_converter([1,2,3,45, 6], [2,6,7,1,3])