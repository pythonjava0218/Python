def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    merged_list = []
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

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list

    divide = len(my_list) // 2
    left = my_list[:divide]
    right = my_list[divide:]


    return merge(merge_sort(left), merge_sort(right))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))