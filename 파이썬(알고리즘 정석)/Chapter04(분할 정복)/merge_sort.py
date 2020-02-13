def merge(list1, list2):

    merged_list = [] # list1과 list2를 파라미터로 받고 합쳐진 리스트 이걸 return 해줌

    # list1과 list2는 이미 정렬되어 있기 때문
    # merged_list에 먼저 추가될 원소는 두 리스트의 왼쪽 값 중 더 작은 값

    '''
    if len(list1) == 0:
        return merged_list + list2
    elif len(list2) == 0:
        return list1 + merged_list

    if list1[0] > list2[0]:
        merged_list.append(list2[0])
        return merged_list + merge(list1, list2[1:])
    elif list1[0] < list2[0]:
        merged_list.append(list1[0])
        return merged_list + merge(list1[1:], list2)
    '''
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

        if len(list1) == i:
            merged_list += (list2[j:])
        elif len(list2) == j:
            merged_list += (list1[i:])

    return merged_list

    #list[1:n] -> 시간 복잡도 증가...
# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))