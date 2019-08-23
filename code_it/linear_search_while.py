def linear_search(element, some_list):
    # 코드를 작성하세요.
    i = 0

    while i < len(some_list):

        if element == some_list[i]:
   
            return i
        i += 1
     
   
    return None
    
        
        
        
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
