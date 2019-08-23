def binary_search(element, some_list):
    # 코드를 작성하세요.
    #for i in range(0, len(some_list)):

    start_index = 0
    end_index = len(some_list)

    for i in range(start_index, end_index):

        mid = (start_index + end_index - 1) // 2

        if some_list[mid] == element:

            return mid
        
        elif some_list[mid] > element:  

            end_index = mid

        elif some_list[mid] < element:

            start_index = mid + 1
                        
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
 
