 
# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.

    new_list = []
    i = 0
    j = 0

    while len(list1) > i and len(list2) > j:
        
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
            
    if len(list1) > i :
        new_list += (list1[i:])

    elif len(list2) > j:
        new_list += list2[j:]
    return new_list

def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
        
    value = len(my_list) // 2
    left_list = my_list[:value]
    right_list = my_list[value:]

    return merge(merge_sort(left_list), merge_sort(right_list))
         
some_list = [11, 3, 6, 4, 12, 1, 2]
#some_list = [11, 3, 4, 6, 5]
sorted_list = merge_sort(some_list)
print(sorted_list)

 
