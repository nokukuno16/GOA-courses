def manual(manual_list, manul_numbers):
    for i in manual_list:
        if i == manul_numbers:
            manual_list.remove(i)
            print(manual_list)

manual([1,2,3,4,5], 3)