def get_min_num(lst):
    min_num = lst[0]                                     
    for i in lst:                                           
        if i < min_num:                                  
            min_num = i                                  
    return min_num                                      



def get_min_num1(lst):
    min_num1 = lst[0]                                  
    for i in lst:                                           
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  
            if min_num1 > lst[j]:                       
                min_num1 = lst[j]                       
    return min_num1                                     


first_list = [100, 50, 3, 4, 23, 10]

print(get_min_num(first_list))

print(get_min_num1(first_list))
