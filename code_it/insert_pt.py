#some_list = [4, 5, 3, 1, 2]
some_list = [11, 3, 6, 4, 12, 1, 2]
 
for i in range(0, len(some_list)):

    for j in range(0,len(some_list)):

        if some_list[i] < some_list[j]:
            some_list[i], some_list[j] = some_list[j], some_list[i] 
 
                
    print(some_list)                        
            

 

        
 
