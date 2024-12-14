def manual(manual_list, num):
    for i in manual_list:
        if i == num:
            manual_list.remove(i)
            n = len(manual_list)
            for j in range(1, n):
                for t in range(0, n-1): 
                    if manual_list[t] > manual_list[t + 1]:
                        manual_list[t],  manual_list[t + 1] = manual_list[t + 1], manual_list[t]
                        print(manual_list)


manual([1,2,3,4,5], 3)